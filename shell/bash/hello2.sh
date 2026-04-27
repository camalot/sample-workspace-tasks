#!/bin/bash
# Simple hello world script

echo "Hello from shell script!"
echo "Current directory: $(pwd)"
echo "Current user: $(whoami)"

for arg in "$@"; do
    echo "Arg: $arg"
done
