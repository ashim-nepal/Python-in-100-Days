"""
Seventh Exercise:
Nested Conditions
"""

print("""
Have you ever watched Peaky Blinders? If yes then lets find out if you're really a fan or not!
""")
print("Just answer few questions!")
print()
pb = input('Who is the main character of Peaky Blinders?: ')
if pb == 'Thomas Shelby':
  print('Correct!')
  print()
  enemy = input('Who became the enemy of Thomas Shelby from family ?: ')
  if enemy == 'Michael Gray':
    print('Correct!')
    print()
    print('You are a true Peaky Blinders fan!')
  else:
    print('Wrong! You are not a Peaky Blinders fan!')
else:
  print('Mistake happens!')
  print()
  sis = input('What is the name of only Shelby Sister?: ')
  if sis == 'Ada Shelby':
    print('Correct!')
  else:
    print('Looks like you are really a fake fan!')
    print()

print('Thanks for playing! See you soon!')
