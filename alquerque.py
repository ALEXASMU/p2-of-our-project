from board import *
from move import *
from minimax import *
from dataclasses import dataclass
def start_game():
    start_menu()
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
    game_type = int(input(": ")) #Typecasting input to an int
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


def _piece_draw(color: str) -> str:
    return "x" if color == "black" else "O" if color == "white" else " "

def _Horizontal() -> str:
    return "---"

def _Vertical() -> str:
    return "| "

def Board_Composer(b :Board) -> str:
    img = ""
    board = ["black" if x in black(b) else "white" if x in white(b) else "empty" for x in range(1,26)]
    for y in range(0,5):
        for x in range(0,5):
            img = img + _piece_draw(board[x+y*5])
            if x != 4:
                img = img + _Horizontal()
          
        img = img + " " + str(5 - y) + "\n" 
        if y != 4 :
            for x in range(0,5):
                img = img + _Vertical()
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

print(Board_Composer(make_board()))

def _start_game():
    """
    Will start the game inbetween two players, if 1 bot or more, will ask to select difficulty
    """

def game_over(b:Board) -> None:
    
    print("Game Over!")
    if black(b) != [] and white(b) != []:
        print("The game ended in a draw")
        return
    elif white_plays(b):
        print("White won!")
    else:
        print("Black won!")


