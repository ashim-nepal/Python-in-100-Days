'''
Day 6 Challenge:
Elif Statements
'''

print("Secure Login\n")
username = input("Enter username: ")
password = input("Enter password: ")

if username == "Max" and password == "MaxDMax":
  print("Welcome, Max! You are looking nice today!")

elif username == "Rocky" and password == "Rock0n":
  print("Hi Becky! Love your hair today!")

elif username == "Sam" and password == "54mmy!!":
  print("Hello Sam! What up?!")
else:
  print("You do not have access. Please contact administrator!")
