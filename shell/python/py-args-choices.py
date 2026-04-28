#!/usr/bin/env python
"""
Choices (fixed allowed values) and constrained arguments.
"""
import argparse

parser = argparse.ArgumentParser(description="Demonstrates choices and constrained arguments.")

# String choices
parser.add_argument("--environment", choices=["development", "staging", "production"],
                    required=True, help="Target deployment environment")

# String choices with a default
parser.add_argument("--config", choices=["Debug", "Release"], default="Release",
                    help="Build configuration (default: Release)")

# Int choices
parser.add_argument("--workers", type=int, choices=[1, 2, 4, 8], default=4,
                    help="Number of worker processes (default: 4)")

# Choices with a short alias
parser.add_argument("-l", "--log-level",
                    choices=["debug", "info", "warning", "error", "critical"],
                    default="info", help="Logging level (default: info)")

args = parser.parse_args()

print(f"Environment: {args.environment}")
print(f"Config:      {args.config}")
print(f"Workers:     {args.workers}")
print(f"Log level:   {args.log_level}")
