'''
ChatGPT Prompt
Week 1 (Sept 9-15)
Project: Number Guessing Game
Create a command-line game where the computer randomly 
selects a number between 1 and 100. The player has to 
guess the number, and the program provides feedback such as 
“too high” or “too low.” Allow for multiple guesses and display 
the total attempts.
'''
from random import randint
import os, shutil
cWidth = shutil.get_terminal_size().columns

def rainbow_text(text):
    colors = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m']
    bgcolors = ['\033[41m', '\033[42m', '\033[43m', '\033[44m', '\033[45m', '\033[46m']

    reset = '\033[0m'
    randFG = 0
    randBG = 0
    for i, char in enumerate(text):
        if char == " ":
            print(reset + char, end="")
            randFG = randint(0,len(colors)-1)
            randBG = randint(0,len(bgcolors)-1)
            continue
        print(colors[randFG] + bgcolors[randBG] + char, end="")
    
    print(reset, end="")  # Reset color after the loop

def titleMaker(message, cWidth, fgcolor, bgcolor):

    cenDigit = len(message)
    i = 0
    fgcolor = str("\033["+ str(fgcolor) +"m")
    bgcolor = str("\033["+ str(bgcolor) +"m")
    while i < cWidth:
        if message == "none":
            print ("*", end="")
            i += 1
        else:    
            if i == int(cWidth / 2) - (int(cenDigit/2)+2):
                print(fgcolor,bgcolor, end="")
                print("", message, end=" \033[0m ")
                i = i + cenDigit + 4
            else:
                print ("*", end="")
                i += 1
    print("")

#initialize the Game
os.system('clear')
answer = randint(10,100)
tries = 0
highscore = None
prevGueses = []

#game loop
while True:

    if tries == 0:
        titleMaker("High / Low Guessing Game", cWidth, randint(90,98), randint(40,48))
        titleMaker("I have thought of a number between 1 and 100!", cWidth, randint(90,98),randint(40,48))
        
    guess = input("What is your guess: ")
    
    try:
        guess = int(guess)
        prevGueses.append(guess)
    except ValueError:
        print("That was not a number, Please Try again.")
        continue
    
    tries += 1

    if guess != answer:
        if guess < answer:
            print ("\nYour Guess was \033[34mtoo low\033[0m. Please Try again.")
        else:
            print ("\nYour Guess was \033[31mtoo high\033[0m. Please Try again.")
        print ("Number of Tries = ", tries)
        print ("Your Previous Gueses: ", end="")
        for i, displayGuesses in enumerate(prevGueses):
            if displayGuesses < answer:
                print("\033[34m", end="(L)")
            elif displayGuesses > answer:
                print("\033[31m", end="(H)")

           
            #if i == 0:
            #    print(displayGuesses, end="")
            if i < len(prevGueses)-1:
                print(displayGuesses, end = "\033[0m, ")
            else:
                print(displayGuesses, end="\033[0m")
        print("\n")

    else:
        print ("\n\033[35mYou guessed it!\033[0m")
        print ("Number of Tries =\033[32m", tries,"\033[0m")

        if highscore == None:
            highscore = tries
            print("\033[33mHIGH SCORE =",highscore, end="\033[m" )           
        else:
            if tries < highscore:  
                highscore = tries
                rainbow_text("NEW HIGH SCORE")
                print (" =", highscore, end="")           
            else:
                print("Current High Score:", highscore)

        
        while True:
            replay = input("\nWould you like to play again (y/n)? ")
            if replay == "y":
                exit = False
                tries = 0
                answer = randint(10,100)
                prevGueses = []
                os.system('clear')
                break
            if replay == "n":
                exit = True
                break
            else:
                print("Invalid Response. Pleasy Try again.")
        
        if exit == True:
            break