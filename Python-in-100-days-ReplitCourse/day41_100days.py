"""
Day 41 Challenge: Keys and Values dynamic use in Dictionary
Simple website storing with user input in dictionary
"""

website = {"name": None, "url": None, "desc": None, "rating": None}

for name in website.keys():
  website[name] = input(f"{name}: ")

print()
for name, value in website.items():
  print(f"{name}: {value}")
