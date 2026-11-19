"""
INHERITANCE IN PYTHON
---------------------------------------


1. What is Inheritance?

Inheritance allows one class to acquire the attributes and methods of another class.

Parent class = Base class
Child class  = Derived class

Example:

Parent class: Animal
Child classes: Dog and Cat

Both dogs and cats are animals, so they can share common functionality.

Benefits of inheritance:
1. Code reusability
2. Code organization
3. Easy maintenance
4. Method overriding
"""


"""
2. BASIC SYNTAX OF INHERITANCE
---------------------------------------

class Parent:
    pass

class Child(Parent):
    pass

Here, Child inherits from Parent.
"""


"""
3. SIMPLE INHERITANCE EXAMPLE
---------------------------------------

A child class can access the methods of its parent class.
"""

class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


d1 = Dog()

d1.eat()
d1.bark()

# Output:
# Animal is eating
# Dog is barking


"""
4. TYPES OF INHERITANCE
---------------------------------------

Python supports five commonly discussed inheritance structures.

1. Single Inheritance
2. Multiple Inheritance
3. Multilevel Inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance
"""


"""
4.1 SINGLE INHERITANCE
--------------------------------------------------------

One parent class -> One child class

        Parent
           |
         Child

A child class inherits from only one parent class.
"""

class Employee:

    def work(self):
        print("Employee is working")


class Developer(Employee):

    def coding(self):
        print("Developer is coding")


d1 = Developer()

d1.work()
d1.coding()

# Output:
# Employee is working
# Developer is coding


"""
4.2 MULTIPLE INHERITANCE
--------------------------------------------------------

Multiple parent classes -> One child class

       Parent A    Parent B
           \        /
             Child

A child class inherits from more than one parent class.
"""

class Father:

    def father_property(self):
        print("Father owns a house")


class Mother:

    def mother_property(self):
        print("Mother owns jewellery")


class Child(Father, Mother):

    def child_property(self):
        print("Child owns a bicycle")


c1 = Child()

c1.father_property()
c1.mother_property()
c1.child_property()

# Output:
# Father owns a house
# Mother owns jewellery
# Child owns a bicycle


"""
4.3 MULTILEVEL INHERITANCE
--------------------------------------------------------

Grandparent -> Parent -> Child

       Grandparent
            |
          Parent
            |
          Child

A class inherits from another child class, creating multiple levels of inheritance.
"""

class Grandparent:

    def house(self):
        print("Grandparent owns a house")


class Parent(Grandparent):

    def car(self):
        print("Parent owns a car")


class Child(Parent):

    def bike(self):
        print("Child owns a bike")


c1 = Child()

c1.house()
c1.car()
c1.bike()

# Output:
# Grandparent owns a house
# Parent owns a car
# Child owns a bike


"""
4.4 HIERARCHICAL INHERITANCE
--------------------------------------------------------

One parent class -> Multiple child classes

             Parent
             /    \
         Child A  Child B

Multiple child classes inherit from the same parent class.
"""

class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


class Cat(Animal):

    def meow(self):
        print("Cat is meowing")


d1 = Dog()
c1 = Cat()

d1.eat()
d1.bark()

c1.eat()
c1.meow()

# Output:
# Animal is eating
# Dog is barking
# Animal is eating
# Cat is meowing


"""
4.5 HYBRID INHERITANCE
--------------------------------------------------------

Hybrid inheritance is a combination of two or more inheritance structures.

Example: Multiple + Multilevel Inheritance

       Father       Mother
           \        /
             Child
               |
            Student

"""

class Father:

    def father_property(self):
        print("Father owns a house")


class Mother:

    def mother_property(self):
        print("Mother owns a car")


class Child(Father, Mother):

    def child_property(self):
        print("Child owns a bicycle")


class Student(Child):

    def study(self):
        print("Student is studying")


s1 = Student()

s1.father_property()
s1.mother_property()
s1.child_property()
s1.study()

# Output:
# Father owns a house
# Mother owns a car
# Child owns a bicycle
# Student is studying


