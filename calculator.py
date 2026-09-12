num1 = float(input("Enter first number:"))
num2 = float(input("enter second number"))

operation = input("Enter the operator (+,-,*,/):")


if operation == '+':
    result = num1 + num2
elif operation =='-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
else:
    result = None


print(result )
