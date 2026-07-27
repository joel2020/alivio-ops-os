"""The rules exist in three places. This proves they agree.

  1. The markdown       — the source of truth a human reads
  2. dashboard.html     — a RULES block in JavaScript
  3. ops.py / ledger.py — the same thresholds in Python

Three copies is a design smell, and it is deliberate: the dashboard must run
from a file:// URL with no server and no build step, so it cannot import
Python, and Python cannot import JavaScript. Given that constraint the choice
is between duplication that is tested and duplication that is hoped for.

This is the test. If someone changes a chase tier in one place and not the
others, it fails here rather than six weeks later when an invoice is chased at
the wrong tier — or, worse, when the dashboard and the Monday brief quietly
disagree about which projects are red and nobody can tell which is lying.
"""

import json
import os
import re
import sys
import unittest

LIB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, LIB)

import ledger  # noqa: E402
import ops  # noqa: E402

OS_ROOT = os.path.dirname(os.path.dirname(LIB))
DASHBOARD = os.path.join(OS_ROOT, "07-dashboard", "dashboard.html")


def js_rules():
    """Pull the RULES object out of dashboard.html and read it as data."""
    with open(DASHBOARD) as f:
        src = f.read()
    m = re.search(r"const RULES = \{(.*?)\n\};", src, re.S)
    if not m:
        raise AssertionError("RULES block not found in dashboard.html")
    body = m.group(1)
    body = re.sub(r"//[^\n]*", "", body)              # line comments
    body = re.sub(r"/\*.*?\*/", "", body, flags=re.S)  # block comments
    return body


def nums_after(body, key, count=None):
    """Every number that follows `key` up to the next top-level key."""
    i = body.find(key)
    if i < 0:
        raise AssertionError(f"{key} missing from the dashboard RULES block")
    seg = body[i:]
    end = re.search(r"\n\s{2}[a-zA-Z]+:", seg[len(key):])
    if end:
        seg = seg[:len(key) + end.start()]
    out = [float(x) for x in re.findall(r"-?\d+\.?\d*", seg)]
    return out[:count] if count else out


class TestChaseTiersAgree(unittest.TestCase):

    def test_tier_days_match(self):
        py = [d for d, _, _, _ in ledger.CHASE_TIERS]
        js = js_rules()
        seg = js[js.find("chaseTiers"):]
        seg = seg[:seg.find("],") + 1]
        js_days = [int(x) for x in re.findall(r"day:\s*(\d+)", seg)]
        self.assertEqual(py, js_days,
                         "chase tier days differ between ledger.py and dashboard.html")

    def test_tier_owners_match(self):
        py = [w for _, _, w, _ in ledger.CHASE_TIERS]
        js = js_rules()
        seg = js[js.find("chaseTiers"):]
        seg = seg[:seg.find("],") + 1]
        js_who = re.findall(r'who:"([^"]+)"', seg.replace(" ", ""))
        self.assertEqual(py, js_who)


class TestPipelineAgree(unittest.TestCase):

    def test_weights_match(self):
        js = js_rules()
        seg = js[js.find("pipelineWeights"):]
        seg = seg[:seg.find("}") + 1]
        found = {k: float(v) for k, v in
                 re.findall(r'"(\w+)":\s*([\d.]+)', seg)}
        self.assertEqual(found, ops.PIPELINE_WEIGHTS,
                         "pipeline weights differ between ops.py and dashboard.html")

    def test_dwell_match(self):
        js = js_rules()
        seg = js[js.find("pipelineDwell"):]
        seg = seg[:seg.find("}") + 1]
        found = {k: int(v) for k, v in re.findall(r'"([\w ]+)":\s*(\d+)', seg)}
        self.assertEqual(found, ops.PIPELINE_DWELL)

    def test_untouched_and_coverage_match(self):
        js = js_rules()
        self.assertEqual(int(nums_after(js, "untouchedDays", 1)[0]),
                         ops.UNTOUCHED_DAYS)
        cov = nums_after(js, "coverage", 2)
        self.assertEqual([int(cov[0]), int(cov[1])],
                         [ops.COVERAGE_TARGET, ops.COVERAGE_ALARM])