"""
5. INHERITANCE WITH CONSTRUCTOR
---------------------------------------

A child class inherits the parent constructor if it does not define its own constructor.
"""

class Employee:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)


class Developer(Employee):

    def coding(self):
        print("Developer is coding")


d1 = Developer("Ram")

d1.display()
d1.coding()

# Output:
# Name: Ram
# Developer is coding

# Developer does not define its own constructor.
# Therefore, it inherits the constructor from Employee.


"""
6. UNDERSTANDING super()
---------------------------------------

super() allows a child class to call methods from the next class in the Method Resolution Order (MRO).

It is commonly used to call the parent constructor.
"""

class Employee:

    def __init__(self, name):
        self.name = name


class Developer(Employee):

    def __init__(self, name, language):

        super().__init__(name)

        self.language = language

    def display(self):
        print("Name:", self.name)
        print("Language:", self.language)


d1 = Developer("Ram", "Python")

d1.display()

# Output:
# Name: Ram
# Language: Python

# super().__init__(name)
# Calls the next class constructor in the MRO.


"""
7. METHOD OVERRIDING
---------------------------------------

Method overriding happens when a child class provides its own implementation of a method already defined in the parent class.
"""

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


a1 = Animal()
d1 = Dog()

a1.sound()
d1.sound()

# Output:
# Animal makes a sound
# Dog barks


"""
8. METHOD RESOLUTION ORDER (MRO)
---------------------------------------

MRO determines the order in which Python searches for methods and attributes in an inheritance hierarchy.

We can check MRO using:

ClassName.mro()
"""

class A:

    def show(self):
        print("Class A")


class B(A):
    pass


class C(B):
    pass


print(C.mro())

# Output:
# [<class '__main__.C'>,
#  <class '__main__.B'>,
#  <class '__main__.A'>,
#  <class 'object'>]

# Python searches in this order:
# C -> B -> A -> object


"""
9. MRO WITH MULTIPLE INHERITANCE
---------------------------------------

Python uses C3 linearization to determine MRO in multiple inheritance.
"""

class A:

    def show(self):
        print("Class A")


class B(A):

    def show(self):
        print("Class B")


class C(A):

    def show(self):
        print("Class C")


class D(B, C):
    pass


d1 = D()

d1.show()

print(D.mro())

# Output:
# Class B
#
# MRO:
# D -> B -> C -> A -> object

# Python searches B before C because D inherits from B first and then C.


"""
10. DIFFERENCE BETWEEN FIVE TYPES OF INHERITANCE
---------------------------------------

+------------------+----------------------------------+
| Type             | Structure                        |
+------------------+----------------------------------+
| Single           | One parent -> One child          |
| Multiple         | Multiple parents -> One child    |
| Multilevel       | Grandparent -> Parent -> Child   |
| Hierarchical     | One parent -> Multiple children  |
| Hybrid           | Combination of inheritance types |
+------------------+----------------------------------+


11. DIFFERENCE BETWEEN PARENT AND CHILD CLASS
---------------------------------------

+----------------------+---------------------------------+
| Parent Class         | Child Class                     |
+----------------------+---------------------------------+
| Base class           | Derived class                   |
| Provides attributes  | Inherits attributes             |
| Provides methods     | Inherits methods                |
| Can be inherited by- | Can extend parent functionality |
| multiple classes     | functionality                   |
+----------------------+---------------------------------+


12. IMPORTANT POINTS TO REMEMBER
---------------------------------------

1. Inheritance promotes code reusability.
2. Parent class is also called a base class.
3. Child class is also called a derived class.
4. Python supports five commonly discussed inheritance structures.
5. A child class can inherit the parent constructor.
6. super() calls the next implementation in the MRO.
7. Method overriding allows a child class to redefine a parent class method.
8. MRO determines the method lookup order.
9. Python uses C3 linearization for MRO.
10. Every Python class ultimately inherits from object unless a different hierarchy is specified.
"""
