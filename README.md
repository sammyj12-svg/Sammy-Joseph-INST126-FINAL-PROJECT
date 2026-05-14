#Tuple out dice game 

##Game rules 
-This program runs a two-player dice game 
-Players take turns rolling three dice and both try to reach the target score before the other player. 

-At the beginning, users choose a target score between 20 and 50 to play to. 

-Players alternate rolling the three dice each turn 

-After each turn the three dice numbers will count toward each players score. 

-During a player's turn they can roll as many times as they want unless 3 numbers match (tuple out) or if the player chooses to stop rolling 

-If a player rolls two of the same number, those dice are fixed and cannot be rolled again 

-If a player chooses to re-roll after getting fixed dice, they can only roll the non-fixed dice 

##Functions 
-roll_dice() --> rolls and returns three random dice 
-turn() --> handles the logic for a single player's turn 