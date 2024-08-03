"""
Day 19 Challenge:
Simple loan calculator for next n years 
"""

loan = float(input("Enter the loan Amount: ")) # Loan amt
apr = float(input("Enter the loan Annual Percentage of rate: ")) # Annual percentage rate
yrs = int(input("Enter the years to borrow loan: "))
for i in range(10):
  loan+=(loan*apr)
  print("Year", i+1, "is", round(loan,2))
