"""
Day 23 Challenge: Functions / Subroutines
Simple login system based function!
"""
def login():
  while True:
    username = input("Username: ")
    password = input("Password: ")
    if username == "user" and password == "password":
      print("Login successful! Welcome ", username)
      break
    else:
      print("Login failed! Recheck and login again with valid credientials")
      continue


print("Welcome to the login page")
print("Please enter your username and password")
login()
