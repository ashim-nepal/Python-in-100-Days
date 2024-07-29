'''
Day 4 Challenge
Color print and formatted print
'''

print("Uh, oh, you've been given a", "\033[31m", "warning", "\033[32m",
      "for being a bad - bad person.")

print('''
Welcome to your adventure simulator. I am going to ask you a bunch of questions and then create an epic story with you as the star!
''')

name = input('Enter your name: ')
enemy = input('Enter your worst enemy name: ')
superpower = input('What is your superpower: ')
address = input('Enter your address: ')
food = input('Enter your favourite food: ')

print(f'''
  Hello {name}! Your ability to {superpower} will make sure you never have to look at {enemy} again. Go eat {food} as you walk down the streets of {address} and use {superpower} for good and not evil!
''')
