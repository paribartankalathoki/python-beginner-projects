# ============================================================
# LISTS
# ============================================================

# A list is an ordered, mutable collection.
# "Mutable" means we can change, add, or remove items.

cities = ['Los Angeles', 'London', 'Tokyo']

# Access an item using its index.
# Indexing starts from 0.
cities[0]  # 'Los Angeles'


# ------------------------------------------------------------
# Converting a string into a list
# ------------------------------------------------------------

developer = 'Jessica'

# list() converts an iterable into a list.
# A string is iterable, so each character becomes an item.
list(developer)
# ['J', 'e', 's', 's', 'i', 'c', 'a']


# ------------------------------------------------------------
# len()
# ------------------------------------------------------------

# len() returns the number of items in a collection.

numbers = [1, 2, 3, 4, 5]
len(numbers)  # 5


# ------------------------------------------------------------
# Changing an item in a list
# ------------------------------------------------------------

# Lists are mutable, so we can change individual items.

programming_languages = ['Python', 'Java', 'C++', 'Rust']

programming_languages[0] = 'JavaScript'

print(programming_languages)
# ['JavaScript', 'Java', 'C++', 'Rust']


# ------------------------------------------------------------
# Checking if an item exists
# ------------------------------------------------------------

# The "in" operator checks whether an item exists in a list.
# It returns True or False.

programming_languages = ['Python', 'Java', 'C++', 'Rust']

'Rust' in programming_languages        # True
'JavaScript' in programming_languages  # False


# ------------------------------------------------------------
# Nested lists
# ------------------------------------------------------------

# A list can contain another list.
# This is called a nested list.

developer = ['Alice', 25, ['Python', 'Rust', 'C++']]

developer[2]
# ['Python', 'Rust', 'C++']


# ------------------------------------------------------------
# Deleting an item
# ------------------------------------------------------------

# del removes an item from a list using its index.

developer = ['Jane Doe', 23, 'Python Developer']

del developer[1]

print(developer)
# ['Jane Doe', 'Python Developer']


# ============================================================
# LIST UNPACKING
# ============================================================

# List unpacking assigns list items to multiple variables.

developer = ['Alice', 34, 'Rust Developer']

name, age, job = developer

print(name)  # 'Alice'
print(age)   # 34
print(job)   # 'Rust Developer'


# ------------------------------------------------------------
# Extended unpacking with *
# ------------------------------------------------------------

# * collects the remaining items into a list.

developer = ['Alice', 34, 'Rust Developer']

name, *rest = developer

print(name)  # 'Alice'
print(rest)  # [34, 'Rust Developer']


# ------------------------------------------------------------
# Unpacking error
# ------------------------------------------------------------

# The number of variables must normally match
# the number of items in the list.

developer = ['Alice', 34, 'Rust Developer']

# This causes ValueError because there are 4 variables
# but only 3 items.
#
# name, age, job, city = developer
#
# ValueError: not enough values to unpack
# (expected 4, got 3)


# ============================================================
# LIST SLICING
# ============================================================

# Syntax:
# list[start:stop:step]

numbers = [1, 2, 3, 4, 5, 6]

# Start at index 1, go to the end, and take every 2nd item.
numbers[1::2]
# [2, 4, 6]


# ============================================================
# COMMON LIST METHODS
# ============================================================


# ------------------------------------------------------------
# append()
# ------------------------------------------------------------

# append() adds ONE item to the end of a list.

numbers = [1, 2, 3, 4, 5]

numbers.append(6)

print(numbers)
# [1, 2, 3, 4, 5, 6]


# append() can also add another list as a single item.

numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.append(even_numbers)

print(numbers)
# [1, 2, 3, 4, 5, [6, 8, 10]]


# ------------------------------------------------------------
# extend()
# ------------------------------------------------------------

# extend() adds each item from another iterable
# to the end of the list.

numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.extend(even_numbers)

print(numbers)
# [1, 2, 3, 4, 5, 6, 8, 10]


# IMPORTANT:
# append() -> adds the entire object as ONE item
# extend() -> adds each item individually


# ------------------------------------------------------------
# insert()
# ------------------------------------------------------------

# insert(index, value) adds an item at a specific position.

numbers = [1, 2, 3, 4, 5]

numbers.insert(2, 2.5)

print(numbers)
# [1, 2, 2.5, 3, 4, 5]


# ------------------------------------------------------------
# remove()
# ------------------------------------------------------------

# remove() removes the FIRST occurrence of a value.

numbers = [10, 20, 30, 40, 50, 50]

numbers.remove(50)

print(numbers)
# [10, 20, 30, 40, 50]


# If the value appears multiple times,
# remove() only removes the first occurrence.

numbers = [10, 20, 30, 40, 50, 50, 50]

numbers.remove(50)

print(numbers)
# [10, 20, 30, 40, 50, 50]


# ------------------------------------------------------------
# pop()
# ------------------------------------------------------------

# pop() removes and RETURNS an item.
# Without an index, it removes the last item.

