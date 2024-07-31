"""
Day 11: Simple seconds calculator for year and leap year
"""

days_count = int(input("How many days are in this year?"))

days_year = 365
days_leapyear = 366
hours_day = 24
minutes_hour = 60
seconds_minute = 60

seconds = days_year * hours_day * minutes_hour * seconds_minute

leapyear_seconds = days_leapyear * hours_day * minutes_hour * seconds_minute

if days_year == 366:
  print("Number of seconds in a leap year are", leapyear_seconds)
else:
  print("Number of seconds in a year are", seconds)
