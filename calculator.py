from art import art

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(art)  # если хочешь логотип
    num1 = float(input("What is the first number?: "))

    should_accumulate = True

    while should_accumulate:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))

        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(
            f"Type 'y' to continue calculations with {answer}, or 'n' to start new, or 'q' to quit: "
        )

        if choice == "y":
            num1 = answer
        elif choice == "n":
            calculator()  # начинаем заново
            return
        else:
            should_accumulate = False
            print("Goodbye!")

# Start the calculator
calculator()
