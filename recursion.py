
# Program 1: Factorial using Recursion

"""
This program calculates the factorial of a number
entered by the user using a recursive function.
"""

print("\n========== FACTORIAL USING RECURSION ==========\n")

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial of", num, "is:", factorial(num))



# Program 2: Fibonacci Series using Recursion

"""
This program generates the Fibonacci series
for the number of terms entered by the user.
Each number is the sum of the previous two numbers.
"""

print("\n========== FIBONACCI SERIES USING RECURSION ==========\n")

def fibonacci(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

terms = int(input("Enter the number of terms: "))

for i in range(terms):
    print(fibonacci(i), end=" ")

print("\n\n")
