#!/bin/bash

# Loop through all PDF files in the current directory
for file in *.pdf; do
  # Skip if no files match
  [ -e "$file" ] || continue

  # Construct new name:
  # 1. Replace spaces with nothing
  # 2. Replace underscores with dashes
  # 3. Convert to lowercase (optional)

  newname=$(echo "$file" | tr ' ' '-' | tr '_' '-' | tr '[:upper:]' '[:lower:]')

  # Print the change
  echo "Renaming: $file → $newname"

  # Rename the file
  mv "$file" "$newname"
done
