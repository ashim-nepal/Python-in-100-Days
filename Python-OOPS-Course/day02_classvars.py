# For Student Class
class Student:

  # Class variable
  class_year = 2024
  num_students = 0

  def __init__(self, name, age):
    # Instance variables
    self.name = name
    self.age = age
    Student.num_students += 1

st1 = Student("Dev", 14)
st2 = Student("Bis", 13)


print(st1.name)
print(st2.name)

print(st1.class_year) # instance variable printed
print(Student.class_year) # Class variable printed
print(Student.num_students)


########Output#########
""" 
Dev
Bis
2024
2024
2
"""