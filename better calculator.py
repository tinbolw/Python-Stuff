
num1 = float(input("Enter your first number: "))
operator = input("What do you want to do?")
num2 = float(input("Enter your second number: "))

if operator == " add"  or operator == "add" or operator == "+" or operator == " +":
    print(num1 + num2)
elif operator == " subtract" or operator == "subtract" or operator == "-" or operator == " -":
    print (num1 - num2)
elif operator == " divide" or operator == "divide" or operator == "/" or operator == " /":
    print (num1 / num2)
elif operator == " multiply" or operator == "multiply" or operator == "*" or operator == " *" or operator == "x" or operator == " x":
    print (num1 * num2)
else:
    print("Invalid operator (try add, subtract, multiply, or divide)")











