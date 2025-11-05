#!/bin/bash

# Check if at least two arguments are provided
if [ $# -lt 2 ]; then
  echo "Usage: $0 <course_section> <script_name>"
  exit 1
fi

# Access the first and second arguments
course_section=$1
script_name=$2

rustc ./sections/${course_section}/${script_name}.rs && ./${script_name}
