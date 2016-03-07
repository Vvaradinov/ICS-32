# 32979197 Vladislav Varadinov

NONE = "."
WHITE = "W"
BLACK = "B"

class GameLogic():
    def __init__(self,board:list,turn:str,selection:[int],win:str):
        self._board = board # the board list itself
        self._selection = selection
        self._turn = turn # the current turn
        self._win = win

    def insert_check(self):
        """
        """
        row_num = int(self._selection[0]) - 1
        column_num = int(self._selection[1]) -1
        if self._board[row_num][column_num] == NONE:
            return True
        else:
            return False


    def is_valid_move_vertical_plus(self,row_num:int,column_num:int,turn:str):
        """
        Checks if the move is valid
        And returns true or false
        """
        row_num = int(self._selection[0]) - 1
        column_num = int(self._selection[1]) -1
        count = 1
        while row_num + count < len(self._board[row_num]) and self._board[row_num + count][column_num] == player_turn(turn) and \
            self._board[row_num + count][column_num] != NONE:
            count += 1
        if row_num + count < len(self._board[row_num]) and\
            self._board[row_num+ count][column_num] == turn and \
                self._board[row_num +1][column_num] != turn:
            return True

    def is_valid_move_vertical_minus(self,row_num:int,column_num:int,turn: str):
        row_num = int(self._selection[0]) - 1
        column_num = int(self._selection[1]) -1
        count = 1
        while row_num - count >= 0 and self._board[row_num - count][column_num] == player_turn(turn) and \
            self._board[row_num - count][column_num] != NONE:
            count += 1
        if row_num - count >= 0 and self._board[row_num-count][column_num] == turn and \
            self._board[row_num -1][column_num] != turn:
            return True

    def is_valid_move_horizontal_plus(self,row_num: int,column_num: int,turn:str):
        """
        Checks if the move is valid
        And returns true or false
        """
        row_num = int(self._selection[0]) - 1
        column_num = int(self._selection[1]) -1
        count = 1
        while column_num + count < len(self._board[column_num])and\
            self._board[row_num][column_num + count] == player_turn(turn) and \
            self._board[row_num][column_num + count] != NONE:
            count += 1
        if column_num + count < len(self._board[column_num])and\
            self._board[row_num][column_num + count] == turn \
            and self._board[row_num][column_num +1] != turn:
            return True

    def is_valid_move_horizontal_minus(self,row_num:int,column_num:int,turn:str):
        row_num = int(self._selection[0]) - 1
        column_num = int(self._selection[1]) -1
        count = 1
        while column_num - count >= 0 and\
            self._board[row_num][column_num - count] == player_turn(turn) and \
            self._board[row_num][column_num - count] != NONE:
            count += 1
        if column_num - count >= 0 and\
            self._board[row_num][column_num - count] == turn and\
            self._board[row_num][column_num -1] != turn:
            return True

    def diagonal_plus_plus(self,row_num:int,column_num:int,turn:str):
        """
        """
        row_num = int(self._selection[0]) - 1
        column_num = int(self._selection[1]) -1
        count = 1
         # + 1 + 1
        while row_num + count < len(self._board[row_num]) and\
            column_num + count < len(self._board[column_num]) and \
            self._board[row_num + count][column_num + count] == player_turn(turn) and \
            self._board[row_num + count][column_num + count] != NONE:
            count += 1
        if row_num + count < len(self._board[row_num]) and\
            column_num + count < len(self._board[column_num]) and\
            self._board[row_num + count][column_num + count] == turn \
                and self._board[row_num +1][column_num +1] != turn:
            return True

    def diagonal_minus_minus(self,row_num:int,column_num:int,turn:str):
        row_num = int(self._selection[0]) - 1
        column_num = int(self._selection[1]) -1
        count = 1
        # -1 -1
        while row_num - count >= 0 and column_num - count >= 0 and\
            self._board[row_num - count][column_num - count] == player_turn(turn) and \
            self._board[row_num - count][column_num - count] != NONE:
            count += 1
        if row_num - count >= 0 and column_num - count >= 0 and \
            self._board[row_num - count][column_num - count] == turn and\
            self._board[row_num -1][column_num -1] != turn:
            return True

    def diagonal_minus_plus(self,row_num:int,column_num:int,turn:str):
        row_num = int(self._selection[0]) - 1
        column_num = int(self._selection[1]) -1
        count = 1
        # -1 + 1
        while row_num - count >= 0 and column_num + count < len(self._board[column_num]) and\
            self._board[row_num - count][column_num + count] == player_turn(turn) and \
            self._board[row_num - count][column_num + count] != NONE:
            count += 1
        if row_num - count >= 0 and column_num + count < len(self._board[column_num]) and \
            self._board[row_num - count][column_num + count] == turn and\
            self._board[row_num -1][column_num +1] != turn:
            return True

    def diagonal_plus_minus(self,row_num:int,column_num:int,turn:str):

        row_num = int(self._selection[0]) - 1
        column_num = int(self._selection[1]) -1
        count = 1
        # +1 - 1
        while row_num + count < len(self._board[row_num]) and column_num - count >= 0 and\
            self._board[row_num +count][column_num - count] == player_turn(turn) and \
            self._board[row_num + count][column_num - count] != NONE:
            count += 1
        if row_num + count < len(self._board[row_num]) and column_num - count >= 0 and \
            self._board[row_num + count][column_num - count] == turn\
                and self._board[row_num +1][column_num -1] != turn:
            return True

    def flip_vertical(self):
        """
        """
        row_num = int(self._selection[0]) - 1
        column_num = int(self._selection[1]) -1
        count = 1
        if self.is_valid_move_vertical_plus(row_num,column_num,self._turn) == True:
            self._board[row_num][column_num] = self._turn
            while row_num + count < len(self._board[row_num]) and\
                self._board[row_num + count][column_num] == player_turn(self._turn):
                self._board[row_num + count][column_num] = self._turn
                count += 1
        if self.is_valid_move_vertical_minus(row_num,column_num,self._turn) == True:
            self._board[row_num][column_num] = self._turn
            count = 1
            while row_num - count >= 0 and self._board[row_num - count][column_num] == player_turn(self._turn):
                self._board[row_num - count][column_num] = self._turn
                count +=1

    def flip_horizontal(self):
        """
        """
        row_num = int(self._selection[0]) - 1
        column_num = int(self._selection[1]) -1
        count = 1
        if self.is_valid_move_horizontal_plus(row_num,column_num,self._turn) == True:
            self._board[row_num][column_num] = self._turn
            while column_num + count < len(self._board[column_num]) and\
                self._board[row_num][column_num+ count] == player_turn(self._turn):
                self._board[row_num][column_num+ count] = self._turn
                count += 1
        if self.is_valid_move_horizontal_minus(row_num,column_num,self._turn) == True:
            self._board[row_num][column_num] = self._turn
            count = 1
            while column_num - count >= 0 and \
                self._board[row_num][column_num - count] == player_turn(self._turn):
                self._board[row_num][column_num - count] = self._turn
                count += 1

    def flip_diagonal(self):
        """
        """
        row_num = int(self._selection[0]) - 1
        column_num = int(self._selection[1]) -1
        if self.diagonal_plus_plus(row_num,column_num,self._turn) == True:
            self._board[row_num][column_num] = self._turn
            count = 1
            while row_num + count < len(self._board[row_num]) and \
                column_num + count < len(self._board[column_num]) and\
                self._board[row_num + count][column_num+ count] == player_turn(self._turn):
                self._board[row_num + count][column_num+ count] = self._turn
                count += 1
        if self.diagonal_minus_minus(row_num,column_num,self._turn) == True:
            self._board[row_num][column_num] = self._turn
            count = 1
            while row_num - count >= 0 and column_num - count >= 0 and\
                self._board[row_num - count][column_num - count] == player_turn(self._turn):
                self._board[row_num - count][column_num - count] = self._turn
                count += 1
        if self.diagonal_plus_minus(row_num,column_num,self._turn) == True:
            self._board[row_num][column_num] = self._turn
            count = 1
            while row_num + count < len(self._board[row_num]) and column_num - count >= 0\
                and self._board[row_num + count][column_num - count] == player_turn(self._turn):
                self._board[row_num + count][column_num - count] = self._turn
                count += 1
        if self.diagonal_minus_plus(row_num,column_num,self._turn) == True:
            self._board[row_num][column_num] = self._turn
            count =1
            while row_num - count >= 0 and column_num + count >= 0 and \
                self._board[row_num - count][column_num + count] == player_turn(self._turn):
                self._board[row_num- count][column_num + count] = self._turn
                count += 1

    def check_validity(self,row_num:int,column_num:int,turn: str):
        """
        """
        row_num = int(self._selection[0]) - 1
        column_num = int(self._selection[1]) -1
        horizontal = self.is_valid_move_horizontal_plus(row_num,column_num,turn)
        horizontal1 = self.is_valid_move_horizontal_minus(row_num,column_num,turn)
        vertical = self.is_valid_move_vertical_plus(row_num,column_num,turn)
        vertical1 = self.is_valid_move_vertical_minus(row_num,column_num,turn)
        diagonal1 = self.diagonal_minus_plus(row_num,column_num,turn)
        diagonal2 = self.diagonal_plus_minus(row_num,column_num,turn)
        diagonal3 = self.diagonal_plus_plus(row_num,column_num,turn)
        diagonal4 = self.diagonal_minus_minus(row_num,column_num,turn)
        if horizontal == True or horizontal1 == True or vertical == True or vertical1 == True or diagonal1 == True or diagonal2 == True or \
                diagonal3 == True or diagonal4 == True:
            return True
        else:
            return False


    def check_both_players(self):
        """
        """
        valid = False
        for row in range(len(self._board)):
            for col in range(len(self._board[0])):
                x = self.check_validity(row,col,self._turn)
                y = self.check_validity(row,col,player_turn(self._turn))
                if x == True or y == True:
                    valid = True
        return valid

    def check_one_player(self):
        """
        """
        valid = False
        for row in range(len(self._board)):
            for col in range(len(self._board[0])):
                x = self.check_validity(row,col,self._turn)
                if x == True:
                    valid = True
        return valid

def count_black(board:list):
    black = 0
    for obj in board:
        for num in obj:
            if num == BLACK:
                black += 1
    return black

def count_white(board: list):
    white = 0
    for obj in board:
        for num in obj:
            if num == WHITE:
                white += 1
    return white

def winner(board:list, win: str):
    black = count_black(board)
    white = count_white(board)
    if(win == ">"):
        if(white > black):
            winner = "White"
        elif(white == black):
            winner = "None"
        else:
            winner = "Black"
    else:
        if(white < black):
            winner = "White"
        elif(white == black):
            winner = "None"
        else:
            winner = "Black"
    print( "Winner: "+ winner)

def full_board(board: list):
    valid = False
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == NONE:
                valid = True
    return valid

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

def player_turn(selection:str):
    """
    Keeps track of who's turn
    it is at any given time
    during the game play
    """
    if selection == BLACK:
        return WHITE
    else:
        return BLACK


