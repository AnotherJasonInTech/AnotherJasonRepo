import json
from datetime import datetime
import os



def clear_screen():
    #Pulled directly forom ChatGPT
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Linux/macOS
    else:
        os.system('clear')

def parseInput(userInput):
    # Takes input and pulls first work from it. 
    # Saves first work as Command. Second Word as Task


    # Split user input into list
    userInput = userInput.split()
    
    # Save Command separately. This is also used to find the task to update.
    command = userInput[0]

    # Move the rest of input back to a variable and join it together. 
    task = userInput
    del task[0]
    task = " ".join(task)

    # return the command and string separately.
    return str(command).upper(), task.capitalize()

# Try to open to JSON file, If you can, create a new one.
try: 
    with open('tasksDB.json', 'r') as json_file:
        database = json.load(json_file)
except: 
    with open('tasksDB.json', 'w') as json_file:
        json_file.write('')
        database = []
clear_screen()


# Main Loop
while True:

    print()
    print("ADD | UPDATE | DELETE | LIST | MARK | EXIT | HELP")
    userInput = input("Enter a Command:")
    clear_screen()
    command, task = parseInput(userInput)

    if command == "ADD":
        newEntry = {"task":task,"createddate":datetime.now().strftime("%m.%d.%y %H:%M:%S"),"status": "Not Started", "completeddate": None}
        database.append(newEntry)
        print ("ADDED:", newEntry["task"],"|", "Created:",  newEntry["createddate"])
    
    if command == "UPDATE":
        item, updatedTask = parseInput(task)
        oldTask = database[int(item)-1]["task"]
        database[int(item)-1]["task"] = updatedTask
        print ("UPDATED TASK ", item, ":",oldTask, "->", database[int(item)-1]["task"] )


    if command == "DELETE":
        try: 
            delTaskNumber = int(task)-1
        except: 
            print("Error. Please Try again")
        deleted = database[delTaskNumber]
        del database[delTaskNumber]
        print ("DELETED:", deleted["task"],"|", "Created:",  deleted["createddate"])


    if command == "LIST":
        for index, entry in enumerate(database):
            if entry["status"] == "Not Started":
                checkmark = "[ ]"
            elif entry["status"] == "Started":
                checkmark = "[S]"
            elif entry["status"] == "Completed":
                checkmark = "[X]"
            
            print (index + 1, "-", checkmark, entry["task"], end="")
            if entry["status"] == "Not Started":
                print (" | Created:",entry["createddate"])
            
            if entry["status"] == "Started":
                print (" | Started:",entry["starteddate"])
            if entry["status"] == "Completed":
                print (" | Completed:",entry["completeddate"])     

    if command == "MARK":

        item, taskStatus = parseInput(task)
        taskStatus = taskStatus.title()
        if taskStatus in ["Not Started", "Started", "Completed"]:
            oldStatus = database[int(item)-1]["status"]
            database[int(item)-1]["status"] = taskStatus
            print ("UPDATED STATUS", item ,database[int(item)-1]["task"], ":", oldStatus, "->", database[int(item)-1]["status"])
            if taskStatus == "Started":
                database[int(item)-1]["starteddate"] = datetime.now().strftime("%m.%d.%y %H:%M:%S")
                database[int(item)-1]["completeddate"] = None

            
            if taskStatus == "Completed":
                database[int(item)-1]["starteddate"] = None
                database[int(item)-1]["completeddate"] = datetime.now().strftime("%m.%d.%y %H:%M:%S")
    if command == "EXIT":
        break
    if command == "HELP":
        print("Here is the Help Section")

    with open('tasksDB.json', 'w') as json_file:
        json.dump(database, json_file, indent=4)