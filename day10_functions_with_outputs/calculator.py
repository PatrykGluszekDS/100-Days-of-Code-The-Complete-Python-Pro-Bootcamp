def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

num1 = float(input("What's the first number? "))
for k in operations.keys():
    print(k)

while True:
    operation_symbol = input("Pick an operation symbol: ")
    num2 = float(input("What is the second number? "))

    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    want_to_continue = input("Do you want to continue with the previous number? (Type y/n): ")
    if want_to_continue == 'n':
        break
    elif want_to_continue == 'y':
        num1 = answer
