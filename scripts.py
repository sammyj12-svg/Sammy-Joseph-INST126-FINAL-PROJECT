import numpy as np 
def roll_dice():
    dice_array = np.array ([1, 2, 3, 4, 5, 6])
    np.random.choice(dice_array, size = 3, replace = True)
    return np.random.choice(dice_array, size = 3, replace = True)



def turn():
    continue_turn = True 
    while continue_turn:
        dice = roll_dice()
        print("Start roll:", dice)
        if dice [0] == dice [1] == dice [2]:
            print("tuple out!: 0 points")
            return 0
        
        if dice[0] == dice [1]:
            again = input ("Dice 1 and Dice 2 are fixed, would you like to roll dice 3 again? (y/n): ")
    
        elif dice[1] == dice [2]:
            again = input ("Dice 2 and Dice 3 are fixed would you like to roll dice 1 again? (y/n): ")

        elif dice[0] == dice [2]:
            again = input ("Dice 1 and Dice 3 are fixed, would you like to roll dice 2 again? (y/n): ")

        else: 
            again = input("No matching dice, would you like to roll again? (y/n): ")
    return sum(dice)

    