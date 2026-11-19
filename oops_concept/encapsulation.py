"""
1. What is Encapsulation?

Encapsulation means combining data (attributes) and methods
inside a class and controlling how that data is accessed or modified.

In simple words:
Encapsulation helps protect data and control access to it.


2. Types of Access Conventions in Python

Python commonly uses three naming conventions:

+------------+-------------+--------------------------------------+
| Type       | Syntax      | Meaning                              |
+------------+-------------+--------------------------------------+
| Public     | name        | Accessible from anywhere             |
| Protected  | _name       | Intended for internal/subclass use   |
| Private    | __name      | Name-mangled to discourage direct    |
|            |             | access                               |
+------------+-------------+--------------------------------------+


3. Public Attributes

Public attributes can be accessed and modified from anywhere.

"""

class Student:

    def __init__(self):
        self.name = "Ram"


s1 = Student()

print(s1.name)



"""
4. Protected Attributes

Protected attributes use a single underscore (_).

They are intended for internal use or subclass use.
However, Python does not strictly restrict their access.
"""

class Student:

    def __init__(self):
        self._name = "Ram"


s1 = Student()

print(s1._name)


# A single underscore is a naming convention,
# not strict access protection.


"""
5. Private Attributes

Private attributes use double underscores (__).

Python performs name mangling to discourage direct access.
"""

class Student:

    def __init__(self):
        self.__name = "Ram"


s1 = Student()

# print(s1.__name)


# Python name-mangles __name into _Student__name.


"""
6. How to Access Private Attributes?

We can provide getter and setter methods to access
and modify private attributes.
"""


class Student:

    def __init__(self):
        self.__name = "Ram"

    # Getter method
    def get_name(self):
        return self.__name

    # Setter method
    def set_name(self, new_name):
        self.__name = new_name


s1 = Student()

print(s1.get_name())

s1.set_name("Hari")

print(s1.get_name())


"""
7. Using @property and @property.setter

Python provides @property to access methods like attributes.

@property         -> Getter
@property.setter  -> Setter

This provides a cleaner way to control attribute access.
"""


class Student:

    def __init__(self):
        self.__name = "Ram"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name


s1 = Student()

print(s1.name)

s1.name = "Hari"

print(s1.name)


"""
8. Practical Example of Encapsulation

Let's understand how encapsulation can protect
a bank account balance.

The balance is private, and we provide methods
to deposit, withdraw, and check the balance.
"""


class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)

account.deposit(500)
account.withdraw(200)

print("Current Balance:", account.get_balance())


"""
9. Difference Between Public, Protected, and Private Attributes

+----------------+------------------+------------------------------+
| Public         | Protected        | Private                      |
+----------------+------------------+------------------------------+
| name           | _name            | __name                       |
| Accessible     | Accessible, but  | Name-mangled by Python       |
| from anywhere  | intended for     | to discourage direct access  |
|                | internal use     |                              |
| No restriction | No strict access | No strict access restriction |
|                | restriction      |                              |
+----------------+------------------+------------------------------+


10. Important Points to Remember
----------------------------------------

1. Encapsulation combines data and methods inside a class.
2. Public attributes can be accessed directly.
3. Protected attributes use a single underscore (_).
4. Private attributes use double underscores (__).
5. Python uses name mangling for private attributes.
6. Getters and setters control how attributes are accessed and modified.
7. @property provides a cleaner way to implement getters and setters.
8. Python naming conventions do not provide strict security.
"""
