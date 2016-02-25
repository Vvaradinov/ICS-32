# 32979197 Vladislav Varadinov

import collections


NONE = "."
WHITE = "W"
BLACK = "B"



class GameLogic():
    def __init__(self,board:list,turn:str):
        self._board = new_othello_board(board)
        self._turn = turn
    def player_move(self):
        """
        get the player input check if it's valid
        print the entire UI
        call list and get user input and check if it's valid move
        after that update the update the board and turn
        """
        self._turn = player_turn(self._turn)





def insert_check(board:list,selection: [int],turn:str) -> "Game Board":
    """
    Checks if the insertion we make
    is legal- meaning is the spot free
    to put a new a chip or is there a chip already there
    """
    row_num = selection[0] - 1
    column_num = selection[1] -1
    print(board[row_num  ][column_num ])
    if board[row_num][column_num] == NONE:
        board[row_num][column_num] = turn
        return board

    elif board[row_num][column_num] == WHITE or board[row_num][column_num] == BLACK:
        print("INVALID")
        return board


def vertical_check(board:list,selection: [int],turn: str):
    """
    """
    row_num = selection[0] - 1
    column_num = selection[1] - 1
    print(board[row_num][column_num])




def new_othello_board(INPUTS:list)-> [[str]]:
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

def initial_four_chips(board: list,selection: str) -> "Game Board":
    """
    Inserts the initial 4 chips into the
    middle of the board depending on the
    columns and rows that the user gives
    """
    row_num = int(len(board)/2)
    column_num = int(len(board[0])/2)

    board[row_num-1][column_num-1] = NONE
    if selection[3] == BLACK:
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



def visual_othello_board(board: list) -> "Visual Game Board":
    """
    Makes a visual board
    suitable for game play
    """
    for obj in board:
        for obj1 in obj:
            print(obj1,end="")
        print()



def player_turn(selection:str): # still under construction
    """                          # might not work
    Keeps track of who's turn
    it is at any given time
    during the game play
    """
    if selection == BLACK:
        return WHITE
    else:
        return BLACK


