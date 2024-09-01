# OOP in short in python programming language

from day01_car import Car
car1 = Car("Mustang", 2022, "Red", True)

print(car1.model)
print(car1.color)
print(car1.year)
print(car1.for_sale)


car1.drive()
car1.stopped()
car1.describe()


##### OUTPUT #####
""" 
Mustang
Red
2022
True
Mustang is being Drived
Mustang has been stopped
2022 Mustang Red

"""