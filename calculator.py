"""Calculator CLI App - Internship Task 1."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please enter a numeric value.")


def calculate(choice, a, b):
    operations = {"1": add, "2": subtract, "3": multiply, "4": divide}
    return operations[choice](a, b)


def main():
    print("=" * 34)
    print("       CALCULATOR CLI APP")
    print("=" * 34)

    while True:
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "5":
            print("Thanks for using the calculator!")
            break
        if choice not in {"1", "2", "3", "4"}:
            print("Invalid choice. Please select 1-5.")
            continue

        first = get_number("Enter first number: ")
        second = get_number("Enter second number: ")

        try:
            result = calculate(choice, first, second)
            print(f"Result: {result:g}")
        except ZeroDivisionError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