numbers = [1, 2, 3, 4, 5]

numbers.pop(1)
# Removes and returns 2


numbers = [1, 2, 3, 4, 5]

numbers.pop()
# Removes and returns 5


# ------------------------------------------------------------
# clear()
# ------------------------------------------------------------

# clear() removes ALL items from the list.

numbers = [1, 2, 3, 4, 5]

numbers.clear()

print(numbers)
# []


# ------------------------------------------------------------
# sort()
# ------------------------------------------------------------

# sort() changes the original list.
# By default, it sorts in ascending order.

numbers = [19, 2, 35, 1, 67, 41]

numbers.sort()

print(numbers)
# [1, 2, 19, 35, 41, 67]


# ------------------------------------------------------------
# sorted()
# ------------------------------------------------------------

# sorted() creates a NEW sorted list.
# The original list remains unchanged.

numbers = [19, 2, 35, 1, 67, 41]

sorted_numbers = sorted(numbers)

print(numbers)
# [19, 2, 35, 1, 67, 41]

print(sorted_numbers)
# [1, 2, 19, 35, 41, 67]


# IMPORTANT:
# list.sort() -> changes the original list
# sorted(list) -> creates a new sorted list


# ------------------------------------------------------------
# reverse()
# ------------------------------------------------------------

# reverse() reverses the order of items in the original list.

numbers = [6, 5, 4, 3, 2, 1]

numbers.reverse()

print(numbers)
# [1, 2, 3, 4, 5, 6]


# ------------------------------------------------------------
# index()
# ------------------------------------------------------------

# index() returns the position of the first matching item.

programming_languages = ['Rust', 'Java', 'Python', 'C++']

programming_languages.index('Java')
# 1


# If the item doesn't exist, index() raises ValueError.

# programming_languages.index('JavaScript')
#
# ValueError: 'JavaScript' is not in list


# ============================================================
# TUPLES
# ============================================================

# A tuple is similar to a list, but it is IMMUTABLE.
# Immutable means we cannot change, add, or remove individual items.

developer = ('Alice', 34, 'Rust Developer')


# ------------------------------------------------------------
# Accessing tuple items
# ------------------------------------------------------------

programming_languages = ('Python', 'Java', 'C++', 'Rust')

developer = ('Alice', 34, 'Rust Developer')

developer[1]
# 34


# ------------------------------------------------------------
# Tuple immutability
# ------------------------------------------------------------

# You cannot change an existing tuple item.

programming_languages = ('Python', 'Java', 'C++', 'Rust')

# programming_languages[0] = 'JavaScript'
#
# TypeError:
# 'tuple' object does not support item assignment


# ------------------------------------------------------------
# Tuple indexing errors
# ------------------------------------------------------------

numbers = (1, 2, 3, 4, 5)

# Index 7 does not exist.
#
# numbers[7]
#
# IndexError: tuple index out of range


# ------------------------------------------------------------
# Converting a string to a tuple
# ------------------------------------------------------------

developer = 'Jessica'

tuple(developer)
# ('J', 'e', 's', 's', 'i', 'c', 'a')


# ------------------------------------------------------------
# Checking membership in a tuple
# ------------------------------------------------------------

programming_languages = ('Python', 'Java', 'C++', 'Rust')

'Rust' in programming_languages        # True
'JavaScript' in programming_languages  # False


# ------------------------------------------------------------
# Tuple unpacking
# ------------------------------------------------------------

developer = ('Alice', 34, 'Rust Developer')

name, age, job = developer

print(name)  # 'Alice'
print(age)   # 34
print(job)   # 'Rust Developer'


# ------------------------------------------------------------
# Tuple deletion
# ------------------------------------------------------------

# You cannot delete individual items from a tuple.

developer = ('Jane Doe', 23, 'Python Developer')

# del developer[1]
#
# TypeError:
# 'tuple' object doesn't support item deletion


# ============================================================
# LOOPS
# ============================================================

# Loops allow us to execute code repeatedly.


# ------------------------------------------------------------
# for loop
# ------------------------------------------------------------

# A for loop goes through each item in an iterable.

programming_languages = ['Rust', 'Java', 'Python', 'C++']

for language in programming_languages:
    print(language)


# A string is also iterable.
# A for loop can therefore go through each character.

for char in 'code':
    print(char)


# ------------------------------------------------------------
# while loop
# ------------------------------------------------------------

# A while loop keeps running as long as its condition is True.

secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input('Guess the number (1-5): '))

    if guess != secret_number:
        print('Wrong! Try again.')

print('You got it!')


# ============================================================
# break AND continue
# ============================================================


# ------------------------------------------------------------
# break
# ------------------------------------------------------------

# break immediately stops the loop.

developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        break

    print(developer)

# Output:
# Jess


# ------------------------------------------------------------
# continue
# ------------------------------------------------------------

# continue skips the current iteration
# and moves to the next iteration.

developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        continue

    print(developer)

# Output:
# Jess
# Tom


