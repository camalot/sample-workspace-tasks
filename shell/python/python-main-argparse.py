#!/usr/bin/env python

import argparse

def main():
    parser = argparse.ArgumentParser(description="Script Description")
    parser.add_argument("--name", type=str, help="Your name")
    parser.add_argument("--age", type=int, help="Your age")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("--hobbies", nargs='*', type=str, help="List of your hobbies")
    # argument with list of choices
    parser.add_argument("--color", choices=['red', 'green', 'blue'], help="Your favorite color")
    # argument with default value
    parser.add_argument("--country", type=str, default="USA", help="Your country of residence")

    args = parser.parse_args()
    print(f"Hello {args.name}, you are {args.age} years old.")
    if args.verbose:
        print("Verbose mode is enabled.")
    if args.hobbies:
        print(f"Your hobbies are: {', '.join(args.hobbies)}")
    if args.color:
        print(f"Your favorite color is {args.color}")
    print(f"You live in {args.country}.")

if __name__ == "__main__":
    main()
