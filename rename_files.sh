#!/usr/bin/env bash

# Function to rename .sh files
rename_files() {
  for file in "$1"/*; do
    if [ -d "$file" ]; then
      # If the current file is a directory, call rename_files recursively
      rename_files "$file"
    elif [[ "$file" == *.sh ]]; then
      # If the file is a .sh file and contains "-", rename it
      new_name=$(echo "$file" | sed 's/-/_/g')
      if [ "$file" != "$new_name" ]; then
        mv "$file" "$new_name"
        echo "Renamed: $file -> $new_name"
      fi
    fi
  done
}

# Start renaming from the current directory or provided directory
start_dir=${1:-.}
rename_files "$start_dir"
