import json
from pathlib import Path


def read_json_file(file_path: str):
    path = Path(file_path)

    if not path.exists():
        return {
            "error": True,
            "message": f"Fichier introuvable : {file_path}"
        }

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)