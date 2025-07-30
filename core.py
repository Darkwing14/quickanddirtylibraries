# core.py
import os
import json

def stat(code):
    return {"status": code}  # Placeholder definition

def save(base_path, filename, data):
    path = os.path.join(base_path, filename)
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    return stat(6)

def load(base_path, filename):
    path = os.path.join(base_path, filename)
    if not os.path.exists(path):
        return stat(1)
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return stat(2)

def delete(base_path, filename):
    path = os.path.join(base_path, filename)
    if os.path.exists(path):
        os.remove(path)
        return stat(6)
    else:
        return stat(1)
