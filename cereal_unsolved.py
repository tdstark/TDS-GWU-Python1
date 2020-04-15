import os
import csv

cereal_csv = os.path.join("../Resources", "cereal.csv")
with open(cereal_csv, 'r') as csvfile:
    cereals = csv.reader(csvfile)
    next(cereals, None)
    for x in cereals:
        if float(x[7]) >= 5:
            print(x)


