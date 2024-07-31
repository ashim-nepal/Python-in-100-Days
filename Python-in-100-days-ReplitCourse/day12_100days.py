"""
Day 12 Challenge: Debugging
Try and fix this code which is full of errors
"""
"""
Given Code with errors:


print("100 Days of Code QUIZ")
print()
print("How many can you answer correctly?)
ans1 = ("What language are we writing in?")
if ans1 == "python":
  print("Correct")
else:
  print("Nope🙈
ans2 = input("Which lesson number is this?")
if(ans2>12):
print("We're not quite that far yet")
else:
  print("We've gone well past that!")
elif(ans2==12):
  print("That's right!")

  """

# Fixing the code
print("100 Days of Code QUIZ")
print()
print("How many can you answer correctly?")
ans1 = ("What language are we writing in?")
if ans1 == "python":
  print("Correct")
else:
  print("Nope🙈")

ans2 = int(input("Which lesson number is this?"))
if ans2 > 12:
  print("We're not quite that far yet")
elif ans2 == 12:
  print("That's right!")
else:
  print("We've gone well past that!")
