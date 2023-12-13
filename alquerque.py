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

def game_state(b: Board) -> None:
    """Checks wether game over,
       calls player_turn or game_over.
    """
    if is_game_over
        game_over
    else:
        player_turn(b)
            
def player_turn(b: Board) -> None:
    """Either plays for White or Black,
       using distinct process flow for human/ vs bot play.
    """
    if white_plays:
        print('White is playing.')
        if game_type == 3 or game_type = 4:
            bot_play(b)
        else:
            human_player(b)
    else:
        print('Black is playing.')
        if game_type == 2 or game_type = 4:
            bot_play(b)
        else:
            human_player(b)

def bot_play(b: Board) -> None:
    """Bot makes move and informs about move.
    """
    ne = next_move(b)
    move(ne, b)
    print(f"Bot has moved {_coordinates_move(ne)}")
    Board_Composer(b)
        
def human_player(b: Board) -> None:
    """asks human player to make move,
       input is xy-xy
       if incorrect input, calls itself again
       if correct, effects a move on the board
    """
    print('Please make a move. Input for coordinates is format "a1".')
    print('Please select a piece to move.')
    source = input('')
    print(f'You selected {source}, now choose where to move it')
    target = _translatetoint(input(''))
    source = _translatetoint(source)
    move = (source, target)
    if is_legal(move, b)
        Move(move, b)
        Board_Composer(b)
    else:
        print('Wrong input, please try again!')
        human_player(b)

def _coordinates_move(m: Move) -> str:
    """Returns string describing board coordinates
       for a specific move.
    """
    statement = f'{_translatetostr(m[0])}' + ' to ' + f'{_translatetostr(m[1])}'
    return statement

def _translatetostr(a: int) -> str:
    ans = ''
    ans = ans + [['a' if a % 5 == 1
                 else 'b' if a % 5 == 2
                 else 'c' if a % 5 == 3
                 else 'd' if a % 5 == 4
                 else 'e' if a % 5 == 0]
                ['1' if a >= 21
                 else '2' if 16 <= a <= 20
                 else '3' if 11 <= a <= 15
                 else '4' if 6 <= a <= 10
                 else '5' if 1 <= a <= 5]]
    return ans

def _translatetoint(a: str) -> int:
    x = (ord(a[0]) - 96)
    y = (5 - a[1])
    return (x + y * 5)
    




def _piece_draw(color: str) -> str:
    return "x" if color == "black" else "O" if color == "white" else "H"

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

