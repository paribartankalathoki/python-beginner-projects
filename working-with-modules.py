# ============================================================
# STANDARD LIBRARY AND MODULES
# ============================================================


# ============================================================
# 1. WHAT IS THE PYTHON STANDARD LIBRARY?
# ============================================================

# The Python Standard Library is a collection of modules
# that come built into Python.
#
# These modules provide useful functions, classes, constants,
# and other tools that we can use in our programs.
#
# Examples of standard library modules:
#
# math
# datetime
# random
# os
# sys
# json
#
# We use the import statement to use these modules.


# ============================================================
# 2. IMPORTING A MODULE
# ============================================================

# We use the "import" statement to import a module.
#
# General syntax:
#
# import module_name


# Example:

import math


# Once a module is imported, we can access its elements
# using dot notation.
#
# General syntax:
#
# module_name.element


print(math.sqrt(36))

# Output:
# 6.0


# math -> module
# sqrt -> function
#
# math.sqrt() means:
# "Use the sqrt function from the math module."


# ============================================================
# 3. IMPORTING A MODULE WITH AN ALIAS
# ============================================================

# We can give a module a different name using "as".
#
# This is called an alias.
#
# General syntax:
#
# import module_name as alias


import math as m


# Now we can use "m" instead of "math".

print(m.sqrt(36))

# Output:
# 6.0


# Example:

print(m.pi)
print(m.sqrt(25))


# Aliases are useful when:
#
# 1. We want shorter code.
# 2. The module name is long.
# 3. We want to avoid naming conflicts.


# ============================================================
# 4. IMPORTING SPECIFIC ELEMENTS FROM A MODULE
# ============================================================

# Sometimes we don't need the entire module.
# We may only need one or two functions or classes.
#
# We can import only the elements we need.
#
# General syntax:
#
# from module_name import name1, name2


from math import radians, sin, cos


# Now we can use these functions directly.
#
# We don't need to write:
#
# math.radians()
# math.sin()
# math.cos()
#
# We can simply write:
#
# radians()
# sin()
# cos()


# ============================================================
# 5. EXAMPLE USING SPECIFIC IMPORTS
# ============================================================

from math import radians, sin, cos

angle_degrees = 40

# Convert degrees to radians:

angle_radians = radians(angle_degrees)

# Calculate sine:

sine_value = sin(angle_radians)

# Calculate cosine:

cos_value = cos(angle_radians)

print(sine_value)
print(cos_value)

# Output:
#
# 0.6427876096865393
# 0.766044443118978


# ============================================================
# 6. IMPORTING SPECIFIC ELEMENTS WITH AN ALIAS
# ============================================================

# We can also give an imported function or element
# a different name using "as".
#
# General syntax:
#
# from module_name import name as alias


from math import sqrt as square_root


print(square_root(36))

# Output:
# 6.0


# sqrt        -> original function name
# square_root -> alias


# ============================================================
# 7. IMPORTING MULTIPLE ELEMENTS WITH ALIASES
# ============================================================

# We can give multiple imported elements aliases.
#
# General syntax:
#
# from module_name import name1 as alias1, name2 as alias2


from math import sqrt as square_root, pow as power


print(square_root(25))
print(power(5, 2))

# Output:
#
# 5.0
# 25.0


# ============================================================
# 8. IMPORTING EVERYTHING USING *
# ============================================================

# We can use "*" to import everything from a module.
#
# General syntax:
#
# from module_name import *


# Example:
#
# from math import *
#
# print(sqrt(36))
# print(pow(5, 2))
# print(exp(1))


# NOTE:
#
# Although this is valid Python, using "*" is generally
# not recommended.
#
# It can make it difficult to know where a function or
# variable came from.
#
# It is usually better to import only what you need.


# ============================================================
# 9. IMPORTING CONSTANTS
# ============================================================

# Modules can contain constants as well as functions.
#
# The math module contains the constant pi.


import math

print(math.pi)

# Output:
# 3.141592653589793


# We can also import pi directly:

from math import pi

print(pi)


# ============================================================
# 10. IMPORTING CLASSES
# ============================================================

# Modules can also contain classes.
#
# The datetime module contains classes for working
# with dates and times.


from datetime import date


# Create a date object:

my_date = date(1959, 7, 15)


# Access the individual parts of the date:

print(my_date.day)
print(my_date.month)
print(my_date.year)

# Output:
#
# 15
# 7
# 1959


# date     -> class
# my_date  -> object
# day      -> attribute
# month    -> attribute
# year     -> attribute


# ============================================================
# 11. DOT NOTATION
# ============================================================

# Dot notation is used to access elements inside a module
# or attributes/methods inside an object.
#
# General syntax:
#
# object_or_module.element


# Examples:

import math

print(math.pi)
print(math.sqrt(25))


# Here:
#
# math.pi
#     -> accesses pi from the math module
#
# math.sqrt()
#     -> accesses the sqrt function from the math module


