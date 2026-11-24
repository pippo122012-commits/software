import csv
import json
import math

f = open("data/tiny.csv")
rows = list(csv.DictReader(f))
values = []

for row in rows:
    red = float(row["red"])
    nir = float(row["nir"])
    quality = int(row["quality"])
    if red + nir == 0:
        value = float("nan")
    else:
        value = (nir - red) / (nir + red)
    values.append(value)
    print(row["id"], value)

valid_values = []
for value in values:
    if math.isfinite(value):
        valid_values.append(value)

n = sum(value != 0 for value in valid_values)
mean = sum(valid_values) / len(valid_values)
print("total:", len(values), "valid:", n, "mean:", mean)

out = open("report.json", "w")
json.dump(
    {
        "n_total": len(values),
        "n_valid": sum(value != 0 for value in valid_values),
        "mean_ndvi": sum(valid_values) / len(valid_values),
    },
    out,
)
out.close()
