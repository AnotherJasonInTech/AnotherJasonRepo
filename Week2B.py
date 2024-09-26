'''
2.	Challenge 2: Simple Calculator
Create a simple calculator program that asks the user for two 
numbers and a mathematical operation (+, -, *, /). It should then 
output the result of that operation on the two numbers.

'''


intro = True

while True:

    number1 = None
    number2 = None
    operation = None
    divRemainder = None
    remainder = None
    answer = None
    loopAnswer = None
 

    if intro == True:
        print ("Welcome to the Console Calulator!")
        print("Pick 2 Numbers and an Operation and I will deliver Results!")
        intro = False


    number1 = input("Enter First Number: ")
    number2 = input("Enter Second Number: ")

    try:
        number1 = int(number1)
        number2 = int(number2)
    except:
        print("An Error Occured")
        continue

    print("\nEnter an Operation from list below")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    operation = input("\nChoose from list: ")

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
        operation = "divided by"
        
        if number2 == 0: 
             print(number1, operation, number2, "can not be completed as you can not divide by 0")
             continue

        
        if number1 > number2:
            divRemainder = input("Did you want a remainder (y/n)? ").lower()
        else:
            divRemainder = 'n'
        
        if divRemainder == 'y':
            answer = number1 // number2
            remainder = number1 % number2
            

        if divRemainder == 'n':
            answer = number1 / number2
            remainder = None

    else: 
        print("An Error Occurred.")
        continue
    print()
    print(number1, operation, number2, "equals", answer, end=" ")
    if remainder != None:
        print("with a remainder of", remainder)

    while True:
        loopAnswer = input("\nWould you like to try another operation? (y/n): ").lower()        
        if loopAnswer == 'n':
            print ("Thanks for Playing!")
            exit()
        if loopAnswer == 'y':
            break
        else:
            print("invalid entry, please try again")   