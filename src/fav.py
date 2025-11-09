import csv
import os

# مسیر فایل CSV بر اساس محل اجرای فایل پایتون
csv_path = os.path.join(os.path.dirname(__file__), "fav.csv")

with open(csv_path, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    counts = {}

    for row in reader:
        fav2 = row["language"].strip()
        if fav2 in counts:
            counts[fav2] += 1
        else:
            counts[fav2] = 1

for fav2, count in counts.items():
    print(f"{fav2}: {count}")
