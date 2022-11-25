#!/bin/bash
 
# Check if Arduino is installed
if ! [ -x "$(command -v arduino)" ]; then
  echo 'Error: Arduino is not installed.' >&2
  exit 1
fi
 
echo 'Enter the path to the Arduino sketch: '
read sketch_path
 
# Compile and upload the Arduino sketch
arduino --upload $sketch_path
 
# Wait for 30 seconds
sleep 30
 
echo 'Enter the path to the Python script: '
read script_path
 
# Run the Python script
python $script_path
