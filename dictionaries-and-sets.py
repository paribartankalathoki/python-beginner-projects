# ============================================================
# DICTIONARIES AND SETS
# ============================================================


# ============================================================
# 1. DICTIONARIES
# ============================================================

# A dictionary is a built-in Python data structure that stores
# data as key-value pairs.
#
# Think of a real dictionary:
# key   -> word
# value -> meaning
#
# Python dictionary:
# key   -> identifier
# value -> data


# ------------------------------------------------------------
# Creating a Dictionary
# ------------------------------------------------------------

pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}

# The dictionary above contains 4 key-value pairs:
#
# 'name'               -> 'Margherita Pizza'
# 'price'              -> 8.9
# 'calories_per_slice' -> 250
# 'toppings'           -> ['mozzarella', 'basil']


# General dictionary syntax:
#
# dictionary = {
#     'key1': value1,
#     'key2': value2,
#     'key3': value3
# }


# ------------------------------------------------------------
# Creating a Dictionary Using dict()
# ------------------------------------------------------------

# Another way to create a dictionary is by using the dict()
# constructor.
#
# We can pass a list of tuples to dict().
#
# Each tuple contains:
#     first element  -> key
#     second element -> value

pizza = dict([
    ('name', 'Margherita Pizza'),
    ('price', 8.9),
    ('calories_per_slice', 250),
    ('toppings', ['mozzarella', 'basil'])
])

# Example of one key-value tuple:
#
# ('name', 'Margherita Pizza')
#
# key   -> 'name'
# value -> 'Margherita Pizza'


# ============================================================
# 2. SETS
# ============================================================

# A set is a collection of unique elements.
#
# Sets do not store duplicate values.
#
# Example:

my_set = {1, 2, 3, 4, 5}


# If we try to create a set with duplicate values,
# the duplicates are automatically removed.

my_set = {1, 2, 2, 3, 3, 4}

# Result:
# {1, 2, 3, 4}


# ============================================================
# 3. ADDING ELEMENTS TO A SET
# ============================================================

# The add() method adds an element to a set.

my_set = {1, 2, 3, 4, 5}

my_set.add(6)

print(my_set)

# Result:
# {1, 2, 3, 4, 5, 6}


# Syntax:
#
# set_name.add(element)


# ============================================================
# 4. REMOVING ELEMENTS FROM A SET
# ============================================================

# remove() removes an element from a set.

my_set = {1, 2, 3, 4, 5}

my_set.remove(4)

print(my_set)

# Result:
# {1, 2, 3, 5}


# IMPORTANT:
# remove() raises an error if the element does not exist.


# ------------------------------------------------------------
# discard()
# ------------------------------------------------------------

# discard() also removes an element from a set.

my_set = {1, 2, 3, 4, 5}

my_set.discard(4)

print(my_set)

# Result:
# {1, 2, 3, 5}


# IMPORTANT:
# discard() does NOT raise an error if the element
# does not exist.


# Easy way to remember:
#
# remove()  -> error if element doesn't exist
# discard() -> no error if element doesn't exist


# ============================================================
# 5. CLEARING A SET
# ============================================================

# clear() removes all elements from a set.

my_set = {1, 2, 3, 4, 5}

my_set.clear()

print(my_set)

# Result:
# set()


# ============================================================
# 6. SET RELATIONSHIP METHODS
# ============================================================

my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}


# ------------------------------------------------------------
# issubset()
# ------------------------------------------------------------

# issubset() checks whether all elements of one set
# are present in another set.

print(your_set.issubset(my_set))

# Result:
# False
#
# Why?
# your_set contains 6, but 6 is not present in my_set.


# Easy way to remember:
#
# subset -> "Are ALL of my elements inside the other set?"


# ------------------------------------------------------------
# issuperset()
# ------------------------------------------------------------

# issuperset() checks whether one set contains all
# elements of another set.

print(my_set.issuperset(your_set))

# Result:
# False
#
# Why?
# my_set does not contain 6.


# Easy way to remember:
#
# superset -> "Do I contain ALL elements of the other set?"


# ------------------------------------------------------------
# isdisjoint()
# ------------------------------------------------------------

# isdisjoint() checks whether two sets have NO elements
# in common.

print(my_set.isdisjoint(your_set))

# Result:
# False
#
# Why?
# Both sets contain:
# 2, 3, 4


# If two sets have no common elements:
#
# set1 = {1, 2}
# set2 = {3, 4}
#
# set1.isdisjoint(set2)
# Result:
# True


# ============================================================
# 7. SET OPERATORS
# ============================================================

