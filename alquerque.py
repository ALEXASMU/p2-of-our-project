from board import *
from move import *
from minimax import *

def start_game():
    """
    Determines wether or not a player is a bot
    start_game()
    Should Player 1 be a bot?: Yes
    Should Player 2 be a bot?: Yes
    >>>Player 1 is a bot and so is Player 2
    """
    print("""
    WELCOME TO ALQUERQUE!!!

    """)
    print("Player 1 is white and Player 2 is black, this is important because white starts")

    player1 = input("Should Player 1 be a bot? (Yes/No): ")
    player2 = input("Should Player 2 be a bot? (Yes/No): ")
#This section can be used to return a bool value that determines human and bot players
    if player1 == "Yes" and player2 == "No":
        return('Player 1 is a bot, and Player 2 is a human player')
    elif player1 == "No" and player2 == "Yes":
        return('Player 1 is a human player, and Player 2 is a bot')
    elif player1 == "Yes" and player2 == "Yes":
        return('Player 1 is a bot and so is Player 2')
    elif player1 == "No" and player2 == "No":
        return('both Player 1 & 2 are human players')
    else:
        return('Pick either yes or no')
   
