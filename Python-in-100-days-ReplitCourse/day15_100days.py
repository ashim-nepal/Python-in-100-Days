"""
Day 15 Challenge: Loop! While Loop
"""

exit = ""

while exit == "":
  animal_sound = input("What animal sound do you want to hear?")

  if animal_sound == "cow" or animal_sound == "Cow":
    print("🐮 Moo")
  elif animal_sound == "pig" or animal_sound == "Pig":
    print("🐷 Oink")
  elif animal_sound == "sheep" or animal_sound == "Sheep":
    print("🐑 Baaa")
  elif animal_sound == "duck" or animal_sound == "Duck":
    print("🦆 Quack")
  elif animal_sound == "dog" or animal_sound == "Dog":
    print("🐶 Woof")
  elif animal_sound == "cat" or animal_sound == "Cat":
    print("🐱 Meow")
  else:
    print("This animal sound is not in my data. Please Try Again.")

  exit = input("Do you want to exit?(Type any key and enter to exit): ")
  print()
