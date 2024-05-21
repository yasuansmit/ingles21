import math

def main():
    option = 0
    results = {}  # Dictionary to store operation results

    while option != 7:
        print("Select the operation you want to perform:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square Root")
        print("6. Check if a number is prime")
        print("7. Exit")
        print("8. View previous results")

        option = int(input("Enter the number of the operation: "))

        if option in [1, 2, 3, 4, 5, 6]:
            result = perform_operation(option)
            results[option] = result
        elif option == 7:
            print("Exiting the program...")
        elif option == 8:
            view_results(results)
        else:
            print("Invalid option. Please select a valid option.")

def perform_operation(option):
    if option == 1:
        return perform_addition()
    elif option == 2:
        return perform_subtraction()
    elif option == 3:
        return perform_multiplication()
    elif option == 4:
        return perform_division()
    elif option == 5:
        return calculate_square_root()
    elif option == 6:
        return check_if_prime()

def perform_addition():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print("The result of the addition is:", result)
    return result

def perform_subtraction():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 - num2
    print("The result of the subtraction is:", result)
    return result

def perform_multiplication():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 * num2
    print("The result of the multiplication is:", result)
    return result

def perform_division():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num2 != 0:
        result = num1 / num2
        print("The result of the division is:", result)
        return result
    else:
        print("Cannot divide by zero.")
        return None

def calculate_square_root():
    num = float(input("Enter the number to calculate its square root: "))
    if num >= 0:
        result = math.sqrt(num)
        print("The square root of", num, "is:", result)
        return result
    else:
        print("Cannot calculate square root of a negative number.")
        return None

def check_if_prime():
    num = int(input("Enter a number to check if it's prime: "))
    if num > 1:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                print(num, "is not prime.")
                return False
        else:
            print(num, "is prime.")
            return True
    else:
        print(num, "is not prime.")
        return False

def view_results(results):
    if results:
        print("Previous results:")
        for operation, result in results.items():
            print(f"Operation {operation}: {result}")
    else:
        print("No previous results.")

main()