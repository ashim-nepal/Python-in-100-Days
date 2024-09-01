# Car Class
class Car:
  def __init__(self, model, year, color, for_sale):
    self.model = model
    self.year = year
    self.color = color
    self.for_sale = for_sale

  # Methods

  def drive(self):
    print(f"{self.model} is being Drived")
  
  def stopped(self):
    print(f"{self.model} has been stopped")

  def describe(self):
    print(f"{self.year} {self.model} {self.color}")