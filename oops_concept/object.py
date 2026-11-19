"""
An object is an instance of a class.
"""


class Car:
    pass

car1 = Car()
car2 = Car()

print(car1)
print(car2)

# Here, car1 and car2 are two different objects created from the same class.



# Adding attributes to objects
# Attributes are variables that belong to objects.

car1 = Car()

car1.brand = "BMW"
car1.color = "Black"
car1.year = 2025

print(car1.brand)
print(car1.color)
print(car1.year)


# Here we added attributes directly to the object.

# However, there is a better way to initialize object attributes using __init__() method in python