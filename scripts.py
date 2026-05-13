import numpy as np 
def roll_dice():
    dice_array = np.array ([1, 2, 3, 4, 5, 6])
    np.random.choice(dice_array, size = 3, replace = True)
    return np.random.choice(dice_array, size = 3, replace = True)



def turn():
    dice = roll_dice()
    print("Start roll:", dice)
    if dice [0] == dice [1] == dice [2]:
        print("tuple out!: 0 points")
        return 0

    