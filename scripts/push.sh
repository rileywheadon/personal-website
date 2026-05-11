set -e -o pipefail

./scripts/whitespace.sh
./scripts/compile.sh
echo ""

jj bookmark set master
jj git push --remote=prod
jj git push --remote=origin