# ============================================================
# RANGE
# ============================================================

# range() generates a sequence of numbers.
#
# Syntax:
# range(start, stop, step)
#
# start = where to begin
# stop  = where to stop (NOT included)
# step  = how much to increase/decrease each time


# Example:
# range(5) -> 0, 1, 2, 3, 4


# ============================================================
# ENUMERATE
# ============================================================

# enumerate() gives us both:
# 1. the index
# 2. the value


languages = ['Spanish', 'English', 'Russian', 'Chinese']

index = 0

for language in languages:
    print(f'Index {index} and language {language}')
    index += 1


# Instead of manually creating and increasing an index,
# we can use enumerate().

languages = ['Spanish', 'English', 'Russian', 'Chinese']

list(enumerate(languages))
# [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]


# Common way to use enumerate():

for index, language in enumerate(languages):
    print(f'Index {index} and language {language}')


# We can specify the starting index.

for index, language in enumerate(languages, 1):
    print(f'Index {index} and language {language}')

# Indexes will start at 1 instead of 0.


# ============================================================
# ZIP
# ============================================================

# zip() combines items from multiple iterables
# based on their positions.

developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

list(zip(developers, ids))
# [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4)]


# zip() is useful when we want to loop through
# two related lists at the same time.

for name, dev_id in zip(developers, ids):
    print(f'Name: {name}')
    print(f'ID: {dev_id}')


# ============================================================
# LIST COMPREHENSIONS
# ============================================================

# A list comprehension is a shorter way to create a list
# using a loop and optionally a condition.
#
# Basic syntax:
#
# [expression for item in iterable]
#
# With a condition:
#
# [expression for item in iterable if condition]


# ------------------------------------------------------------
# Normal for loop
# ------------------------------------------------------------

even_numbers = []

for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)


# The same thing using a list comprehension:

even_numbers = [num for num in range(21) if num % 2 == 0]

print(even_numbers)


# ------------------------------------------------------------
# Conditional expression in a list comprehension
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5]

# If number is even -> "Even"
# Otherwise -> "Odd"

result = [
    (num, 'Even') if num % 2 == 0 else (num, 'Odd')
    for num in numbers
]

print(result)

# [(1, 'Odd'), (2, 'Even'), (3, 'Odd'), (4, 'Even'), (5, 'Odd')]


# ============================================================
# filter()
# ============================================================

# filter() keeps only the items for which
# the function returns True.

words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']


def is_long_word(word):
    return len(word) > 4


long_words = list(filter(is_long_word, words))

print(long_words)
# ['mountain', 'river', 'cloud']


# ============================================================
# map()
# ============================================================

# map() applies a function to EVERY item in an iterable.

celsius = [0, 10, 20, 30, 40]


def to_fahrenheit(temp):
    return (temp * 9 / 5) + 32


fahrenheit = list(map(to_fahrenheit, celsius))

print(fahrenheit)
# [32.0, 50.0, 68.0, 86.0, 104.0]


# ============================================================
# sum()
# ============================================================

# sum() adds numbers together.

numbers = [5, 10, 15, 20]

# start=10 means:
# add 10 to the result of summing the list.

total = sum(numbers, start=10)

print(total)
# 60


# Calculation:
# 5 + 10 + 15 + 20 + 10 = 60


# ============================================================
# LAMBDA FUNCTIONS
# ============================================================

# A lambda is a small anonymous function.
#
# Syntax:
#
# lambda arguments: expression


# Example:

lambda num: num ** 2

# This function takes a number and returns its square.


# ------------------------------------------------------------
# lambda with filter()
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5]

# Keep only numbers where x % 2 == 0.
# In other words, keep even numbers.

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print(even_numbers)
# [2, 4]


# ------------------------------------------------------------
# map() with a normal function
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5]


def square(num):
    return num ** 2


# Apply square() to every number.

squared_numbers = list(map(square, numbers))

print(squared_numbers)
# [1, 4, 9, 16, 25]



# ------------------------------------------------------------
# 🧠 Super-Quick Memory Map
# ------------------------------------------------------------

# LIST        → [] → changeable
# TUPLE       → () → unchangeable

# INDEX       → [0] → get item
# SLICE       → [1:4] → get range of items
# len()       → how many?

# append()    → add ONE
# extend()    → add MANY
# insert()    → add at position
# remove()    → remove by VALUE
# pop()       → remove by INDEX + return
# clear()     → remove ALL

# for         → for each
# while       → while condition
# break       → STOP
# continue    → SKIP

# range()     → generate numbers
# enumerate() → INDEX + VALUE
# zip()       → PAIR collections

# list comp   → CREATE a list
# filter()    → KEEP matching items
# map()       → TRANSFORM items
# sum()       → ADD numbers
# lambda      → SMALL anonymous function


# When to Use a Tuple vs. a List?
# Use a List ([]) when you need a dynamic collection of elements that may need to be added, removed, or updated.

# Use a Tuple (()) when you have a fixed collection of data that should not be changed.