import os
import sys
import json
from pathlib import Path
from jsonschema import Draft202012Validator

schema_path = Path(".schema/conference-schema.json")
with schema_path.open("r", encoding="utf-8") as f:
    schema = json.load(f)
validator = Draft202012Validator(schema)

changed = os.environ.get("CHANGED_JSON", "").strip()
if not changed:
    print("No changed JSON files to validate.")
    sys.exit(0)

failed = False
for path_str in changed.split():
    p = Path(path_str)
    if not p.is_file():
        continue
    print(f"\nValidating {p} ...")
    try:
        with p.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"\033[31m[error]\033[0m JSON parse error: {e}")
        failed = True
        continue

    errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
    if errors:
        failed = True
        print("\033[31m[error]\033[0m Schema check failed:")
        for err in errors:
            loc = "/".join(str(x) for x in err.path) or "(root)"
            print(f"    - {loc}: {err.message}")
    else:
        print("\033[32m[success]\033[0m JSON Schema check passed!")

sys.exit(1 if failed else 0)