class TestProjectRulesAgree(unittest.TestCase):

    def test_stage_dwell_match(self):
        js = js_rules()
        seg = js[js.find("dwellDays"):]
        seg = seg[:seg.find("}") + 1]
        found = {k: int(v) for k, v in re.findall(r'"([\w ]+)":\s*(\d+)', seg)}
        self.assertEqual(found, ops.STAGE_DWELL,
                         "stage dwell limits differ between ops.py and dashboard.html")

    def test_build_fraction_matches(self):
        js = js_rules()
        self.assertAlmostEqual(nums_after(js, "buildFractionOfDuration", 1)[0],
                               ops.BUILD_FRACTION)

    def test_red_thresholds_match(self):
        js = js_rules()
        seg = js[js.find("red:"):]
        seg = seg[:seg.find("}") + 1]
        found = {k: int(v) for k, v in re.findall(r"(\w+):\s*(\d+)", seg)}
        self.assertEqual(found["milestoneSlipDays"], ops.RED["milestone_slip_days"])
        self.assertEqual(found["blockerDays"], ops.RED["blocker_days"])
        self.assertEqual(found["missedCheckpoints"], ops.RED["missed_checkpoints"])
        self.assertEqual(found["invoiceOverdueDays"], ops.RED["invoice_overdue_days"])

    def test_amber_thresholds_match(self):
        js = js_rules()
        seg = js[js.find("amber:"):]
        seg = seg[:seg.find("}") + 1]
        found = {k: float(v) for k, v in re.findall(r"(\w+):\s*([\d.]+)", seg)}
        self.assertEqual(int(found["blockerDaysMin"]), ops.AMBER["blocker_min"])
        self.assertEqual(int(found["blockerDaysMax"]), ops.AMBER["blocker_max"])
        self.assertEqual(int(found["milestoneWithinDays"]), ops.AMBER["milestone_within"])
        self.assertAlmostEqual(found["budgetConsumed"], ops.AMBER["budget_consumed"])
        self.assertAlmostEqual(found["deliveredBelow"], ops.AMBER["delivered_below"])


class TestMarkdownAgrees(unittest.TestCase):
    """The markdown is the source of truth. Spot-check the load-bearing numbers
    actually appear in the documents that own them."""

    def read(self, rel):
        with open(os.path.join(OS_ROOT, rel)) as f:
            return f.read()

    def test_net_7_is_in_the_invoicing_policy(self):
        self.assertIn("Net 7", self.read("03-finance/invoicing-policy.md"))
        self.assertEqual(ledger.NET_DAYS, 7)

    def test_late_fee_is_in_the_invoicing_policy(self):
        self.assertIn("2% per month", self.read("03-finance/invoicing-policy.md"))
        self.assertEqual(ledger.LATE_FEE_MONTHLY, 0.02)
        self.assertEqual(ledger.LATE_FEE_AFTER_DAYS, 30)

    def test_chase_days_are_in_the_chase_sequence(self):
        t = self.read("03-finance/ar-chase-sequence.md")
        for day in [d for d, _, _, _ in ledger.CHASE_TIERS]:
            self.assertRegex(t, rf"\b{day}\b",
                             f"day {day} missing from ar-chase-sequence.md")

    def test_receipt_threshold_is_in_month_end_close(self):
        self.assertIn("$75", self.read("03-finance/month-end-close.md"))
        self.assertEqual(ledger.RECEIPT_REQUIRED_OVER, 75)

    def test_coverage_target_is_in_the_forecast_method(self):
        self.assertIn("3×", self.read("02-sales/forecast-method.md"))
        self.assertEqual(ops.COVERAGE_TARGET, 3)


class TestNoSendPath(unittest.TestCase):
    """'Nothing sends externally' and 'no money moves' are enforced by the
    capability not existing, not by remembering."""

    FORBIDDEN = re.compile(
        r"\b(smtplib|sendmail|send_email|requests\.post|urllib\.request\.urlopen"
        r"|stripe|paypal|ach_transfer|wire_transfer)\b")

    def test_no_module_can_send_or_pay(self):
        for name in ("ledger.py", "ops.py", "drafts.py", "sync_dashboard.py"):
            with open(os.path.join(LIB, name)) as f:
                src = f.read()
            # strip comments and docstrings so prose about "sending" is allowed
            src = re.sub(r'""".*?"""', "", src, flags=re.S)
            src = re.sub(r"#[^\n]*", "", src)
            m = self.FORBIDDEN.search(src)
            self.assertIsNone(m, f"{name} contains a send/pay capability: "
                                 f"{m.group(0) if m else ''}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
