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
import os


os.system('clear')
answer = randint(10,100)
tries = 0
highscore = None
prevGueses = []
while True:

    if tries == 0:
        print("\033[32mHigh / Low Guessing Game \033[0m")
        print("I have thought of a number between \033[32m1\033[0m and \033[32m100\033[0m!")

        
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
            print ("Your Guess was \033[34mtoo low\033[0m. Please Try again.")
        else:
            print ("Your Guess was \033[31mtoo high\033[0m. Please Try again.")
        print ("\nNumber of Tries = ", tries)
        print ("Your Previous Gueses: ", end="")
        for i, displayGuesses in enumerate(prevGueses):
            if displayGuesses < answer:
                print("\033[34m", end="")
            else:
                print("\033[31m", end="")

           
            if i == 0:
                print(displayGuesses, end="")
            elif i < len(prevGueses)-1:
                print(",",displayGuesses, end = ",")
            else:
                print("",displayGuesses, end="")
        print("\033[0m")

    else:
        print ("\n\033[35mYou guessed it!\033[0m")
        print ("Number of Tries =\033[32m", tries,"\033[0m")

        if highscore == None:
            highscore = tries           
        else:
            if tries < highscore:  
                highscore = tries
                print("NEW HIGH SCORE =", highscore, "!!!")
            else:
                print("Current High Score:", highscore)

        
        while True:
            replay = input("Would you like to play again (y/n)? ")
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