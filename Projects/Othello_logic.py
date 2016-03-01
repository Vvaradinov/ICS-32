# 32979197 Vladislav Varadinov

import collections


NONE = "."
WHITE = "W"
BLACK = "B"



class GameLogic():
    def __init__(self,board:list,turn:str,selection:[int]):
        self._board = board
        self._selection = selection
        self._turn = turn
        """
    def player_move(self):

        get the player input check if it's valid
        print the entire UI
        call list and get user input and check if it's valid move
        after that update the update the board and turn

        self.turn = player_turn(self.turn)
        """


    def insert_check(self):
        """
        Checks if the insertion we make
        is legal- meaning is the spot free
        to put a new a chip or is there a chip already there
        """

        row_num = self._selection[0] -1
        column_num = self._selection[1] -1
        current_turn = self._turn
        while True:
            if self._board[row_num][column_num] == NONE:
                print("Valid")
                self._board[row_num][column_num] = current_turn
                return self._board
            elif self._board[row_num][column_num] == WHITE or self._board[row_num][column_num] == BLACK:
                print("Invalid")
                return False


    def vertical_check(self):
        """
        Checks the spot we are trying to put in on a vertical scale,
        if the spot is empty --> check if the vertical line,
        if it's the opposite color --> continue until you
        find your color that is nearest to the spot
        you are trying to put in and change everything
        in between to your color!!
        """
        row_num = self._selection[0] - 1
        column_num = self._selection[1] - 1
        current_turn = self._turn

        while True:
            count = 1
            for obj in self._board[column_num]:
                if self._board[row_num+count][column_num] == player_turn(current_turn):
                    self._board[row_num+count][column_num] = current_turn
                    count += 1
            for obj in self._board[column_num]:
                if self._board[row_num-count][column_num] == player_turn(current_turn):
                    self._board[row_num-count][column_num] = current_turn
                    count += 1

            break


    def horizontal_check(self):
        """
        """
        row_num = self._selection[0] - 1
        column_num = self._selection[1] -1
        current_turn = self._turn

        while True:
            count = 1
            for obj in self._board[row_num]:
                if self._board[row_num][column_num+count] == player_turn(current_turn):
                    self._board[row_num][column_num+count] = current_turn
                    count+=1
            for obj in self._board[row_num]:
                if self._board[row_num][column_num-count] == player_turn(current_turn):
                    self._board[row_num][column_num-count] = current_turn
                    count +=1
            break




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


