#!/usr/bin/env python
"""
Accumulating arguments using action='append', action='extend', and action='count'.
"""
import argparse

parser = argparse.ArgumentParser(description="Demonstrates accumulating action arguments.")

# action='append' — flag may be supplied multiple times; each value is appended to a list
#   Usage: --tag backend --tag api --tag v2
parser.add_argument("--tag", action="append", dest="tags",
                    help="Tag to attach (may be repeated)")

# action='extend' with nargs='+' — each occurrence extends the list with multiple values
#   Usage: --include src tests --include docs
parser.add_argument("--include", action="extend", nargs="+",
                    help="Paths to include (may be repeated with multiple values each time)")

# action='count' — counts how many times the flag appears; -v=1, -vv=2, -vvv=3
#   Usage: -v  or  -vvv  or  --verbose --verbose
parser.add_argument("-v", "--verbose", action="count", default=0,
                    help="Increase verbosity level (repeat for more detail: -v, -vv, -vvv)")

args = parser.parse_args()

print(f"Tags:      {args.tags or []}")
print(f"Include:   {args.include or []}")
print(f"Verbosity: {args.verbose}")

if args.verbose >= 3:
    print("[DEBUG] Maximum verbosity.")
elif args.verbose == 2:
    print("[INFO] High verbosity.")
elif args.verbose == 1:
    print("[INFO] Standard verbosity.")
