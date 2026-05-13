import numpy as np 
import scripts

player1_score = 0
player2_score = 0

while True:
    win_condition = int(input("What score do you want to play to? (30-50)"))
    if win_condition != int:
        print ("Please enter a numer")
        continue
    if win_condition > 50 or win_condition < 30:
        print("Please enter a number between (30-50)")
    else: 
        break

while player1_score < 50 and player2_score < 50:
    print ("Player 1 turn:")
    turn_score = scripts.turn()    
    player1_score += turn_score
    print("Player 1's current score is:", player1_score)

    if player1_score >= 50:
        print("game over, player 1 wins!!!")

    print ("Player 2 turn:")
    turn_score = scripts.turn()    
    player2_score += turn_score
    print("Player 2's current score is:", player2_score)


    if player2_score >= 50: 
        print("game over, player 2 wins!!!")






    







