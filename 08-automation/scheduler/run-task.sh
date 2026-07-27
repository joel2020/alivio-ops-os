#!/bin/bash
# Runs one Alivio scheduled task headlessly under launchd.
#
#   scheduler/run-task.sh <task-name> <slash-command>
#   scheduler/run-task.sh monday-brief /monday-brief
#
# launchd provides almost no environment, so PATH is set explicitly.
#
# Always exits 0. A failed task is recorded in the run log; letting launchd see
# a non-zero exit makes it retry blindly, which is worse than recording the
# failure and waiting for the next slot.

set -uo pipefail

TASK="${1:?usage: run-task.sh <task> <slash-command>}"
CMD="${2:?usage: run-task.sh <task> <slash-command>}"

OS_ROOT="$HOME/alivio-ops-os"
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

LOGDIR="$OS_ROOT/08-automation/runs"
mkdir -p "$LOGDIR"
LOG="$LOGDIR/${TASK}-$(date +%Y-%m-%d).log"
RUNLOG="$LOGDIR/run-log.jsonl"

cd "$OS_ROOT" || exit 0

START=$(date +%s)
echo "=== $(date -Iseconds) $TASK ($CMD) ===" >>"$LOG"

# The engine runs regardless of whether Claude is available. That matters: the
# numbers are the point, and a missing CLI must not mean a missing sweep.
ENGINE_OK=0
if /usr/bin/python3 "$OS_ROOT/08-automation/lib/ops.py" "$TASK" >>"$LOG" 2>&1; then
  ENGINE_OK=1
else
  echo "engine failed for $TASK" >>"$LOG"
fi

CLAUDE_OK=0
BLOCKED=0
NOTE=""
if command -v claude >/dev/null 2>&1; then
  MARK=$(wc -c <"$LOG" | tr -d ' ')       # where this session's output starts
  # --max-turns bounds a runaway session. Scheduled work is short by design.
  if claude -p "$CMD" --max-turns 30 >>"$LOG" 2>&1; then CLAUDE_OK=1; fi

  # `claude -p` exits 0 for a session in which everything was denied. On
  # 2026-07-27 every one of these six tasks reported success while the
  # workspace was untrusted, so all ten permissions.allow entries were ignored
  # and the commands never ran. Trusting the exit code makes the run log a
  # record of nothing.
  if tail -c "+$MARK" "$LOG" | grep -qiE \
      "has not been trusted|Ignoring [0-9]+ permissions\.allow|permission denied|requires approval"; then
    BLOCKED=1
    CLAUDE_OK=0
    NOTE="permission-blocked: the workspace is untrusted or the command is not allowed"
    echo "=== PERMISSION BLOCKED — see the note above ===" >>"$LOG"
  fi
else
  echo "claude CLI not on PATH — engine output above is the whole result" >>"$LOG"
fi

END=$(date +%s)
printf '{"ts":"%s","task":"%s","engine_ok":%s,"claude_ok":%s,"blocked":%s,"note":"%s","duration_s":%s}\n' \
  "$(date -Iseconds)" "$TASK" "$ENGINE_OK" "$CLAUDE_OK" "$BLOCKED" "$NOTE" "$((END - START))" >>"$RUNLOG"

echo "=== engine_ok=$ENGINE_OK claude_ok=$CLAUDE_OK blocked=$BLOCKED ===" >>"$LOG"

# Keep the log directory bounded.
find "$LOGDIR" -name '*.log' -mtime +30 -delete 2>/dev/null

exit 0
