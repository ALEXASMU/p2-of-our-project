Move = (int,int)

def make_move(src: int, trg: int) -> Move:
    """Creates a new move in Alquerque between the two given squares."""
    return (src, trg)

def source(m: Move) -> int:
    """Returns the source of a given move.
    >>> source(make_move(15,22))
    15
    """
    return m[0]

def target(m: Move) -> int:
    """Returns the target of a given move.
    >>> target(make_move(15,22))
    22
    """
    return m[1]
