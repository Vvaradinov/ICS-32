# 32979197 Vladislav Varadinov

NONE = "."
WHITE = "W"
BLACK = "B"

class GameLogic():
    def __init__(self,board:list,turn:str,win:str):
        self._board = board # the board list itself
        self._turn = turn # the current turn
        self._win = win

    def insert_check(self,selection:list):
        """
        """
        row_num = int(selection[0])
        column_num = int(selection[1])
        if self._board[row_num][column_num] == NONE:
            return True
        else:
            return False

    def is_valid_move_vertical_plus(self,selection:list):
        """
        Checks if the move is valid
        And returns true or false
        """
        row_num = int(selection[0])
        column_num = int(selection[1])
        count = 1
        while row_num + count < len(self._board) and self._board[row_num + count][column_num] == self.player_turn() and \
            self._board[row_num + count][column_num] != NONE:
            count += 1
        if row_num + count < len(self._board) and\
            self._board[row_num+ count][column_num] == self._turn and \
                self._board[row_num +1][column_num] != self._turn:
            return True

    def is_valid_move_vertical_minus(self,selection:list):
        row_num = int(selection[0])
        column_num = int(selection[1])
        count = 1
        while row_num - count >= 0 and self._board[row_num - count][column_num] == self.player_turn() and \
            self._board[row_num - count][column_num] != NONE:
            count += 1
        if row_num - count >= 0 and self._board[row_num-count][column_num] == self._turn and \
            self._board[row_num -1][column_num] != self._turn:
            return True

    def is_valid_move_horizontal_plus(self,selection:list):
        """
        Checks if the move is valid
        And returns true or false
        """
        row_num = int(selection[0])
        column_num = int(selection[1])
        count = 1
        while column_num + count < len(self._board[0])and\
            self._board[row_num][column_num + count] == self.player_turn() and \
            self._board[row_num][column_num + count] != NONE:
            count += 1
        if column_num + count < len(self._board[0])and\
            self._board[row_num][column_num + count] == self._turn \
            and self._board[row_num][column_num +1] != self._turn:
            return True

    def is_valid_move_horizontal_minus(self,selection:list):
        row_num = int(selection[0])
        column_num = int(selection[1])
        count = 1
        while column_num - count >= 0 and\
            self._board[row_num][column_num - count] == self.player_turn() and \
            self._board[row_num][column_num - count] != NONE:
            count += 1
        if column_num - count >= 0 and\
            self._board[row_num][column_num - count] == self._turn and\
            self._board[row_num][column_num -1] != self._turn:
            return True

    def diagonal_plus_plus(self,selection:list):
        """
        """
        row_num = int(selection[0])
        column_num = int(selection[1])
        count = 1
         # + 1 + 1
        while row_num + count < len(self._board) and\
            column_num + count < len(self._board[0]) and \
            self._board[row_num + count][column_num + count] == self.player_turn() and \
            self._board[row_num + count][column_num + count] != NONE:
            count += 1
        if row_num + count < len(self._board) and\
            column_num + count < len(self._board[0]) and\
            self._board[row_num + count][column_num + count] == self._turn \
                and self._board[row_num +1][column_num +1] != self._turn:
            return True

    def diagonal_minus_minus(self,selection:list):
        row_num = int(selection[0])
        column_num = int(selection[1])
        count = 1
        # -1 -1
        while row_num - count >= 0 and column_num - count >= 0 and\
            self._board[row_num - count][column_num - count] == self.player_turn()and \
            self._board[row_num - count][column_num - count] != NONE:
            count += 1
        if row_num - count >= 0 and column_num - count >= 0 and \
            self._board[row_num - count][column_num - count] == self._turn and\
            self._board[row_num -1][column_num -1] != self._turn:
            return True

    def diagonal_minus_plus(self,selection:list):
        row_num = int(selection[0])
        column_num = int(selection[1])
        count = 1
        # -1 + 1
        while row_num - count >= 0 and column_num + count < len(self._board[0]) and\
            self._board[row_num - count][column_num + count] == self.player_turn()and \
            self._board[row_num - count][column_num + count] != NONE:
            count += 1
        if row_num - count >= 0 and column_num + count < len(self._board[0]) and \
            self._board[row_num - count][column_num + count] == self._turn and\
            self._board[row_num -1][column_num +1] != self._turn:
            return True

    def diagonal_plus_minus(self,selection:list):

        row_num = int(selection[0])
        column_num = int(selection[1])
        count = 1
        # +1 - 1
        while row_num + count < len(self._board) and column_num - count >= 0 and\
            self._board[row_num +count][column_num - count] == self.player_turn()and \
            self._board[row_num + count][column_num - count] != NONE:
            count += 1
        if row_num + count < len(self._board) and column_num - count >= 0 and \
            self._board[row_num + count][column_num - count] == self._turn\
                and self._board[row_num +1][column_num -1] != self._turn:
            return True

    def flip_vertical(self,selection:list):
        """
        """
        row_num = int(selection[0])
        column_num = int(selection[1])
        count = 1
        if self.is_valid_move_vertical_plus(selection) == True:
            self._board[row_num][column_num] = self._turn
            while row_num + count < len(self._board[row_num]) and\
                self._board[row_num + count][column_num] == self.player_turn():
                self._board[row_num + count][column_num] = self._turn
                count += 1
        if self.is_valid_move_vertical_minus(selection) == True:
            self._board[row_num][column_num] = self._turn
            count = 1
            while row_num - count >= 0 and self._board[row_num - count][column_num] == self.player_turn():
                self._board[row_num - count][column_num] = self._turn
                count +=1

    def flip_horizontal(self,selection:list):
        """
        """
        row_num = int(selection[0])
        column_num = int(selection[1])
        count = 1
        if self.is_valid_move_horizontal_plus(selection) == True:
            self._board[row_num][column_num] = self._turn
            while column_num + count < len(self._board[0]) and\
                self._board[row_num][column_num+ count] == self.player_turn():
                self._board[row_num][column_num+ count] = self._turn
                count += 1
        if self.is_valid_move_horizontal_minus(selection) == True:
            self._board[row_num][column_num] = self._turn
            count = 1
            while column_num - count >= 0 and \
                self._board[row_num][column_num - count] == self.player_turn():
                self._board[row_num][column_num - count] = self._turn
                count += 1

    def flip_diagonal(self,selection:list):
        """
        """
        row_num = int(selection[0])
        column_num = int(selection[1])
        if self.diagonal_plus_plus(selection) == True:
            self._board[row_num][column_num] = self._turn
            count = 1
            while row_num + count < len(self._board) and \
                column_num + count < len(self._board[0]) and\
                self._board[row_num + count][column_num+ count] == self.player_turn():
                self._board[row_num + count][column_num+ count] = self._turn
                count += 1
        if self.diagonal_minus_minus(selection) == True:
            self._board[row_num][column_num] = self._turn
            count = 1
            while row_num - count >= 0 and column_num - count >= 0 and\
                self._board[row_num - count][column_num - count] == self.player_turn():
                self._board[row_num - count][column_num - count] = self._turn
                count += 1
        if self.diagonal_plus_minus(selection) == True:
            self._board[row_num][column_num] = self._turn
            count = 1
            while row_num + count < len(self._board[row_num]) and column_num - count >= 0\
                and self._board[row_num + count][column_num - count] == self.player_turn():
                self._board[row_num+ count][column_num - count] = self._turn
                count += 1
        if self.diagonal_minus_plus(selection) == True:
            self._board[row_num][column_num] = self._turn
            count =1
            while row_num - count >= 0 and column_num + count >= 0 and \
                self._board[row_num - count][column_num + count] == self.player_turn():
                self._board[row_num- count][column_num + count] = self._turn
                count += 1

    def check_validity(self,selection:list):
        """
        """
        horizontal = self.is_valid_move_horizontal_plus(selection)
        horizontal1 = self.is_valid_move_horizontal_minus(selection)
        vertical = self.is_valid_move_vertical_plus(selection)
        vertical1 = self.is_valid_move_vertical_minus(selection)
        diagonal1 = self.diagonal_minus_plus(selection)
        diagonal2 = self.diagonal_plus_minus(selection)
        diagonal3 = self.diagonal_plus_plus(selection)
        diagonal4 = self.diagonal_minus_minus(selection)
        if horizontal == True or horizontal1 == True or vertical == True or vertical1 == True or diagonal1 == True or diagonal2 == True or \
                diagonal3 == True or diagonal4 == True:
            return True
        else:
            return False

    def check_both_players(self):
        """
        """
        valid = False
        for col in range(len(self._board[0])):
            for row in range(len(self._board)):
                x = self.check_validity([row,col])
                y = self.check_validity([row,col])
                if x == True or y == True:
                    valid = True
        return valid

    def check_one_player(self):
        """
        """
        valid = False
        for col in range(len(self._board[0])):
            for row in range(len(self._board)):
                x = self.check_validity([row,col])
                if x == True:
                    valid = True

        return valid


    def count_of_chips(self):
        """
        Track the number of chips that
        each player has on the game board
        """
        count_black = 0
        count_white = 0
        for obj in self._board:
            for num in obj:
                if num == BLACK:
                    count_black += 1
                elif num == WHITE:
                    count_white += 1
        count = ("B:",count_black, "W:",count_white)
        return count

    def player_turn(self):
        """
        Keeps track of who's turn
        it is at any given time
        during the game play
        """
        if self._turn == BLACK:
            return WHITE
        else:
            return BLACK

    def count_black(self):
        black = 0
        for obj in self._board:
            for num in obj:
                if num == BLACK:
                    black += 1
        return black

    def count_white(self):
        white = 0
        for obj in self._board:
            for num in obj:
                if num == WHITE:
                    white += 1
        return white

    def winner(self):
        black = self.count_black()
        white = self.count_white()
        if(self._win == ">"):
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
        return("Winner: " + winner)

    def full_board(self):
        valid = True
        for row in range(len(self._board)):
            for col in range(len(self._board[0])):
                if self._board[row][col] == NONE:
                    valid = False
        return valid

def visual_othello_board(board:list) -> "Visual Game Board":
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
    Track the number of chips that
    each player has on the game board
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
    return ("B:",count_black, "W:",count_white)

def new_othello_board(INPUTS: list)-> [[str]]:
    """
    Makes an othello board that is a 2D list
    depending on the ROW and COL input
    """
    board = []
    for obj in range(int(INPUTS[0])):
        board.append([])
        for obj1 in range(int(INPUTS[1])):
            board[obj].append(NONE)

    return board

def initial_four_chips(board:list,INPUTS: list) -> "Game Board":
    """
    Inserts the initial 4 chips into the
    middle of the board depending on the
    columns and rows that the user gives
    """
    row_num = int(len(board)/2)
    column_num = int(len(board[0])/2)

    board[row_num-1][column_num-1] = NONE
    if INPUTS[3] == BLACK:
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
