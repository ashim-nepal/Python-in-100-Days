"""
Day 8: Simple Affirmation
"""
print("Hello. Welcome to your daily affirmation generator.")
name = input("Enter your name: ")

if name == "David" or name == "david":
   DOW = input("What is the day of the week?: ")
   if DOW == "monday" or DOW == "Monday":
      print("It is going to be a great Monday", name)
   if DOW == "tuesday" or DOW == "Tuesday":
      print("What a wonderful Tuesday it is", name)
   if DOW == "wednesday" or DOW == "Wednesday":
      print("Happy Hump Day", name)
   if DOW == "thursday" or DOW == "Thursday":
      print(name, "your week is almost over!")
   if DOW == "friday" or DOW == "Friday":
      print(name, "It's FRIDAY!")

elif name == "Lana" or name == "lana":
   DOW = input("What is the day of the week? ")
   if DOW == "monday" or DOW == "Monday":
      print("It is going to be a great Monday", name)
   if DOW == "tuesday" or DOW == "Tuesday":
      print("You look great in that color", name)
   if DOW == "wednesday" or DOW == "Wednesday":
      print("You look chipper today", name)
   if DOW == "thursday" or DOW == "Thursday":
      print(name, "you are doing a great job!")
   if DOW == "friday" or DOW == "Friday":
      print(name, "it's FRIDAY!")
else:
   print("Your entry is not available, Sorry for inconvenience", name,"!:(")
