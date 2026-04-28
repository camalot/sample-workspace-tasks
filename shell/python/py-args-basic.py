#!/usr/bin/env python
"""
Basic argument types: string, int, float, required vs optional, default values.
"""
import argparse

parser = argparse.ArgumentParser(description="Demonstrates basic argument types.")

# Required string argument
parser.add_argument("--name", type=str, required=True, help="Your full name")

# Optional int argument with a default
parser.add_argument("--retries", type=int, default=3, help="Number of retries (default: 3)")

# Optional float argument
parser.add_argument("--threshold", type=float, default=0.75, help="Confidence threshold (default: 0.75)")

# Optional string argument without a default
parser.add_argument("--output", type=str, help="Output file path")

# String argument with a short form alias
parser.add_argument("-e", "--environment", type=str, default="development",
                    help="Target environment (default: development)")

args = parser.parse_args()

print(f"Name:        {args.name}")
print(f"Environment: {args.environment}")
print(f"Retries:     {args.retries}")
print(f"Threshold:   {args.threshold}")
print(f"Output:      {args.output or '(not set)'}")
