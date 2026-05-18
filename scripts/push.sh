set -e -o pipefail

./scripts/whitespace.sh
./scripts/compile.sh
echo ""

echo "Running tests.."
python3 app.py &> /dev/null &
python3 tests/links.py
python3 tests/metadata.py
kill %
echo ""

jj bookmark set master > /dev/null 2>&1
jj git push --remote=origin > /dev/null 2>&1

echo "Building and pushing Docker image..."
docker build -t rileywheadon/personal-website:latest .
docker push rileywheadon/personal-website:latest
echo ""

# TODO: Replace this with something more robust
echo "Redeploying the application..."
cd ../personal-platform
./deploy.sh
