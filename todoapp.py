import json
from datetime import datetime

def parseInput(userInput):

    userInput = userInput.split()

    command = userInput[0]

    task = userInput
    del task[0]
    task = " ".join(task)
    
    return str(command).upper(), task.capitalize()


try: 
    with open('tasksDB.json', 'r') as json_file:
        database = json.load(json_file)
except: 
    with open('tasksDB.json', 'w') as json_file:
        json_file.write('')
        database = []

while True:
    print()
    print("ADD | UPDATE | DELETE | LIST | MARK")
    userInput = input("Enter a Command:")

    command, task = parseInput(userInput)

    if command == "ADD":
        newEntry = {"task":task,"date":datetime.now().strftime("%m.%d.%y %H:%M:%S"),"completed": False}
        database.append(newEntry)
        print ("ADDED:", newEntry["task"],"|", "Created:",  newEntry["date"])
    
    if command == "UPDATE":
        item, updatedtask = parseInput(task)
        database[int(item)-1]["task"] = updatedtask

    if command == "DELETE":
        try: 
            delTaskNumber = int(task)-1
        except: 
            print("Error. Please Try again")
        deleted = database[delTaskNumber]
        del database[delTaskNumber]
        print ("DELETED:", deleted["task"],"|", "Created:",  deleted["date"])


    if command == "LIST":
        for index, entry in enumerate(database):
            if entry["completed"] == True:
                checkmark = "[X]"
            else:
                checkmark = "[ ]"
            
            print (index + 1, "-", checkmark, entry["task"],"|", "Created:",  entry["date"])
                

        continue

    if command == "MARK":
        try: 
            MarkTaskNumber = int(task)-1
        except: 
            print("Error. Please Try again")
       
        database[int(MarkTaskNumber)]["completed"] = True


    with open('tasksDB.json', 'w') as json_file:
        json.dump(database, json_file, indent=4)