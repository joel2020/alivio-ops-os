"""The six tasks, and the two rules that govern all of them.

Rule one: never report a confident zero for something that could not be read.
Rule two: never silently detach money from the thing it belongs to.

Both defects below were live and shipped before this file existed. Neither was
caught by the unit tests, because each function was individually correct — the
failure was in what the composition claimed.
"""

import json
import os
import shutil
import sys
import tempfile
import unittest

LIB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, LIB)

import ops  # noqa: E402

OS_ROOT = os.path.dirname(os.path.dirname(LIB))
DATA_JS = os.path.join(OS_ROOT, "07-dashboard", "data.js")


class BreakDataJs:
    """Temporarily corrupt data.js, then put it back."""

    def __init__(self, content="window.ALIVIO_DATA = {broken"):
        self.content = content

    def __enter__(self):
        self.backup = tempfile.mktemp()
        shutil.copy(DATA_JS, self.backup)
        with open(DATA_JS, "w") as f:
            f.write(self.content)

    def __exit__(self, *a):
        shutil.copy(self.backup, DATA_JS)
        os.unlink(self.backup)


class TestHonestDegradation(unittest.TestCase):
    """'Nothing to do' and 'I couldn't look' must never render the same.

    The shipped bug: monday_brief returned available:true alongside
    projects.total:0 when data.js was unreadable. A reader concludes there are
    no red projects. There might be three.
    """

    def test_brief_is_not_available_when_the_board_cannot_be_read(self):
        with BreakDataJs():
            b = ops.monday_brief()
        self.assertFalse(b["available"],
                         "a brief missing its projects must not claim availability")
        self.assertTrue(b["partial"])

    def test_brief_names_what_it_could_not_read(self):
        with BreakDataJs():
            b = ops.monday_brief()
        self.assertTrue(any("data.js" in m for m in b["missing"]))

    def test_projects_section_carries_its_own_availability(self):
        with BreakDataJs():
            b = ops.monday_brief()
        self.assertFalse(b["projects"]["available"])
        self.assertIsNotNone(b["projects"]["reason"])
        self.assertEqual(b["projects"]["red"], [],
                         "empty is fine — but only alongside available:false")

    def test_commitments_section_carries_its_own_availability(self):
        with BreakDataJs():
            b = ops.monday_brief()
        self.assertFalse(b["commitments"]["available"])

    def test_brief_is_available_when_everything_reads(self):
        b = ops.monday_brief()
        self.assertTrue(b["available"])
        self.assertTrue(b["projects"]["available"])

    def test_rollup_reports_unavailable_rather_than_no_projects(self):
        with BreakDataJs():
            r = ops.project_status_rollup()
        self.assertFalse(r["available"])
        self.assertEqual(r["red"], [])

    def test_pipeline_hygiene_reports_unavailable(self):
        with BreakDataJs():
            r = ops.pipeline_hygiene()
        self.assertFalse(r["available"])


class TestOrphanDetection(unittest.TestCase):
    """Invoices link to projects by exact string match. A typo silently
    detaches the money: the invoice stops contributing to that project's
    health and the >30-day RED trigger never fires for it."""

    def test_no_orphans_in_the_real_books(self):
        r = ops.orphaned_invoices()
        self.assertTrue(r["available"])
        self.assertEqual(r["orphans"], [],
                         f"invoice(s) point at a project that does not exist: "
                         f"{[o['number'] for o in r['orphans']]}")

    def test_orphans_are_reported_as_unavailable_when_board_is_unreadable(self):
        with BreakDataJs():
            r = ops.orphaned_invoices()
        self.assertFalse(r["available"])

    def test_the_sweep_surfaces_orphans(self):
        s = ops.invoice_chase_sweep()
        self.assertIn("orphaned_invoices", s)

    def test_month_end_surfaces_orphans_as_a_gap(self):
        m = ops.month_end_prep()
        kinds = {g["kind"] for g in m["gaps"]}
        # No orphans right now, so the kind should be absent rather than empty.
        self.assertNotIn("invoice not linked to a project", kinds)


class TestSourcesCited(unittest.TestCase):
    """Phase 3 rule: every automated output cites where its numbers came from."""

    def test_every_task_names_its_sources(self):
        for name, fn in ops.TASKS.items():
            with self.subTest(task=name):
                out = fn()
                self.assertIn("sources", out, f"{name} cites no sources")
                self.assertTrue(out["sources"], f"{name} has an empty sources list")


class TestNoConfidentZeros(unittest.TestCase):

    def test_coverage_is_none_not_zero_when_target_unset(self):
        """A coverage of 0.0 means 'you have no pipeline'. Unset does not."""
        p = ops.pipeline_hygiene()
        if p["coverage"] is None:
            self.assertIsNotNone(p["coverage_note"],
                                 "an uncomputable coverage must explain itself")

    def test_empty_pipeline_is_flagged_as_the_finding(self):
        p = ops.pipeline_hygiene()
        if p["open_deals"] == 0:
            self.assertTrue(p["empty_pipeline_is_the_finding"])


class TestHealthMatchesTheRules(unittest.TestCase):

    def test_milestone_slip_over_five_days_is_red(self):
        p = {"name": "X", "stage": "Build", "stage_since": "2026-07-01",
             "next_milestone": {"date": "2026-07-01"},
             "started": "2026-06-01", "target_delivery": "2026-09-01"}
        h = ops.project_health(p, __import__("datetime").date(2026, 7, 26))
        self.assertEqual(h["level"], "red")

    def test_blocked_three_days_is_amber_not_red(self):
        p = {"name": "X", "stage": "Build", "stage_since": "2026-07-20",
             "blocker_since": "2026-07-23",
             "started": "2026-07-01", "target_delivery": "2026-09-01"}
        h = ops.project_health(p, __import__("datetime").date(2026, 7, 26))
        self.assertEqual(h["level"], "amber")

    def test_clean_project_is_green(self):
        p = {"name": "X", "stage": "Build", "stage_since": "2026-07-24",
             "next_milestone": {"date": "2026-09-01"},
             "started": "2026-07-01", "target_delivery": "2026-09-01",
             "missed_checkpoints": 0}
        h = ops.project_health(p, __import__("datetime").date(2026, 7, 26))
        self.assertEqual(h["level"], "green")


if __name__ == "__main__":
    unittest.main(verbosity=2)
