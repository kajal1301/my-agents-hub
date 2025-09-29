import os, io, zipfile
from typing import List, Dict

def write_project(artifacts: List[Dict], base_dir: str) -> str:
    os.makedirs(base_dir, exist_ok=True)
    for a in artifacts:
        path = os.path.join(base_dir, a["path"])
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(a["content"])
    # also zip it
    zip_path = base_dir.rstrip("/")+ ".zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, _, files in os.walk(base_dir):
            for fn in files:
                full = os.path.join(root, fn)
                rel = os.path.relpath(full, base_dir)
                zf.write(full, rel)
    return zip_path

def memory_safe_get(d, key, default):
    try:
        return d.get(key, default)
    except Exception:
        return default
