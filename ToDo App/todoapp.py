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
    try:
        command = userInput[0]
        # Move the rest of input back to a variable and join it together. 
        task = userInput
        del task[0]
        task = " ".join(task)

        # return the command and string separately.
        return str(command).upper(), task.capitalize()
    except:
        return int(-1), int(-1)

# Try to open to JSON file, If you can, create a new one.
try: 
    with open('ToDo App/tasksDB.json', 'r') as json_file:
        database = json.load(json_file)
except: 
    with open('ToDo App/tasksDB.json', 'w') as json_file:
        json_file.write('')
        database = []
clear_screen()

print("Welcome to the Task Manager")

# Main Loop
while True:
    # Print Commands Prompt
    print("\n\nCOMMANDS:")
    print("ADD | UPDATE | DELETE | LIST | MARK | EXIT | HELP\n")
    userInput = input("Enter a Command:")
    
    # After input, Clar the screen to display results 
    clear_screen()
    
    # Try Except for splitting task into commnd / task pair
    try:
        command, task = parseInput(userInput)
    except:
        # Generic exeption prompt, could be more descriptive.
        print ("An error Has Occured")
        continue

    if command == "ADD":
        # Check to see task value
        if task == "":
            print("Task was Empty")
            print("""ADD: Add a new task to the list. - ADD [ Task ]
Example: ADD Learn Task Manager commands. """)
            print("Please refer to the HELP command to learn ADD functionality.")
        else:
            # Add Task to String for JSON Update
            newEntry = {"task":task,"createddate":datetime.now().strftime("%m.%d.%y %H:%M:%S"),"status": "Not Started", "completeddate": None}
            database.append(newEntry)
            print ("ADDED:", newEntry["task"],"|", "Created:",  newEntry["createddate"])
        
    if command == "UPDATE":
        # Split into Task Number / Task Pair. Uses same fucntion
        item, updatedTask = parseInput(task)
        try:
            int(item)
        except:
            # Throw a negative number into task so it can trigger and error
            item = -1
        if item == -1 or int(item) > len(database):
            print("Task Number not found")
            print("Please refer to the HELP command to learn UPDATE functionality.")
            print("""UPDATE: Update a task details - UPDATE [ Task Number ] [ Updated Task ] 
Example: UPDATE 1 Go through HELP section of Task Manager to learn Commands.
              """)

            continue
        # Catch if task was empty
        if updatedTask == "":
            print("No Task Entered")
            print("Please refer to the HELP command to learn UPDATE functionality.")
            print("""UPDATE: Update a task details - UPDATE [ Task Number ] [ Updated Task ] 
Example: UPDATE 1 Go through HELP section of Task Manager to learn Commands.
              """)
            continue
        # Add Task to String for JSON Update
        else:
                oldTask = database[int(item)-1]["task"]
                database[int(item)-1]["task"] = updatedTask
                print ("UPDATED TASK ", item, ":",oldTask, "->", database[int(item)-1]["task"] )
    if command == "DELETE":
        # Try / Except to assign input to int. If failed advised inccorect imput. 
        try:
            # Check to determine if task number is higher than list index 
            delTaskNumber = int(task)-1
            if delTaskNumber > len(database)-1 or delTaskNumber < 0:
                print("Task Number not found")
                print("Please refer to the HELP command to learn DELETE functionality.")
                print("""DELETE: Delete a task - DELETE [ Task Number ]
Example: DELETE 1""")
                continue
        except: 
            print("Invalid Task Number")
            print("""DELETE: Delete a task - DELETE [ Task Number ]
Example: DELETE 1""")
            print("Please refer to the HELP command to learn DELETE functionality.")
            continue
        # Remember deleted task to print
        deleted = database[delTaskNumber]
        # Delete task
        del database[delTaskNumber]
        print ("DELETED:", deleted["task"],"|", "Created:",  deleted["createddate"])


    elif command == "LIST":
        # Check to see if there is anything in database
        if len(database) == 0:
            print ("No Tasks Available")
            continue

        # Check for list option
        task = task.title()
        options = ["All","Not Started", "Started", "Completed"]
        if task in options:
            # display a [ ], [S] or [X], depending on status
            for index, entry in enumerate(database):
                if entry["status"] == "Not Started":
                    checkmark = "[ ]"
                elif entry["status"] == "Started":
                    checkmark = "[S]"
                elif entry["status"] == "Completed":
                    checkmark = "[X]"
                # Display list of task based on option
                if task == "All" or task == entry["status"]:
                    print (f"{index + 1:<3}-", checkmark, entry["task"], end="")
                    
                    # Determins which date to show (created, started or completed)
                    if entry["status"] == "Not Started":
                        print (" | Created:",entry["createddate"])
                    
                    if entry["status"] == "Started":
                        print (" | Started:",entry["starteddate"])
                    if entry["status"] == "Completed":
                        print (" | Completed:",entry["completeddate"])                  
        else:
            print("Invalid LIST Command ")
            print("""LIST: List tasks in a certain status (Status: ALL, NOT STARTED, STARTED, COMPLETED) - LIST [ Status ]
Example: LIST Not Started""")
            print("Please refer to the HELP command to learn LIST functionality.")
            continue   
    
    elif command == "MARK":
        # Split the task / mark option
        item, taskStatus = parseInput(task)
        # Try execpt to determine if the task number is an int
        try:
            int(item)
        
        except:
            #Assign a -1 to throw an error later
            item = -1
        if item == -1 or int(item) > len(database) or taskStatus == "":
            print("Task not found")
            print("MARK: Assign a Status to a task (Status: ALL, NOT STARTED, STARTED, COMPLETED) - Mark [ Task Number ] [ Status ]")
            print("Please refer to the HELP command to learn MARK functionality.")
            

            continue
        else:
            taskStatus = taskStatus.title()
        if taskStatus in ["Not Started", "Started", "Completed"]:
            # Keep old status to display 
            oldStatus = database[int(item)-1]["status"]
            database[int(item)-1]["status"] = taskStatus
            print ("UPDATED STATUS", item ,database[int(item)-1]["task"], ":", oldStatus, "->", database[int(item)-1]["status"])
            #Assign a new timestamp to the started / created / completed entry in JSON 
            if taskStatus == "Started":
                database[int(item)-1]["starteddate"] = datetime.now().strftime("%m.%d.%y %H:%M:%S")
                database[int(item)-1]["completeddate"] = None
            if taskStatus == "Completed":
                database[int(item)-1]["starteddate"] = None
                database[int(item)-1]["completeddate"] = datetime.now().strftime("%m.%d.%y %H:%M:%S")
        else: 
            print("Invalid Status Entered")
            print("""MARK: Assign a Status to a task (Status: ALL, NOT STARTED, STARTED, COMPLETED) - Mark [ Task Number ] [ Status ]
Example: Mark 1 Completed""")
            print("Please refer to the HELP command to learn MARK functionality.")
            continue


    elif command == "EXIT":
        break
    elif command == "HELP":
        print("Here is the Help Section")
        print("\n\nCommands:")
        print("""  
ADD: Add a new task to the list. - ADD [ Task ]
Example: ADD Learn Task Manager commands. 

UPDATE: Update a task details - UPDATE [ Task Number ] [ Updated Task ] 
Example: UPDATE 1 Go through HELP section of Task Manager to learn Commands.
              
DELETE: Delete a task - DELETE [ Task Number ]
Example: DELETE 1

LIST: List tasks in a certain status (Status: ALL, NOT STARTED, STARTED, COMPLETED) - LIST [ Status ]
Example: LIST Not Started
              
MARK: Assign a Status to a task (Status: ALL, NOT STARTED, STARTED, COMPLETED) - Mark [ Task Number ] [ Status ]
Example: Mark 1 Completed
              
EXIT: Quit the Program
Example: EXIT

HELP: Show Help Menu (This Guide)
Example: HELP
""")

    
    else:
        print("Invalid Command")
        print("Please refer to the HELP command to learn xcommands and functionality.")

    

    
    # At the end of the loop, update the JSON File.
    with open('ToDo App/tasksDB.json', 'w') as json_file:
        json.dump(database, json_file, indent=4)