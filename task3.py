print("Karina Batura, IT-31")

first = float(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /, //, %, **): ")
second = float(input("Enter second number: "))

if operation == "+":
    result = first + second
elif operation == "-":
    result = first - second
elif operation == "*":
    result = first * second
elif operation == "/":
    if second == 0:
        result = None
        print("Error: division by zero")
    else:
        result = first / second
elif operation == "//":
    if second == 0:
        result = None
        print("Error: division by zero")
    else:
        result = first // second
elif operation == "%":
    if second == 0:
        result = None
        print("Error: division by zero")
    else:
        result = first % second
elif operation == "**":
    result = first ** second
else:
    result = None
    print(f"Error: unknown operation '{operation}'")

if result is not None:
    print(f"{first} {operation} {second} = {result:.4f}")