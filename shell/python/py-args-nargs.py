#!/usr/bin/env python
"""
Multi-value arguments using nargs: '?', '*', '+', and an exact integer count.
"""
import argparse

parser = argparse.ArgumentParser(description="Demonstrates multi-value nargs arguments.")

# nargs='?' — zero or one value; uses default when flag is absent, const when flag is present alone
parser.add_argument("--output", nargs="?", const="stdout", default=None,
                    help="Output destination (omit for none, bare flag for stdout, or a file path)")

# nargs='*' — zero or more values into a list
parser.add_argument("--hobbies", nargs="*", type=str,
                    help="List of hobbies (zero or more)")

# nargs='+' — one or more values into a list; error if none provided
parser.add_argument("--files", nargs="+", required=True,
                    help="One or more input files to process")

# nargs=N — exactly N values gathered into a list
parser.add_argument("--range", nargs=2, type=int, metavar=("MIN", "MAX"),
                    help="Numeric range as two integers: MIN MAX")

args = parser.parse_args()

print(f"Output:  {args.output!r}")
print(f"Hobbies: {args.hobbies}")
print(f"Files:   {args.files}")
print(f"Range:   {args.range}")
