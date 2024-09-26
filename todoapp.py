import json

def parseInput(userInput):

    userInput = userInput.split()

    command = userInput[0]

    task = userInput
    del task[0]
    task = " ".join(task)
    
    return str(command).upper(), task.capitalize()




database = [] 


while True:
   
    userInput = input("Enter a Command:")

    command, task = parseInput(userInput)

    if command == "ADD":
        database.append(task)

    if command == "UPDATE":
        item, updatedtask = parseInput(task)
        database[int(item)-1] = updatedtask

    if command == "LIST":
        counter = 1
        for i in database:
            
            print (counter,"-",i, end="")
            print ()
            counter += 1
 
    if command == "DELETE":
        item, updatedtask = parseInput(task)
        del database[int(item)-1]
        

    if command == "EXIT":
        break

print (database)