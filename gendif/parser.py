import json
import yaml
import os


def parse_file(file_path):
    _, ext = os.path.splitext(file_path)

    if ext == '.json':
        with open(file_path, 'r') as file:
            return json.load(file)
    elif ext == '.yaml':
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    else:
        raise ValueError("Invalid file format.")
