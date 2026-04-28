#!/usr/bin/env python
"""
Boolean flags using action='store_true' and action='store_false'.
"""
import argparse

parser = argparse.ArgumentParser(description="Demonstrates boolean flag arguments.")

# store_true: flag is False by default; passing --verbose sets it to True
parser.add_argument("--verbose", action="store_true",
                    help="Enable verbose output")

# store_false: flag is True by default; passing --no-cache sets it to False
parser.add_argument("--no-cache", action="store_false", dest="cache",
                    help="Disable caching")

# store_true with a short alias
parser.add_argument("-d", "--dry-run", action="store_true",
                    help="Simulate execution without making changes")

args = parser.parse_args()

print(f"Verbose:  {args.verbose}")
print(f"Cache:    {args.cache}")
print(f"Dry run:  {args.dry_run}")

if args.dry_run:
    print("[DRY RUN] No changes were made.")
if args.verbose:
    print("[VERBOSE] Detailed output enabled.")
if not args.cache:
    print("[INFO] Cache is disabled.")
