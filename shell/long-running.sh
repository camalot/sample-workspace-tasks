#!/bin/bash
# Long running shell script

echo "Starting long running shell script..."
for i in {1..10}; do
    echo "Progress: $i/10"
    sleep 1
done
echo "Long running script completed!"