# Another example:

from datetime import date

my_date = date(1959, 7, 15)

print(my_date.day)
print(my_date.month)
print(my_date.year)


# ============================================================
# 12. __name__ VARIABLE
# ============================================================

# __name__ is a special built-in variable in Python.
#
# Its value depends on how the Python file is being used.


# If a Python file is executed directly:
#
# __name__ == "__main__"


# If a Python file is imported as a module:
#
# __name__ == the name of the module


# ============================================================
# 13. CHECKING __name__
# ============================================================

print(__name__)


# Since we are running this file directly, the output will be:
#
# __main__


# ============================================================
# 14. if __name__ == "__main__"
# ============================================================

# A very common Python pattern is:

if __name__ == '__main__':
    print("This file is running directly.")


# The code inside this block runs only when the file
# is executed directly.


# ============================================================
# 15. WHY DO WE USE if __name__ == "__main__"?
# ============================================================

# A Python file can be used in two different ways:
#
# 1. It can be executed directly.
# 2. It can be imported into another Python file.
#
#
# When the file is executed directly:
#
#     __name__ == "__main__"
#
# Therefore, the code inside:
#
#     if __name__ == "__main__":
#
# will run.
#
#
# When the file is imported:
#
#     __name__ == the module name
#
# Therefore, the code inside:
#
#     if __name__ == "__main__":
#
# will NOT run automatically.


# ============================================================
# 16. SIMPLE EXAMPLE OF __name__
# ============================================================

# Imagine this file is called:
#
# working_with_modules.py
#
# If we run it directly:
#
# python working_with_modules.py
#
# Python sets:
#
# __name__ = "__main__"


if __name__ == '__main__':
    print("Running the main program.")


# If another Python file imports this file:
#
# import working_with_modules
#
# Then inside this file:
#
# __name__ = "working_with_modules"
#
# So the code inside the if statement will not run.


# ============================================================
# 17. FUNCTIONS + __name__
# ============================================================

# We can define functions in our Python file and then
# choose to run them only when the file is executed directly.


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


if __name__ == '__main__':
    print(add(10, 5))
    print(subtract(10, 5))


# Output when this file is run directly:
#
# 15
# 5


# ============================================================
# 18. IMPORTANT CONCEPT
# ============================================================

# Code outside the if __name__ == "__main__" block can
# execute when a module is imported.
#
# Functions and classes can be defined without being executed.
#
# This is why we commonly put our testing or main program
# code inside:
#
# if __name__ == '__main__':
#
# This prevents that code from running automatically
# when the file is imported.


# ============================================================
# 19. COMPLETE EXAMPLE
# ============================================================

# Imagine this file contains:

def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


if __name__ == '__main__':
    print(multiply(5, 4))
    print(divide(20, 5))


# If we run this file directly:
#
# Output:
#
# 20
# 4.0
#
#
# If another Python file imports this module:
#
# import working_with_modules
#
# The print statements above will NOT run automatically.
#
# But the functions can still be used:
#
# working_with_modules.multiply(5, 4)
# working_with_modules.divide(20, 5)


# ============================================================
# QUICK REVISION
# ============================================================

# IMPORT A MODULE:
#
# import math
#
# Use:
#
# math.sqrt(25)


# IMPORT WITH ALIAS:
#
# import math as m
#
# Use:
#
# m.sqrt(25)


# IMPORT SPECIFIC ELEMENTS:
#
# from math import sqrt, pi
#
# Use:
#
# sqrt(25)
# pi


# IMPORT WITH ALIAS:
#
# from math import sqrt as square_root
#
# Use:
#
# square_root(25)


# IMPORT EVERYTHING:
#
# from math import *
#
# Use:
#
# sqrt(25)
#
# Generally avoid this when possible.


# ============================================================
# IMPORTANT IMPORT SYNTAX
# ============================================================

# 1. Import entire module:
#
# import module_name


# 2. Import module with alias:
#
# import module_name as alias


# 3. Import specific elements:
#
# from module_name import name1, name2


# 4. Import specific elements with aliases:
#
# from module_name import name1 as alias1


# 5. Import everything:
#
# from module_name import *


# ============================================================
# __name__ QUICK REVISION
# ============================================================

# __name__ is a special built-in variable.


# When the file is executed directly:
#
# __name__ == "__main__"


# When the file is imported:
#
# __name__ == module_name


# Common Python pattern:

if __name__ == '__main__':
    # Code here runs only when this file
    # is executed directly.
    pass


# ============================================================
# EASY MEMORY TRICK
# ============================================================

# import math
#     -> Import the entire math module.
#
#
# import math as m
#     -> Import math with a shorter name.
#
#
# from math import sqrt
#     -> Import only sqrt.
#
#
# from math import sqrt as square_root
#     -> Import sqrt with a new name.
#
#
# from math import *
#     -> Import everything.
#
#
# if __name__ == '__main__':
#     -> Run this code only when the file is executed directly.
