"""
Day 20 Challenge:
Simple List generator usng the range func and for loop
"""

startat = int(input("Enter the Starting value: "))
inc = int(input("Enter the Increment value: "))
endat = int(input("Enter the Ending value: ")) + inc # Prints upto 10 if user has provided 10 or 50 if provided 50 instead of python's explicit range

for i in range(startat, endat, inc):
  print("List No, ", i)