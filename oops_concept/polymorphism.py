"""
POLYMORPHISM IN PYTHON
------------------------------------------------------------

1. What is Polymorphism?

Polymorphism means one name, multiple forms or behaviors.

In Python, the same method or operation can behave
differently depending on the object or data type.

Example:

A sound() method can behave differently for Dog and Cat.

Dog  -> Bark
Cat  -> Meow

Benefits of polymorphism:

1. Code reusability
2. Flexibility
3. Easy maintenance
4. Common interface for different objects
"""


"""
2. METHOD OVERRIDING
------------------------------------------------------------

Method overriding occurs when a child class provides its own implementation of a method inherited from its parent class.

It is commonly used to achieve runtime polymorphism.
"""

class Animal:

    def sound(self):
        print("Animal makes a sound")


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

# The same method sound() behaves differently
# depending on the object calling it.


"""
3. RUNTIME POLYMORPHISM
------------------------------------------------------------

Runtime polymorphism means the method implementation is selected based on the actual object at runtime.

Method overriding is a common way to achieve it.
"""

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


class Cat(Animal):

    def sound(self):
        print("Cat meows")


def make_sound(animal):
    animal.sound()


make_sound(Dog())
make_sound(Cat())

# Output:
# Dog barks
# Cat meows


"""
4. DUCK TYPING
------------------------------------------------------------

Duck typing is an important Python concept related to polymorphism.

The idea is:

"If an object behaves like what we need, we can use it."

Python focuses on the object's behavior rather than requiring it to belong to a particular class.
"""

class Dog:

    def speak(self):
        print("Bark")


class Person:

    def speak(self):
        print("Hello")


class Robot:

    def speak(self):
        print("Beep")


def make_sound(obj):
    obj.speak()


make_sound(Dog())
make_sound(Person())
make_sound(Robot())

# Output:
# Bark
# Hello
# Beep

# All three classes provide the speak() method.
# Therefore, they can be used with make_sound().


"""
5. OPERATOR OVERLOADING
------------------------------------------------------------

Operator overloading means giving special behavior to operators such as +, -, *, and == for custom objects.

Python uses special methods, also called:
1. Magic methods
2. Dunder methods

Example:

__add__() controls the behavior of the + operator.
"""

class Calculator:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


a = Calculator(10)
b = Calculator(20)

print(a + b)

# Output:
# 30

# Here, a + b internally calls:
# a.__add__(b)


"""
6. COMMON OPERATOR OVERLOADING METHODS
------------------------------------------------------------

+  -> __add__()
-  -> __sub__()
*  -> __mul__()
/  -> __truediv__()
// -> __floordiv__()
%  -> __mod__()
** -> __pow__()
== -> __eq__()
!= -> __ne__()
<  -> __lt__()
>  -> __gt__()
<= -> __le__()
>= -> __ge__()

These special methods allow custom objects to support built-in operators.


7. METHOD OVERLOADING IN PYTHON
------------------------------------------------------------

Method overloading means defining multiple methods with the same name but different parameter lists.

Languages like Java support traditional method overloading based on method signatures.

Python does not support traditional signature-based method overloading directly.

However, similar functionality can be achieved using default arguments and *args.


7.1 USING DEFAULT ARGUMENTS
--------------------------------------------------------
"""

class Calculator:

    def add(self, a, b=0, c=0):
        return a + b + c


obj = Calculator()

print(obj.add(10, 20))
print(obj.add(10, 20, 30))
print(obj.add(10))

# Output:
# 30
# 60
# 10


"""
7.2 USING *args
--------------------------------------------------------

*args allows a method to accept a variable number of positional arguments.
"""

class Calculator:

    def add(self, *args):
        return sum(args)


obj = Calculator()

print(obj.add(10, 20))
print(obj.add(10, 20, 30))
print(obj.add(10, 20, 30, 40))

# Output:
# 30
# 60
# 100


"""
8. POLYMORPHISM USING A COMMON INTERFACE
------------------------------------------------------------

Different classes can implement the same method.

A common interface allows us to use different objects in a consistent way.
"""

class Payment:

    def pay(self, amount):
        raise NotImplementedError(
            "Child class must implement pay()"
        )


class CreditCard(Payment):

    def pay(self, amount):
        print("Credit Card Payment:", amount)


class UPI(Payment):

    def pay(self, amount):
        print("UPI Payment:", amount)


class NetBanking(Payment):

    def pay(self, amount):
        print("Net Banking Payment:", amount)


def process_payment(payment, amount):
    payment.pay(amount)


process_payment(CreditCard(), 1000)
process_payment(UPI(), 2000)
process_payment(NetBanking(), 3000)

# Output:
# Credit Card Payment: 1000
# UPI Payment: 2000
# Net Banking Payment: 3000

# Different objects use the same pay() method
# with their own implementations.


"""
9. METHOD OVERLOADING VS METHOD OVERRIDING
------------------------------------------------------------

+----------------------+---------------------------+
| Method Overloading   | Method Overriding        |
+----------------------+---------------------------+
| Same method name     | Same method name         |
| Different parameters | Child redefines parent   |
| Python does not      | Supported in Python      |
| support traditional  |                           |
| signature-based      |                           |
| overloading          |                           |
| Similar behavior    | Achieved through         |
| using default args   | inheritance               |
| and *args            |                           |
+----------------------+---------------------------+


10. TYPES OF POLYMORPHISM - SUMMARY
------------------------------------------------------------

+----------------------------+-----------------------------+
| Type                       | Explanation                 |
+----------------------------+-----------------------------+
| Method Overriding          | Child class redefines       |
|                            | parent method               |
+----------------------------+-----------------------------+
| Runtime Polymorphism       | Implementation is selected |
|                            | based on the actual object |
+----------------------------+-----------------------------+
| Duck Typing                | Objects are used based on  |
|                            | their behavior               |
+----------------------------+-----------------------------+
| Operator Overloading       | Operators behave differently|
|                            | for custom objects          |
+----------------------------+-----------------------------+
| Overloading-like Behavior  | Flexible arguments or       |
|                            | default parameters          |
+----------------------------+-----------------------------+


11. IMPORTANT POINTS TO REMEMBER
------------------------------------------------------------

1. Polymorphism means one name, multiple forms.
2. Method overriding is supported in Python.
3. Runtime polymorphism is commonly achieved through method overriding.
4. Duck typing focuses on object behavior.
5. Operator overloading uses magic methods.
6. __add__() controls the + operator.
7. Python does not support traditional signature-based method overloading directly.
8. Default arguments and *args provide overloading-like behavior.
9. Different objects can implement the same method with different behaviors.
10. Polymorphism improves flexibility and code reuse.
"""
