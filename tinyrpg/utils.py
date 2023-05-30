import os
import json

from .constants import Color


def read_json(json_file: str) -> dict:
    json_path = os.path.join("data", json_file + ".json")
    if not os.path.exists(json_path):
        print(f"Reading JSON file: FILE NOT FOUND => {json_path}")
        return None
    with open(json_path, "r", encoding="utf-8") as json_f:
        return json.loads(json_f.read())

def printformat(msg: str):
    for word in msg.split(' '):
        if word[0] == '|':
            print(Color.GREEN + word.strip('|') + Color.ENDC, end=" ")
        else:
            print(word, end=" ")
