#!/bin/bash
set -e -o pipefail

echo $'\nStarting compile.sh:'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATES_DIR="${SCRIPT_DIR}/../blog/templates"

if [[ ! -d "${TEMPLATES_DIR}" ]]; then
  echo "  Templates directory not found: ${TEMPLATES_DIR}"
  exit 1
fi

cd "${TEMPLATES_DIR}"

for dir in *; do
    if [ -d "$dir" ]; then
        echo "  Generating HTML for templates/$dir"
        pandoc -i "$dir/post.md" -o "$dir/post.html" > /dev/null 2>&1
    fi
done

echo "  All HTML files generated successfully!"
