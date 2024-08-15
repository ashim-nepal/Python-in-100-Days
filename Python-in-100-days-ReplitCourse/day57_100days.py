"""
Day 57 Challenge: Recursion Technique in python

Factorial using Recursion technique
"""


def factorial(value):
  if value == 1:
    return 1
  else:
    return value * factorial(value - 1)


print(factorial(5))
