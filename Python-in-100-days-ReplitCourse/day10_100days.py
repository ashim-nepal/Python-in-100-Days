"""
Day 10 Challenge:
Bill Tip adding and Splitting
"""

totalBill = float(input("What is the total bill?: "))
tip = float(input("How many percentage of tipe you wanna leave?: "))
finalBill = totalBill + (totalBill * (tip / 100))
people = int(input("How many people are splitting the bill?: "))
answer = finalBill / people
answer = round(answer, 2)
print("You all owe", answer)
