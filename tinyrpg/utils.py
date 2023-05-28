import os
import json


def read_json(json_file: str) -> dict:
    json_path = os.path.join("data", json_file + ".json")
    if not os.path.exists(json_path):
        print(f"Reading JSON file: FILE NOT FOUND => {json_path}")
        return None
    with open(json_path, "r", encoding="utf-8") as json_f:
        return json.loads(json_f.read())
