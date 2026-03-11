import json
import glob
from datetime import date
import os

def main():
    folder = "static/scholar/"
    files = glob.glob(folder + "*.json")

    all_publications = []
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            all_publications.extend(data['publications'])

    result = {
        "name": "MathExLab",
        "profile_url": "",
        "updated": str(date.today()),
        "publications": all_publications
    }

    os.makedirs("static/scholar", exist_ok=True)
    out_path = "static/scholar/all_publications.json"
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()