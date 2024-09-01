# Inheritance basics in python oops

class Animal:
  def __init__(self, name):
    self.name = name
    self.is_alive = True

  def eat(self):
    print(f"{self.name} is eating")
  
  def sleep(self):
    print(f"{self.name} is sleeping")

class Dog(Animal):
  def bark(self):
    print(f"{self.name} is barking")

class Cat(Animal):
  def meow(self):
    print(f"{self.name} is meowing")

dog = Dog("Doggy")
cat = Cat("Kitty")

dog.eat()
print(dog.is_alive)
dog.bark()

cat.sleep()
print(cat.is_alive)
cat.meow()


##### OUTPUT #####
""" 
Doggy is eating
True
Doggy is barking
Kitty is sleeping
True
Kitty is meowing

"""