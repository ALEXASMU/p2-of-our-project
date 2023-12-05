print("WELCOME TO ALQUERQUE")
print("First, run the is_human_player command to determine what players are human, it only takes boolean value")
print("After this, run the start_game() command to run the game")

def is_human_player(n: bool, b: bool)-> str:
    """Function that checks if both players are human, it takes boolean values and
    returns a string
    """
    if n == True and b == True:
        return("Both players are human")
    elif n == False and b == True:
        return("player 1 is a bot and player 2 is a human")
    elif n == True and b == False:
        return("player 1 is a human and player 2 is a bot")
    elif n == False and b == False:
        return("Both players are bots")
#This implementation should help us later too in programming the
#part where the program has to interpret what players are bots/human


