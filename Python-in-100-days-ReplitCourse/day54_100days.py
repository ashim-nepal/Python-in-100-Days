"""
Day 54 Challenge: Working with csv files in python

Quantity * price, to get total from a csv file
"""

import csv

total = 0.0

with open("Day54Totals.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    total += float(row["Quantity"]) * float(row["Cost"])

print(f"Total: ${round(total,2)}")
