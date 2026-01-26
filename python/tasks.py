#!/usr/bin/env python3
"""
Sample Python script for testing VSCode task runner
"""

import sys
import time

def hello():
    print("Hello from Python!")
    print(f"Python version: {sys.version}")

def long_running():
    print("Starting long running Python task...")
    for i in range(1, 11):
        print(f"Progress: {i}/10")
        time.sleep(1)
    print("Long running task completed!")

def failing():
    print("This Python script will fail...")
    print("Simulating an error condition")
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "hello":
            hello()
        elif command == "long-running":
            long_running()
        elif command == "failing":
            failing()
        else:
            print(f"Unknown command: {command}")
            print("Available commands: hello, long-running, failing")
            sys.exit(1)
    else:
        hello()
