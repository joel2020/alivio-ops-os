#!/bin/bash
# Installs the Alivio Operations OS launchd agents.
#
#   scheduler/install.sh            # write the plists, print what to run next
#   scheduler/install.sh --load     # write AND load them
#   scheduler/install.sh --unload   # stop and remove them
#
# Writing plists does nothing on its own. Nothing is scheduled until you load
# it, and --unload fully reverses this.
#
# Cadence, from 00-charter/cadence-calendar.md. Times are LOCAL — launchd's
# StartCalendarInterval uses local time, so there is no UTC conversion to get
# wrong.
#
#   monday-brief           Mon 07:00
#   invoice-chase-sweep    Tue + Fri 09:00     (twice weekly: tier boundaries
#                                               are days 1 and 7, and a weekly
#                                               sweep can miss one by six days)
#   project-status-rollup  Wed 09:00
#   pipeline-hygiene       Fri 15:00
#   friday-closeout        Fri 16:00
#   month-end-prep         25th 09:00

set -euo pipefail

OS_ROOT="$HOME/alivio-ops-os"
AGENTS="$HOME/Library/LaunchAgents"
RUNNER="$OS_ROOT/08-automation/scheduler/run-task.sh"
PREFIX="com.alivio.ops"

TASKS=(monday-brief invoice-chase-sweep project-status-rollup
       pipeline-hygiene friday-closeout month-end-prep)

if [ ! -x "$RUNNER" ]; then
  echo "runner is not executable: $RUNNER"
  echo "  chmod +x $RUNNER"
  exit 1
fi

if [ "${1:-}" = "--unload" ]; then
  for t in "${TASKS[@]}"; do
    plist="$AGENTS/$PREFIX.$t.plist"
    launchctl unload "$plist" 2>/dev/null || true
    rm -f "$plist"
    echo "removed $t"
  done
  echo
  echo "All Alivio agents removed. Nothing is scheduled."
  exit 0
fi

mkdir -p "$AGENTS" "$OS_ROOT/08-automation/runs"

write_plist() {
  local task="$1" cmd="$2" schedule="$3"
  local plist="$AGENTS/$PREFIX.$task.plist"
  cat >"$plist" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>$PREFIX.$task</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/bash</string>
    <string>$RUNNER</string>
    <string>$task</string>
    <string>$cmd</string>
  </array>
$schedule
  <key>WorkingDirectory</key><string>$OS_ROOT</string>
  <key>StandardOutPath</key><string>$OS_ROOT/08-automation/runs/launchd-$task.out</string>
  <key>StandardErrorPath</key><string>$OS_ROOT/08-automation/runs/launchd-$task.err</string>
  <key>ProcessType</key><string>Background</string>
  <key>LowPriorityIO</key><true/>
  <key>Nice</key><integer>5</integer>
</dict>
</plist>
PLIST
  echo "wrote $plist"
}

# launchd Weekday: 0=Sun 1=Mon ... 5=Fri
write_plist monday-brief /monday-brief "$(cat <<'X'
  <key>StartCalendarInterval</key>
  <dict><key>Weekday</key><integer>1</integer><key>Hour</key><integer>7</integer><key>Minute</key><integer>0</integer></dict>
X
)"

write_plist invoice-chase-sweep /invoice-chase-sweep "$(cat <<'X'
  <key>StartCalendarInterval</key>
  <array>
    <dict><key>Weekday</key><integer>2</integer><key>Hour</key><integer>9</integer><key>Minute</key><integer>0</integer></dict>
    <dict><key>Weekday</key><integer>5</integer><key>Hour</key><integer>9</integer><key>Minute</key><integer>0</integer></dict>
  </array>
X
)"

write_plist project-status-rollup /project-status-rollup "$(cat <<'X'
  <key>StartCalendarInterval</key>
  <dict><key>Weekday</key><integer>3</integer><key>Hour</key><integer>9</integer><key>Minute</key><integer>0</integer></dict>
X
)"

write_plist pipeline-hygiene /pipeline-hygiene "$(cat <<'X'
  <key>StartCalendarInterval</key>
  <dict><key>Weekday</key><integer>5</integer><key>Hour</key><integer>15</integer><key>Minute</key><integer>0</integer></dict>
X
)"

write_plist friday-closeout /friday-closeout "$(cat <<'X'
  <key>StartCalendarInterval</key>
  <dict><key>Weekday</key><integer>5</integer><key>Hour</key><integer>16</integer><key>Minute</key><integer>0</integer></dict>
X
)"

write_plist month-end-prep /month-end-prep "$(cat <<'X'
  <key>StartCalendarInterval</key>
  <dict><key>Day</key><integer>25</integer><key>Hour</key><integer>9</integer><key>Minute</key><integer>0</integer></dict>
X
)"

echo
if [ "${1:-}" = "--load" ]; then
  for t in "${TASKS[@]}"; do
    plist="$AGENTS/$PREFIX.$t.plist"
    launchctl unload "$plist" 2>/dev/null || true
    launchctl load "$plist"
    echo "loaded $t"
  done
  echo
  echo "Scheduled. Check with:"
  echo "  launchctl list | grep $PREFIX"
  echo "  tail -5 $OS_ROOT/08-automation/runs/run-log.jsonl"
else
  echo "Plists written but NOT loaded. Nothing is scheduled yet."
  echo
  echo "To start:            scheduler/install.sh --load"
  echo "To test one now:     08-automation/scheduler/run-task.sh monday-brief /monday-brief"
  echo "To remove:           scheduler/install.sh --unload"
fi

echo
echo "Note: launchd does not run agents while the Mac is asleep. A missed"
echo "StartCalendarInterval fires once on wake."
