"""
ABSTRACTION IN PYTHON
---------------------------------------

1. What is Abstraction?

Abstraction means hiding implementation details and exposing only essential functionality to the user.

In simple words:
Show WHAT an object does, rather than HOW it does it.

Real-world example: ATM Machine

When you withdraw money:

1. Insert your card.
2. Enter your PIN.
3. Enter the withdrawal amount.
4. Receive your cash.

You don't need to know:

1. How the bank verifies your account internally.
2. How the transaction is processed.
3. How the ATM communicates with the bank server.

The internal implementation is hidden.
You only interact with the necessary functionality.

That's abstraction!


2. How do we implement abstraction in Python?

Python provides the abc module.

abc stands for Abstract Base Class.

We mainly use two things:

ABC:
Defines an abstract base class.

@abstractmethod:
Defines a method that child classes must implement.
"""


"""
3. BASIC ABSTRACTION EXAMPLE
---------------------------------------
"""

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog barks")


class Cat(Animal):

    def sound(self):
        print("Cat meows")


d = Dog()
c = Cat()

d.sound()
c.sound()

# Output:
# Dog barks
# Cat meows

# Animal is an abstract class.
# Dog and Cat implement the abstract sound() method.


"""
4. WHAT HAPPENS IF WE DON'T IMPLEMENT ABSTRACT METHOD?
-----------------------------------------------------

A child class must implement all inherited abstract methods before it can be instantiated.
"""

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    pass


# d = Dog()

# Output:
# TypeError: Can't instantiate abstract class Dog with abstract method sound

# Why?
# Dog inherited an abstract method but did not implement it.
# Python prevents creating an object of Dog.


"""
5. CAN WE CREATE AN OBJECT OF AN ABSTRACT CLASS?
-----------------------------------------------------

No, not while it has unimplemented abstract methods.

A child class can implement all abstract methods and then be instantiated.
"""

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


# s = Shape()

# Output:
# TypeError: Can't instantiate abstract class Shape with abstract method area


class Rectangle(Shape):

    def area(self):
        return 10 * 20


r = Rectangle()

print("Area:", r.area())

# Output:
# Area: 200


"""
6. ABSTRACT CLASS WITH CONSTRUCTOR
---------------------------------------

An abstract class can have a constructor.

The child class can call the parent constructor using super().
"""

class Employee(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass


class Developer(Employee):

    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def calculate_salary(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


d = Developer("Ram", 50000)

d.calculate_salary()

# Output:
# Name: Ram
# Salary: 50000

# An abstract class can contain:
# 1. Constructor
# 2. Normal methods
# 3. Abstract methods
# 4. Attributes


"""
7. MULTIPLE ABSTRACT METHODS
---------------------------------------

An abstract class can contain multiple abstract methods.

The child class must implement all inherited abstract methods before it can be instantiated.
"""

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")


c = Car()

c.start()
c.stop()

# Output:
# Car started
# Car stopped


"""
8. ABSTRACT CLASS WITH NORMAL METHODS
---------------------------------------

An abstract class can contain both:

1. Abstract methods
2. Normal methods

Child classes must implement abstract methods, but they can directly use inherited normal methods.
"""

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("Animal is sleeping")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


d = Dog()

d.sound()
d.sleep()

# Output:
# Dog barks
# Animal is sleeping


"""
9. PRACTICAL EXAMPLE OF ABSTRACTION PAYMENT SYSTEM
-----------------------------------------------------

Different payment methods have different implementations.

However, all payment methods provide a common functionality: make_payment().
"""

class Payment(ABC):

    @abstractmethod
    def make_payment(self, amount):
        pass


class CreditCard(Payment):

    def make_payment(self, amount):
        print("Credit Card Payment:", amount)


class UPI(Payment):

    def make_payment(self, amount):
        print("UPI Payment:", amount)


class NetBanking(Payment):

    def make_payment(self, amount):
        print("Net Banking Payment:", amount)


p1 = CreditCard()
p2 = UPI()
p3 = NetBanking()

p1.make_payment(1000)
p2.make_payment(2000)
p3.make_payment(3000)

# Output:
# Credit Card Payment: 1000
# UPI Payment: 2000
# Net Banking Payment: 3000

# All payment classes provide make_payment().
# Each class has its own implementation.


"""
10. DIFFERENCE BETWEEN ABSTRACTION AND ENCAPSULATION
-----------------------------------------------------

+----------------------+---------------------------+
| Abstraction          | Encapsulation             |
+----------------------+---------------------------+
| Hides implementation | Controls access to data  |
| details              | and methods              |
| Focuses on WHAT      | Focuses on HOW data      |
| an object does       | is accessed or modified  |
| Uses ABC and         | Uses access conventions, |
| @abstractmethod      | properties, methods      |
| Example: ATM machine | Example: Bank balance    |
+----------------------+---------------------------+



11. IMPORTANT POINTS TO REMEMBER
---------------------------------------

1. Abstraction hides implementation details.
2. Abstraction exposes essential functionality.
3. Python provides the abc module.
4. ABC stands for Abstract Base Class.
5. @abstractmethod defines an abstract method.
6. An abstract class cannot be instantiated while it has unimplemented abstract methods.
7. Child classes must implement inherited abstract methods before they can be instantiated.
8. An abstract class can have constructors.
9. An abstract class can contain normal methods and abstract methods.
10. An abstract class can have multiple abstract methods.
11. A child class can call the parent constructor using super().




12. DIFFERENCE BETWEEN ABSTRACTION AND ENCAPSULATION
------------------------------------------------------

This is a very common Python interview question.

+---------------------------+---------------------------+
| Encapsulation             | Abstraction               |
+---------------------------+---------------------------+
| Combines data and         | Hides implementation     |
| methods inside a class    | details                  |
+---------------------------+---------------------------+
| Controls access to data   | Exposes essential         |
|                           | functionality             |
+---------------------------+---------------------------+
| Uses classes, properties  | Uses abstract classes    |
| and naming conventions    | and abstract methods     |
+---------------------------+---------------------------+
| Focuses on protecting     | Focuses on defining      |
| and managing state        | required behavior        |
+---------------------------+---------------------------+

Easy way to remember:

Encapsulation:
How do we control access to data?

Abstraction:
What should the user see, and what should remain hidden?

QUICK REVISION

Encapsulation = Data hiding and controlled access.

Abstraction = Implementation hiding and essential functionality.

Both concepts help create organized, maintainable and reusable code.
"""
