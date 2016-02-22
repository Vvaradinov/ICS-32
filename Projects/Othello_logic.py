# 32979197 Vladislav Varadinov

import collections

NONE = 0
WHITE = 1
BLACK = 2

































































def _initial_four_chips_(board: list):
    """
    Inserts the initial 4 chips into the
    middle of the board depending on the
    columns and rows that the user gives
    """
    column_num = int(len(board)/2)
    row_num = int(len(board[0])/2)
    return [[column_num, row_num],[column_num -1, row_num],[column_num, row_num -1],[column_num -1, row_num -1]]


def _othello_board_(COL: int, ROW: int):
    """
    Makes an othello board that is a 2D list
    depending on the ROW and COL input
    """
    board = [["."] * ROW] * COL
    return board

def _visual_othello_board_(board: list):
    """
    Makes a visual board
    suitable for game play
    """
    for obj in board:
        for obj1 in obj:
            print(obj1,end="")
        print()

