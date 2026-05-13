import numpy as np 
import scripts
#players = int(input("How many players are you playing with? (2-3): "))

scripts.turn()    



    
#dice scenarios
elif dice_rolls[0] == dice_rolls [1]:
    print ("Dice 1 and Dice 2 are fixed, would you like to roll dice 3 again? (y/n): ")
    
elif dice_rolls[1] == dice_rolls [2]:
    print ("Dice 2 and Dice 3 are fixed would you like to roll dice 1 again? (y/n): ")

elif dice_rolls[0] == dice_rolls [2]:
    print ("Dice 1 and Dice 3 are fixed, would you like to roll dice 2 again? (y/n): ")

else: 
    print("No matching dice, would you like to roll again? (y/n): ")

