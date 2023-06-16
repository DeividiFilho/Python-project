# A program to perform the 4 basic operations of mathematics.
# Only INTEGER values

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else: 
        print("Error: Division by zero.")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

if operator == '+':
    result = addition(num1, num2)
    print("Result: ", result)

elif operator == '-':
    result = subtraction(num1, num2)
    print("Result: ", result)

elif operator == '*':
    result = multiplication(num1, num2)
    print("Result: ", result)

elif operator == '/':
    result = division(num1, num2)
    if result is not None:
        print("Result: ", result)

else:
    print("Invalid operator.")