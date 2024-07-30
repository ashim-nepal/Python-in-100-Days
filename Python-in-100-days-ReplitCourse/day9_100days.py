"""
Day 9: Input data type casting
"""

print('''
Lets Find out which Generation are you from!
''')
year = int(input('What year were you born? '))
if year >= 1925 and year <= 1946:
  print('You are from Traditionalist Generation')
elif year >= 1947 and year <= 1964:
  print('You are from Baby Boomers Generation')
elif year >= 1965 and year <= 1981:
  print('You are from Generation X')
elif year >= 1982 and year <= 1995:
  print('You are from Millenials Generation')
elif year > 1996 and year <= 2015:
  print('You are from Generation Z')
elif year > 2015 and year <= 2024:
  print('You are from Generation Alpha')
else:
  print(
      '\nDont mess around with input if you really want to find out the generation, enter valid year. Thank You!'
  )
