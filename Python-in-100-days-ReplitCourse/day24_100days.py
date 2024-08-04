"""
Day 24 Challenge: PArameters in functions
Simple infinity dice rolling function
"""


def rollDice(sides):
  import random
  roll = random.randint(1, sides)
  return roll


while True:
  sides = int(input("How many sides?: "))
  roll = rollDice(sides)
  print("You rolled", roll)
  again = input("Roll again? ")
  if again == "yes":
    continue
  else:
    break

print("Thanks for playing!")
