#!/usr/bin/env bash
# stuck.sh – ignores SIGINT (Ctrl+C) and SIGTERM.
# Only a SIGKILL (kill -9) or closing the terminal will stop this process.

trap '' INT TERM

echo "Process $$ is running. Ctrl+C and SIGTERM are ignored."
echo "Kill the terminal or run: kill -9 $$"

while true; do
  echo "Still running... ($(date '+%H:%M:%S'))"
  sleep 2
done
