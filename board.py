from move import *
from dataclasses import dataclass

EMPTY = 0
WHITE = 1
BLACK = 2

@dataclass
class Board:
    board: list[list[int]]
    player: int

def _row(pos: int) -> int:
    """Row corresponding to pos."""
    return (pos-1)//5

def _col(pos:int) -> int:
    """Column corresponding to pos."""
    return (pos-1)%5

def make_board() -> Board:
    """Creates a new Alquerque board with all pieces in their starting
        positions.
    """
    b = [[ BLACK
           if i <= 1 or (i == 2 and j <= 1)
           else EMPTY if i == j == 2
           else WHITE
           for j in range(5)] for i in range(5)]
    return Board(b,WHITE)

def white_plays(b: Board) -> bool:
    """Returns whether it is white's turn."""
    return b.player == WHITE

def _other(b: Board) -> bool:
    """The other player."""
    return 3-b.player

def _find(b: Board, v: int) -> list[int]:
    """Returns a list with all the positions containing v."""
    return list(
        filter(lambda x: x != 0,
               map(lambda i: i if b.board[_row(i)][_col(i)] == v else 0,
                   range(1,26))))

def white(b: Board) -> list[int]:
    """Returns a list with all the positions containing white pieces in b."""
    return _find(b,WHITE)

def black(b: Board) -> list[int]:
    """Returns a list with all the positions containing white pieces in b."""
    return _find(b,BLACK)

def _in_board(pos: int) -> bool:
    """Checks whether a given position is within the board limits."""
    return 1 <= pos <= 25

def _legal_even(m: Move, b: Board) -> bool:
    """Checks whether a move with legal source from an even, non-empty square
        is legal.
    """
    sx = _row(source(m))
    sy = _col(source(m))
    tx = _row(target(m))
    ty = _col(target(m))
    if (target(m) == source(m)-5 and
        b.board[sx][sy] == WHITE and
        b.board[tx][ty] == EMPTY): # white moves up
        return True
    elif (target(m) == source(m)+5 and
          b.board[sx][sy] == BLACK and
          b.board[tx][ty] == EMPTY): # black moves down
        return True
    else: # catching move
        return (((abs(tx-sx) == 2 and ty == sy) or
                 (tx == sx and abs(ty-sy) == 2)) and
                b.board[(tx+sx)//2][(ty+sy)//2] == _other(b))

def _legal_odd(m: Move, b: Board) -> bool:
    """Checks whether a move with legal source from an odd, non-empty square
        is legal.
    """
    sx = _row(source(m))
    sy = _col(source(m))
    tx = _row(target(m))
    ty = _col(target(m))
    if (tx == sx-1 and abs(ty-sy) <= 1 and
        b.board[sx][sy] == WHITE and
        b.board[tx][ty] == EMPTY): # white moves up
        return True
    elif (tx == sx+1 and abs(ty-sy) <= 1 and
          b.board[sx][sy] == BLACK and
          b.board[tx][ty] == EMPTY): # black moves down
        return True
    else: # catching move
        return (((abs(tx-sx) == 2 and ty == sy) or
                 (tx == sx and abs(ty-sy) == 2) or
                 (abs(tx-sx) == abs(ty-sy) == 2)) and
                b.board[(tx+sx)//2][(ty+sy)//2] == _other(b))

def is_legal(m: Move, b: Board) -> bool:
    """Checks whether a given move is legal in a given board state."""
    return (_in_board(source(m)) and
            _in_board(target(m)) and
            b.board[_row(source(m))][_col(source(m))] == b.player and
            b.board[_row(target(m))][_col(target(m))] == EMPTY and
            ((source(m)%2 == 0 and _legal_even(m,b)) or
             (source(m)%2 == 1 and _legal_odd(m,b))))

def legal_moves(b: Board) -> bool:
    """Returns a list with all the legal moves from the given board state."""
    if b.player == WHITE:
        sources = white(b)
    else:
        sources = black(b)
    moves = []
    for s in sources:
        targets = filter(lambda t: is_legal(make_move(s,t),b),
                         range(1,26))
        for t in targets:
            moves.append(make_move(s,t))
    return moves

def move(m: Move, b: Board) -> None:
    """Performs a given move. Requires is_legal(m)."""
    sx = _row(source(m))
    sy = _col(source(m))
    tx = _row(target(m))
    ty = _col(target(m))
    # update the piece's position
    b.board[sx][sy] = EMPTY
    b.board[tx][ty] = b.player
    # remove piece jumped over
    if abs(sx-tx) > 1 or abs(sy-ty) > 1:
        b.board[(sx+tx)//2][(sy+ty)//2] = EMPTY
    # switch between WHITE (1) and BLACK (2)
    b.player = _other(b)

def is_game_over(b: Board) -> bool:
    """Checks whether the game is over."""
    return legal_moves(b) == []

def copy(b: Board) -> Board:
    """Returns a deep copy of b."""
    new_board = [[ b.board[i][j] for j in range(5)] for i in range(5)]
    return Board(new_board,b.player)
