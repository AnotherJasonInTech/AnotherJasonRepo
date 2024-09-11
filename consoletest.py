import shutil

cWidth = shutil.get_terminal_size().columns

message = input("What is your test")
def titleMaker():
    cenDigit = len(message)
    i = 0
    while i < cWidth:
        if i == int(cWidth / 2) - int(cenDigit/2):
            print(" ",message, end=" ")
            i = i + cenDigit + 4
        print ("*", end="")
       
       

    


titleMaker("This is the most intearaction of have done?");