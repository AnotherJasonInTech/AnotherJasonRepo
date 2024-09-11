import shutil

cWidth = shutil.get_terminal_size().columns

message = input("What is your test: ")
def titleMaker(message, cWidth):

    cenDigit = len(message)
    i = 0
    while i < cWidth:
        if message == "none":
            print ("*", end="")
            i += 1
        else:    
            if i == int(cWidth / 2) - int(cenDigit/2):
                print("",message, end=" ")
                i = i + cenDigit + 4
            else:
                print ("*", end="")
                i += 1
       
       

    


titleMaker(message, cWidth)