my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}


# There are four important set operators:
#
# |  -> Union
# &  -> Intersection
# -  -> Difference
# ^  -> Symmetric Difference


# ============================================================
# 8. UNION OPERATOR |
# ============================================================

# The union operator | returns all elements from both sets.

result = my_set | your_set

print(result)

# Result:
# {1, 2, 3, 4, 5, 6}


# Easy way to remember:
#
# UNION = EVERYTHING


# ============================================================
# 9. INTERSECTION OPERATOR &
# ============================================================

# The intersection operator & returns only the elements
# that are present in BOTH sets.

result = my_set & your_set

print(result)

# Result:
# {2, 3, 4}


# Easy way to remember:
#
# INTERSECTION = COMMON ELEMENTS


# ============================================================
# 10. DIFFERENCE OPERATOR -
# ============================================================

# The difference operator - returns elements that are
# in the first set but NOT in the second set.

result = my_set - your_set

print(result)

# Result:
# {1, 5}
#
# Why?
# 1 and 5 are in my_set but not in your_set.


# IMPORTANT:
# The order matters when using the difference operator.
#
# my_set - your_set
# is different from:
# your_set - my_set


# Example:

print(your_set - my_set)

# Result:
# {6}


# ============================================================
# 11. SYMMETRIC DIFFERENCE OPERATOR ^
# ============================================================

# The symmetric difference operator ^ returns elements
# that are in either set, but NOT in both sets.

result = my_set ^ your_set

print(result)

# Result:
# {1, 5, 6}
#
# 1 -> only in my_set
# 5 -> only in my_set
# 6 -> only in your_set
#
# 2, 3, 4 are in both sets, so they are NOT included.


# Easy way to remember:
#
# SYMMETRIC DIFFERENCE = EVERYTHING EXCEPT COMMON ELEMENTS


# ============================================================
# 12. SET ASSIGNMENT OPERATORS
# ============================================================

# Python also provides operators that perform a set
# operation AND update the original set.


# |=  -> Union and update
# &=  -> Intersection and update
# -=  -> Difference and update
# ^=  -> Symmetric difference and update


# ------------------------------------------------------------
# |= Union and Update
# ------------------------------------------------------------

my_set = {1, 2, 3}
your_set = {3, 4, 5}

my_set |= your_set

print(my_set)

# Result:
# {1, 2, 3, 4, 5}


# This is equivalent to:
#
# my_set = my_set | your_set


# ------------------------------------------------------------
# &= Intersection and Update
# ------------------------------------------------------------

my_set = {1, 2, 3}
your_set = {2, 3, 4}

my_set &= your_set

print(my_set)

# Result:
# {2, 3}


# This is equivalent to:
#
# my_set = my_set & your_set


# ------------------------------------------------------------
# -= Difference and Update
# ------------------------------------------------------------

my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

my_set -= your_set

print(my_set)

# Result:
# {1, 5}


# This is equivalent to:
#
# my_set = my_set - your_set


# ------------------------------------------------------------
# ^= Symmetric Difference and Update
# ------------------------------------------------------------

my_set = {1, 2, 3, 4}
your_set = {3, 4, 5, 6}

my_set ^= your_set

print(my_set)

# Result:
# {1, 2, 5, 6}


# This is equivalent to:
#
# my_set = my_set ^ your_set


# ============================================================
# QUICK REVISION
# ============================================================

# DICTIONARY
#
# Dictionary stores:
#     key -> value
#
# Example:
#
# person = {
#     'name': 'John',
#     'age': 25
# }


# SET
#
# Set stores unique elements.
#
# Example:
#
# my_set = {1, 2, 3, 4}


# SET METHODS
#
# add()       -> Add an element
# remove()    -> Remove an element (error if missing)
# discard()   -> Remove an element (no error if missing)
# clear()     -> Remove all elements
#
# issubset()  -> Check if all elements are inside another set
# issuperset()-> Check if set contains all elements of another set
# isdisjoint()-> Check if two sets have no elements in common


# SET OPERATORS
#
# |  -> Union
# &  -> Intersection
# -  -> Difference
# ^  -> Symmetric Difference


# SET UPDATE OPERATORS
#
# |= -> Union and update
# &= -> Intersection and update
# -= -> Difference and update
# ^= -> Symmetric difference and update


# ============================================================
# EASY MEMORY TRICK
# ============================================================

# |  -> EVERYTHING
# &  -> COMMON
# -  -> ONLY IN FIRST SET
# ^  -> DIFFERENT / NOT COMMON
