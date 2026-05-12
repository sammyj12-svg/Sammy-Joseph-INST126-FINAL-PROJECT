import numpy as np 

player_count = int(input("How many players are you playing with? (1-3): "))



dice_array = np.array ([1, 2, 3, 4, 5, 6])

dice_rolls = np.random.choice(dice_array, size = 3, replace = True)

print("Rolls:", dice_rolls)

#Checks for tuple out
if dice_rolls [0] == dice_rolls [1] == dice_rolls [2]:
    print("Tuple out")
#dice scenarios
elif dice_rolls[0] == dice_rolls [1]:
    print ("Dice 1 and Dice 2 are fixed, would you like to roll dice 3 again? (y/n): ")
    
elif dice_rolls[1] == dice_rolls [2]:
    print ("Dice 2 and Dice 3 are fixed would you like to roll dice 1 again? (y/n): ")

elif dice_rolls[0] == dice_rolls [2]:
    print ("Dice 1 and Dice 3 are fixed, would you like to roll dice 2 again? (y/n): ")

else: 
    print("No matching dice, would you like to roll again? (y/n): ")

