#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="${SCRIPT_DIR}/.."
README_FILE="${REPO_ROOT}/README.md"

# Create or overwrite the README.md file with the header
cat > "$README_FILE" << 'EOL'
# Books And Courses

Random learnings from multiple resources.

## Table of content (auto-generated):
EOL

# Add Books section
echo -e "\n### Books" >> "$README_FILE"
find "${REPO_ROOT}/books" -maxdepth 1 -mindepth 1 -type d -exec basename {} \; | sort | while read -r book; do
  # Replace hyphens with spaces and capitalize each word for display
  display_name=$(echo "$book" | sed 's/-/ /g' | awk '{for(i=1;i<=NF;i++){ $i=toupper(substr($i,1,1)) tolower(substr($i,2)) }}1')
  echo "- [${display_name}](./books/${book})" >> "$README_FILE"
done

# Add Courses section
echo -e "\n### Courses" >> "$README_FILE"
find "${REPO_ROOT}/courses" -maxdepth 1 -mindepth 1 -type d -exec basename {} \; | sort | while read -r course; do
  # Replace hyphens with spaces and capitalize each word for display
  display_name=$(echo "$course" | sed 's/-/ /g' | awk '{for(i=1;i<=NF;i++){ $i=toupper(substr($i,1,1)) tolower(substr($i,2)) }}1')
  echo "- [${display_name}](./courses/${course})" >> "$README_FILE"
done

echo -e "\n" >> "$README_FILE"
echo "README.md has been generated successfully at $README_FILE"