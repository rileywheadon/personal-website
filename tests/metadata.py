from pathlib import Path

EXPECTED_KEYS = [
    "title",
    "created",
    "audience",
    "certainty",
    "importance",
    "status",
    "tags",
]

OPTIONAL_KEYS = [
    "math",
]

def check_metadata(file: str):
    lines = Path(file).read_text(encoding="utf-8").splitlines()
    keys = []

    for line in lines:
        if not line.strip():
            continue

        if ";" not in line:
            raise ValueError(f"Error: {file} has invalid line, missing ';': {line}")

        key = line.split(";", 1)[0].strip()
        if key not in OPTIONAL_KEYS:
            keys.append(key)

    if keys == EXPECTED_KEYS:
        return

    raise ValueError(f"Error: {file} has invalid metadata, missing or extra keys")

# Run validation on all matching files
for path in Path("blog/templates").glob("*/metadata.txt"):
    check_metadata(path)
