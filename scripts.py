import numpy as np 
def roll_dice():
    """
    Rolls three six_sided dice and returns their values 
    (an array of random ints between 1-6) to user 
    """
    #Possible values for dice
    dice_array = np.array ([1, 2, 3, 4, 5, 6])
    #randomly select 3 values, with replacement on 
    np.random.choice(dice_array, size = 3, replace = True)
    #return said values 
    return np.random.choice(dice_array, size = 3, replace = True)



def turn():
    """
    This function is for one player's turn during the game.
    If all 3 dice match, player will tuple out and return 0.
    If two dice match, they become fixed (if statements) and
    cannot be rolled again after during the turn. 
    Player can decicde to re-roll until they want to stop or tuple out. 
    This function returns the sum of the dice values at the end of the turn. 
    """
    #Calls roll_dice at the start of the turn 
    dice = roll_dice()
    print("Start roll:", dice)
    continue_turn = True 

    #Turn loop, keeps looping until player tuples out or decides to stop rolling
    while continue_turn:
        
        #checks for tuple out
        if dice [0] == dice [1] == dice [2]:
            print("tuple out!: 0 points")
            return 0
        #fixed dice scenarios
        if dice[0] == dice [1]:
            again = input ("Dice 1 and Dice 2 are fixed, would you like to roll dice 3 again? (y/n): ")
            if again == "y"
                dice[2] = np.random.randint(1,7)
                print(dice[0], dice[1], dice[2])
    
        elif dice[1] == dice [2]:
            again = input ("Dice 2 and Dice 3 are fixed would you like to roll dice 1 again? (y/n): ")
            if again == "y"
                dice[0] = np.random.randint(1,7)
                print(dice[0], dice[1], dice[2])

        elif dice[0] == dice [2]:
            again = input ("Dice 1 and Dice 3 are fixed, would you like to roll dice 2 again? (y/n): ")
            if again == "y"
                dice[1] = np.random.randint(1,7)
                print(dice[0], dice[1], dice[2])
        
        #Re-roll option 
        else: 
            again = input("No matching dice, would you like to roll again? (y/n): ")
            if again == "y":
                dice = roll_dice()
                print("Start roll:", dice)
        #If the player chooses to stop rolling the loop will end and the dice results will be printed 
        if again == "n":
            continue_turn = False
            print (sum(dice))
    return sum(dice)

    