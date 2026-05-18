set -e -o pipefail

./scripts/whitespace.sh
./scripts/compile.sh

jj bookmark set master > /dev/null 2>&1
jj git push --remote=origin > /dev/null 2>&1

echo "\nBuilding and pushing Docker image..."
docker build -t rileywheadon/personal-website:latest .
docker push rileywheadon/personal-website:latest
