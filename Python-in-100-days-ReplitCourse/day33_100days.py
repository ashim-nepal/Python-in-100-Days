"""
Day 33 Challange: Using List Dynamically in Python

Manipulating list dynamically performing crud in python list from terminal!
"""

import os, time

toDoList = []


def printList():
  print()
  for item in toDoList:
    print(item)
  print()


while True:
  menu = input(
      "ToDoList Manager\n\nDo you want to view, add or edit the todo list?\n")
  if menu == "view":
    printList()
  elif menu == "add":
    item = input("What do you want to add?\n")
    toDoList.append(item)
  elif menu == "edit":
    item = input("What do you want to remove?\n")
    if item in toDoList:
      toDoList.remove(item)
    else:
      print(f"{item} is not in the list")
      printList()
