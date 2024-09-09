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
print("High / Low Guessing Game")
answer = randint(10,100)
tries = 0
highscore = None

while True:
        
    guess = input("Please Guess: ")
    
    try:
        guess = int(guess)
    except ValueError:
        print("That was not a number, Please Try again.")
        continue
    
    tries += 1

    if guess != answer:
        if guess < answer:
            print ("Your Guess was too low. Please Try again.")
        else:
            print ("Your Guess was too high. Please Try again.")
        print ("Number of Tries = ", tries)
    else:
        print ("You got it!")
        print ("Number of Tries = ", tries)

        if highscore == None:
            highscore = tries           
        else:
            if tries < highscore:  
                highscore = tries
                print("NEW HIGH SCORE = ", highscore, "!!!")
            else:
                print("Current High Score: ", highscore)

        
        while True:
            replay = input("Would you like to play again? (y/n)")
            if replay == "y":
                exit = False
                tries = 0
                answer = randint(10,100)
                break
            if replay == "n":
                exit = True
                break
            else:
                print("Invalid Response. Pleasy Try again.")
        
        if exit == True:
            break