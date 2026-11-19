"""
The __init__() method initializes an object's attributes when it is created.
"""


class Car:
    
    company = "Google"  # Here company is the Class attribute
    def __init__(self, brand, color): # Here self refers to the current object
        self.brand = brand # Object's brand is an instance attribute
        self.color = color # Object's color is an instance attribute

    def display(self):
        print(self.brand, self.color)


car1 = Car("BMW", "Black")
car2 = Car("Audi", "White")

car1.display()
car2.display()


# When car1.display() runs, self refers to car1.

# When car2.display() runs, self refers to car2.


"""
You can think of:
car1.display() as approximately equivalent to:

Car.display(car1)

Important: self is not a Python keyword. It is a conventional parameter name.
"""


# Difference between Instance Attribute and Class Attribute

"""
+-----------------------------+-----------------------------+
| Instance Attribute          | Class Attribute             |
+-----------------------------+-----------------------------+
| Belongs to an object        | Belongs to the class        |
| Usually defined using self | Defined in the class body   |
| Can differ between objects | Shared by all objects       |
| Example: salary             | Example: company            |
+-----------------------------+-----------------------------+
"""