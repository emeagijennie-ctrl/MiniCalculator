while True:
    print("Select operation: 1.Add 2.Subtract 3.Multiply 4.Divide 5.Exit")
    choice = input("Enter choice: ")

    if choice == '5':
        print("Goodbye!")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", num1 + num2)
    elif choice == '2':
        print("Result:", num1 - num2)
    elif choice == '3':
        print("Result:", num1 * num2)
    elif choice == '4':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Cannot divide by zero")
    else:
        print("Invalid input")
    print()  # Blank line