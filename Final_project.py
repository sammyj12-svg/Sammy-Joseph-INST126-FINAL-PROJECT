#Imports numpy and seperate module 
import numpy as np 
import scripts
#Assigns players scores at beginning of game
player1_score = 0
player2_score = 0
#Parameters loop 
while True:

    try:
        #Asks the user what score they want to play to and allows the user to enter only an integer
        win_condition = int(input("What score do you want to play to? (30-50)"))
        #Makes sure the user enters a number within the range
        if win_condition > 50 or win_condition < 30:
            print("Please enter a numbe between (30-50)")
        #Breaks out of the parameters loop once win_condition is entered
        else: 
            break
    # Catches an error if the user enters something that is not a number
    except ValueError: 
        print ("Please enter a numer")

    
#Game loop 
while player1_score < 50 and player2_score < 50:
   
    #Player 1 turn: 
    print ("Player 1 turn:")
    #Calls the turn function and assigns it to turn_score 
    turn_score = scripts.turn()  
    #Adds the turn_score to player1_score  
    player1_score += turn_score
    print("Player 1's current score is:", player1_score)
    
    #win_condition for player 1
    if player1_score >= 50:
        print("game over, player 1 wins!!!")

    #Player 2 turn: 
    print ("Player 2 turn:")
    #Calls the turn function and assigns it to turn_score 
    turn_score = scripts.turn()   
    #Adds the turn_score to player2_score  
    player2_score += turn_score
    print("Player 2's current score is:", player2_score)

    #win_condition for player 2
    if player2_score >= 50: 
        print("game over, player 2 wins!!!")






    







