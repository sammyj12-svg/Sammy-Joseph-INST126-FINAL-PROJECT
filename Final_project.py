#Imports seperate module 
import scripts
#Assigns players scores at beginning of game
player1_score = 0
player2_score = 0
#Parameters loop 
while True:

    try:
        #Asks the user what score they want to play to and allows the user to enter only an integer
        win_condition = int(input("What score do you want to play to? (20-50)"))
        #Makes sure the user enters a number within the range
        if win_condition > 50 or win_condition < 20:
            print("Please enter a number between (20-50)")
        #Breaks out of the parameters loop once win_condition is entered
        else: 
            break
    # Catches an error if the user enters something that is not a number
    except ValueError: 
        print ("Please enter a number")

    
#Game loop 
while player1_score < win_condition and player2_score < win_condition:
   
    #Player 1 turn: 
    print ("Player 1 turn:")
    #Calls the turn function and assigns it to turn_score 
    turn_score = scripts.turn()  
    #Adds the turn_score to player1_score  
    player1_score += turn_score
    print("Player 1's current score is:", player1_score)
    
    #win_condition for player 1
    if player1_score >= win_condition: 
        print("game over, player 1 wins!!!")
        break

    #Player 2 turn: 
    print ("Player 2 turn:")
    #Calls the turn function and assigns it to turn_score 
    turn_score = scripts.turn()   
    #Adds the turn_score to player2_score  
    player2_score += turn_score
    print("Player 2's current score is:", player2_score)

    #win_condition for player 2
    if player2_score >= win_condition: 
        print("game over, player 2 wins!!!")
        break

players = [player1_score, player2_score]
scores = {"Player 1": player1_score, 
          "Player 2": player2_score
}

with open("Tuple_scores.txt", mode="a") as write_connection:
    write_connection.write("\n-----------------\n")
    write_connection.write("Game Result:\n")
    write_connection.write(f"Player 1: {player1_score}, Player 2: {player2_score}\n")

    write_connection.write(f"List format: {players}\n")
    write_connection.write(f"Dictionary format: {scores}\n")
    write_connection.write("-----------------")

    
with open("Tuple_scores.txt", mode="r") as read_connection:
    print(read_connection.read())






    







