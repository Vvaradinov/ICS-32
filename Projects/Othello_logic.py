# 32979197 Vladislav Varadinov

import collections
import Othello_ui

NONE = "."
WHITE = "W"
BLACK = "B"
"""
class GameLogic():

    The main game logic class
    consisting of all the
    logical methods
    """
def insert_check(board:list,selection:list):
    """
    Checks if the insertion we make
    is legal- meaning is the spot free
    to put a new a chip or is there a chip already there
    """
    while True:
        row_num = selection[0] - 1
        column_num = selection[1] -1
        if board[row_num][column_num] == WHITE or board[row_num][column_num] == BLACK:
            print("INVALID")
        elif board[row_num][column_num] == NONE:
            board[row_num][column_num] = WHITE
            print(board)

























































def _othello_board_(INPUTS:list):
    """
    Makes an othello board that is a 2D list
    depending on the ROW and COL input
    """
    board = []
    for obj in range(INPUTS[0]):
        board.append([])
        for obj1 in range(INPUTS[1]):
            board[obj].append(NONE)

    return board

def _player_turn(selection:str): # still under construction
    """                          # might not work
    Keeps track of who's turn
    it is at any given time
    during the game play
    """
    state = " "
    if selection[0] == BLACK:
        state = BLACK
    elif selection[0] == WHITE:
        state = WHITE
    print(state)

def _initial_four_chips_(board: list,selection: str):
    """
    Inserts the initial 4 chips into the
    middle of the board depending on the
    columns and rows that the user gives
    """
    row_num = int(len(board)/2)
    column_num = int(len(board[0])/2)
    #print([row_num-1,column_num-1],[row_num-1,column_num],[row_num,column_num-1],[row_num,column_num])
    board[row_num-1][column_num-1] = NONE
    if selection[1] == BLACK:
        board[row_num-1][column_num-1] = BLACK
        board[row_num-1][column_num] = WHITE
        board[row_num][column_num-1] = WHITE
        board[row_num][column_num] = BLACK
    else:
        board[row_num-1][column_num-1] = WHITE
        board[row_num-1][column_num] = BLACK
        board[row_num][column_num-1] = BLACK
        board[row_num][column_num] = WHITE
    return board

#print(_initial_four_chips_(_othello_board_(4,4),"B"))

def _visual_othello_board_(board: list):
    """
    Makes a visual board
    suitable for game play
    """
    for obj in board:
        for obj1 in obj:
            print(obj1,end="")
        print()

def count_of_chips(board:list):
    """
    """
    count_black = 0
    count_white = 0
    for obj in board:
        for num in obj:
            if num == BLACK:
                count_black += 1
            elif num == WHITE:
                count_white += 1
    print("B:",count_black, "W:",count_white)
while True:
    (insert_check(_othello_board_([4,4]),Othello_ui.insert_input()))
