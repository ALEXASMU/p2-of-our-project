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
    global game_type #Using the global keyword, so it can be called anywhere
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
    while input == "ja":
        while is_game_over(b):





def piece_draw(color: str) -> str:
    return "x" if color == "black" else "O" if color == "white" else space()

def Horizontal() -> str:
    return "---"

def Vertical() -> str:
    return "| "
def space() -> str:
    return " "

def Board_Composer(b :Board) -> str:
    img = ""
    board = ["black" if x in black(b) else "white" if x in white(b) else "empty" for x in range(1,26)]
    for y in range(0,5):
        for x in range(0,5):
            img = img + piece_draw(board[x+y*5])
            if x != 4:
                img = img + Horizontal()
          
        img = img + " " + str(5 - y) + "\n" 
        if y != 4 :
            for x in range(0,5):
                img = img + Vertical()
                if x == y:
                    img = img + "\\ "
                elif x == 3-y:
                    img = img + "/ "
                elif abs(y-x) == 1 and x != 4:
                    img = img + "/ "
                elif abs(3-y-x) == 1 and x != 4:
                    img = img + "\\ "

            img = img + "\n"
    for x in range(0,5):
        img = img + chr(ord("a") + x) + "   "

    return img

