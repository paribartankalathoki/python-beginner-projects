"""
Python has three commonly used method types.

1. Instance methods
2. Class methods
3. Static methods
"""


# 1. Instance Method:
# An instance method works with an object's data.
# It uses self as its first parameter.

class Employee:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


e1 = Employee("Ram")
e2 = Employee("Hari")

e1.display()
e2.display()



# 2. Class Method:
# A class method works with class-level data.
# It uses the @classmethod decorator and cls parameter.

class Company:

    company = "Google"

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


Company.change_company("Microsoft")

print(Company.company)


# Here, cls refers to the class itself, not an individual object.
# Class methods can access and modify class-level attributes.


# 3. Static Method:
# A static method does not require self or cls.
# It is useful for utility functions logically related to a class.

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b


result = Calculator.add(10, 20)

print(result)



# Difference between Instance Method, Class Method, and Static Method

"""
+-------------------------+-------------------------+-------------------------+
| Instance Method         | Class Method            | Static Method           |
+-------------------------+-------------------------+-------------------------+
| Decorator: None         | @classmethod             | @staticmethod           |
| First parameter: self   | First parameter: cls     | No required parameter   |
| Access instance data:   | Access instance data:   | Access instance data:   |
| Yes                     | No, not directly        | No, not directly        |
| Access class data:      | Access class data:      | Access class data:      |
| Yes                     | Yes                     | Yes, through class name |
| Called using:           | Called using:           | Called using:           |
| Object or class         | Object or class         | Object or class         |
+-------------------------+-------------------------+-------------------------+
"""


# One important thing to remember:

# self → Refers to the current object.

# cls → Refers to the current class.

# Static method → Doesn't automatically receive self or cls.