#!/bin/bash
set -e -o pipefail

echo $'\nRemoving trailing whitespace:'
git grep -I --name-only -z -e '' | xargs -0 sed -i 's/[ \t]\+$//'
echo "  Whitespace removed successfully!"

