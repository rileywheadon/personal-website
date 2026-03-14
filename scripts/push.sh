set -e -o pipefail

./scripts/whitespace.sh
./scripts/compile.sh
echo ""

jj git push
