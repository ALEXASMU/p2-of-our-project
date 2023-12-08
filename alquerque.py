from board import *
from move import *
from minimax import *
from dataclasses import dataclass
def start_game():
    return start_menu()
def start_menu():
    """
    initializes the game by telling the player to pick 1 out of 4 options
    >>> start_game()
    WELCOME TO ALQUERQUE!!!
    
    Player 1 starts
    type 1 to play against a human
    type 2 to play against a bot as white
    type 3 to play against a bot as black
    type 4 to see two bots play
    : 4
    You chose to watch a match between 2 bots
    """
    print("""
    WELCOME TO ALQUERQUE!!!
    """)
    print("Player 1 starts")
    print("type 1 to play against a human")
    print("type 2 to play against a bot as white")
    print("type 3 to play against a bot as black")
    print("type 4 to see two bots play")
    global game_type
    game_type = int(input(": "))
    match game_type:
            case 1:
                print("You chose to play against a human")
            case 2:
                print("You chose to play against a bot as white")
            case 3:
                print("You chose to play against a bot as black")
            case 4:
                print("You chose to watch a match between 2 bots")
            case _:
                print("Please select any number 1-4")

