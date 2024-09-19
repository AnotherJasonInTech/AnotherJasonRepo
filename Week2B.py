'''
2.	Challenge 2: Simple Calculator
Create a simple calculator program that asks the user for two 
numbers and a mathematical operation (+, -, *, /). It should then 
output the result of that operation on the two numbers.

'''

number1 = None
number2 = None
operation = None
divRemainder = None
remainder = None
answer = None


number1 = input("Enter First Number: ")
number2 = input("Enter Second Number: ")

try:
    number1 = int(number1)
    number2 = int(number2)
except:
    print("An Error Occured")

print("Enter Operation from list below")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation = input("Choose from list: ")

if operation == "1":
    answer = number1 + number2
    operation = "plus"
elif operation == "2":
    answer = number1 - number2 
    operation = "minus"
elif operation == "3":
    answer = number1 * number2 
    operation = "multiplied by"

elif operation == "4":
    divRemainder = input("Did you want a remainder (y/n)? ")
    if divRemainder == 'y':
        answer = number1 / number2
        remainder = number1 % number2
        operation = "divided by"

    if divRemainder == 'n':
        answer = number1 / number2
        remainder = None

print(number1, operation, number2, "equals", answer, end="")
if remainder != None:
    print("with a remainder of", remainder)
