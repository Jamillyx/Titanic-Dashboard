import csv
import json

CSV_PATH = "static/data/titanic.csv"
JSON_PATH = "data.json"

fixture = []

with open(CSV_PATH, newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Monta cada item no formato Django fixture
        fixture.append(
            {
                "model": "dashboard.titanicpassenger",
                "fields": {
                    "name": row["Name"],
                    "age": float(row["Age"]) if row["Age"] else None,
                    "sex": row["Sex"],
                    "fare": float(row["Fare"]) if row["Fare"] else None,
                    "survived": bool(int(row["Survived"])),
                    "embarked": row["Embarked"] or None,
                    "pclass": int(row["Pclass"]),
                },
            }
        )

with open(JSON_PATH, "w", encoding="utf-8") as jsonfile:
    json.dump(fixture, jsonfile, ensure_ascii=False, indent=4)

print(f"Fixture gerado em: {JSON_PATH}")
