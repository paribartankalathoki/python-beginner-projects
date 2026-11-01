
print("==============================")
print("    ARITHMETIC CALCULATOR   ")
print("==============================\n")

while True:
    first_number = float(input("Enter your first number: "))
    second_number = float(input("Enter your second number: "))

    print("\n==============================")
    print("      AVAILABLE OPERATIONS")
    print("==============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("==============================")

    choice = input("Enter your choice: ")

    print("\n------------------------------")

    if choice == "1":
        print(f'Operation: Addition between {first_number} and {second_number}')
        print("Output:", first_number + second_number)

    elif choice == "2":
        print(f'Operation: Subtraction between {first_number} and {second_number}')
        print("Output:", first_number - second_number)

    elif choice == "3":
        print(f'Operation: Multiplication between {first_number} and {second_number}')
        print("Output:", first_number * second_number)

    elif choice == "4":
        print(f'Operation: Division between {first_number} and {second_number}')
        if second_number == 0:
            print("Error: Cannot divide by zero")
        else:
            print("Output:", first_number / second_number)

    elif choice == "5":
        print("Thank you for using the calculator!")
        print("==============================")
        break

    else:
        print("Invalid choice!")

    print("------------------------------")

    if choice != "5":
        print("\n==============================")
        print("1. Calculate Again")
        print("2. Exit")
        print("==============================")

        again = input("Enter your next choice: ")

        print("------------------------------")

        if again == "2":
            print("Thank you for using the calculator!")
            print("==============================")
            break

        elif again == "1":
            print("\nStarting a new calculation...")
            print("==============================\n")
            continue

        else:
            print("Invalid choice. Exiting calculator.")
            print("==============================")
            break
