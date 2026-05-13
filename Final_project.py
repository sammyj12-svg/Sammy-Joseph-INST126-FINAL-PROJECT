import numpy as np 
import scripts

player1_score = 0
player2_score = 0

while player1_score < 50 and player2_score < 50:
    scripts.roll_dice()
    turn_score = scripts.turn()    
    player1_score += turn_score

    scripts.roll_dice()
    turn_score = scripts.turn()    
    player2_score += turn_score

    if player1_score >= 50:
        print("player 1 wins")
    if player2_score >= 50: 
        print ("player 2 wins")






    







