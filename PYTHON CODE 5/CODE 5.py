def calculator():
    print("Welcome to the Calculator App!")

    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Thank you for using the Calculator App!")
            break

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            result = add_numbers(num1, num2)
            print("Result:", result)
        elif choice == '2':
            result = subtract_numbers(num1, num2)
            print("Result:", result)
        elif choice == '3':
            result = multiply_numbers(num1, num2)
            print("Result:", result)
        elif choice == '4':
            result = divide_numbers(num1, num2)
            if result is not None:
                print("Result:", result)
        else:
            print("Invalid input. Please enter a number from 1 to 5.")
        print("\n")

# Run the calculator app
calculator()