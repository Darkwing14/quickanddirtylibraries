import os
import json

def save(base_path, filename, data):
    path = os.path.join(base_path, filename)
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def load(base_path, filename):
    path = os.path.join(base_path, filename)
    if not os.path.exists(path):
        return None
    with open(path, 'r') as f:
        return json.load(f)

def delete(base_path, filename):
    path = os.path.join(base_path, filename)
    if os.path.exists(path):
        os.remove(path)
    else:
        raise FileNotFoundError(f"File '{filename}' not found in '{base_path}'")
