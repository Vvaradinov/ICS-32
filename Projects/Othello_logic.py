# 32979197 Vladislav Varadinov

NONE = "."
WHITE = "W"
BLACK = "B"



class GameLogic():
    def __init__(self,board:list,turn:str,selection:[int]):
        self._board = board
        self._selection = selection
        self._turn = turn

    def insert_check(self):
        """
        Checks if the insertion we make
        is legal- meaning is the spot free
        to put a new a chip or is there a chip already there
        """

        row_num = int(self._selection[0]) -1
        column_num = int(self._selection[1]) -1
        while True:
            if self._board[row_num][column_num] == NONE:
                return True
            else:
                return False




    def vertical_valid_plus(self):
        """
        """

        row_num = int(self._selection[0]) -1
        column_num = int(self._selection[1]) -1
        current_turn = self._turn
        count = 1
        while True:
            if self.insert_check() == True:
                while True:
                    try:
                        if self._board[row_num + count][column_num] == NONE:
                            return False
                        if self._board[row_num + count][column_num] != current_turn:
                            count += 1
                        else:
                            if self._board[row_num + count][column_num] == current_turn:
                                self._board[row_num][column_num] = current_turn
                                print("Valid")
                                return True
                    except IndexError:
                        break
            break

    def vertical_valid_minus(self):
        """
        """

        row_num = int(self._selection[0]) -1
        column_num = int(self._selection[1]) -1
        current_turn = self._turn
        count = 1
        while True:
            if self.insert_check() == True:
                while True:
                    if self._board[row_num - count][column_num] == NONE:
                        return False
                    if self._board[row_num- count][column_num ] != current_turn:
                        count += 1
                    else:
                        if self._board[row_num - count][column_num] == current_turn:
                            self._board[row_num][column_num] = current_turn
                            print("Valid")
                            return True
            break

    def horizontal_valid_plus(self):
        """
        """

        row_num = int(self._selection[0]) -1
        column_num = int(self._selection[1]) -1
        current_turn = self._turn
        count = 1
        while True:
            if self.insert_check() == True:
                while True:
                    try:
                        if self._board[row_num][column_num + count] == NONE:
                            return False
                        if self._board[row_num][column_num + count] != current_turn:
                            count += 1
                        else:
                            if self._board[row_num][column_num +count] == current_turn:
                                self._board[row_num][column_num] = current_turn
                                print("Valid")
                                return True
                    except IndexError:
                        break
            break

    def horizontal_valid_minus(self):
        """
        """

        row_num = int(self._selection[0]) -1
        column_num = int(self._selection[1]) -1
        current_turn = self._turn
        count = 1
        while True:
            if self.insert_check() == True:
                while True:
                    if self._board[row_num][column_num - count] == NONE:
                        return False
                    if self._board[row_num][column_num - count] == player_turn(current_turn):
                        count += 1

                    else:
                        if self._board[row_num][column_num -count] == current_turn:
                            self._board[row_num][column_num] = current_turn
                            print("Valid")
                            return True
            break


    def vertical_check(self):
        """
        Checks the spot we are trying to put in on a vertical scale,
        if the spot is empty --> check if the vertical line,
        if it's the opposite color --> continue until you
        find your color that is nearest to the spot
        you are trying to put in and change everything
        in between to your color!!
        """
        row_num = int(self._selection[0]) - 1
        column_num = int(self._selection[1]) - 1
        current_turn = self._turn
        count = 1
        if self.vertical_valid_plus() == True:
            for obj in self._board[column_num]:
                    try:
                        if self._board[row_num+count][column_num] == player_turn(current_turn):
                            self._board[row_num+count][column_num] = current_turn
                            count += 1
                    except IndexError:
                        break
        count = 1
        if self.vertical_valid_minus() == True:
            for obj in self._board[column_num]:
                    if self._board[row_num-count][column_num] == player_turn(current_turn):
                        self._board[row_num-count][column_num] = current_turn
                        count += 1






    def horizontal_check(self):
        """
        """
        row_num = int(self._selection[0]) - 1
        column_num = int(self._selection[1]) -1
        current_turn = self._turn

        count = 1
        if self.horizontal_valid_plus() == True:
            for obj in self._board[row_num]:
                try:
                    if self._board[row_num][column_num+ count] == player_turn(current_turn):
                        self._board[row_num][column_num + count] = current_turn
                        count += 1
                except IndexError:
                    break
        count = 1
        if self.horizontal_valid_minus() == True:
            for obj in self._board[row_num]:
                if self._board[row_num][column_num-count] == player_turn(current_turn):
                    self._board[row_num][column_num-count] = current_turn
                    count += 1




    def diagonal_valid_minus_plus(self):
        """
        """
        row_num = int(self._selection[0]) -1
        column_num = int(self._selection[1]) -1
        current_turn = self._turn
        count = 1
        while True:
            if self.insert_check() == True:
                while True:
                    try:
                        if self._board[row_num - count][column_num + count] == NONE:
                            return False
                        if self._board[row_num - count][column_num + count] != current_turn:
                            count += 1
                        else:
                            if self._board[row_num - count][column_num+ count] == current_turn:
                                self._board[row_num][column_num] = current_turn
                                print("Valid")
                                return True
                    except IndexError:
                        break
            break
    def diagonal_valid_plus_minus(self):
        """
        """
        row_num = int(self._selection[0]) -1
        column_num = int(self._selection[1]) -1
        current_turn = self._turn
        count = 1
        while True:
            if self.insert_check() == True:
                while True:
                    try:
                        if self._board[row_num + count][column_num - count] == NONE:
                            return False
                        if self._board[row_num + count][column_num - count] != current_turn:
                            count += 1
                        else:
                            if self._board[row_num + count][column_num - count] == current_turn:
                                self._board[row_num][column_num] = current_turn
                                print("Valid")
                                return True
                    except IndexError:
                        break
            break
    def diagonal_valid_plus_plus(self):
        """
        """
        row_num = int(self._selection[0]) -1
        column_num = int(self._selection[1]) -1
        current_turn = self._turn
        count = 1
        while True:
            if self.insert_check() == True:
                while True:
                    try:
                        if self._board[row_num + count][column_num + count] == NONE:
                            return False
                        if self._board[row_num + count][column_num + count] != current_turn:
                            count += 1
                        else:
                           if self._board[row_num + count][column_num+ count] == current_turn:
                                self._board[row_num][column_num] = current_turn
                                print("Valid")
                                return True
                    except IndexError:
                        break
            break

    def diagonal_valid_minus_minus(self):
        """
        """
        row_num = int(self._selection[0]) -1
        column_num = int(self._selection[1]) -1
        current_turn = self._turn
        count = 1
        while True:
            if self.insert_check() == True:
                while True:
                    try:
                        if self._board[row_num - count][column_num - count] == NONE:
                            return False
                        if self._board[row_num - count][column_num - count] != current_turn:
                            count += 1
                        else:
                            if self._board[row_num - count][column_num - count] == current_turn:
                                self._board[row_num][column_num] = current_turn
                                print("Valid")
                                return True
                    except IndexError:
                        break
            break


    def diagonal_check(self):
        """
        """
        row_num = int(self._selection[0]) - 1
        column_num = int(self._selection[1]) -1
        current_turn= self._turn


        count = 1
        if self.diagonal_valid_minus_plus() == True:
            for obj in self._board:
                 try:
                    if self._board[row_num -count][column_num + count] == player_turn(current_turn):
                            self._board[row_num - count][column_num + count] = current_turn
                            count += 1
                 except IndexError:
                     break
        if self.diagonal_valid_plus_minus() == True:
            for obj in self._board:
                try:
                    if self._board[row_num + count][column_num - count] == player_turn(current_turn):
                            self._board[row_num + count][column_num - count] = current_turn
                            count += 1
                except IndexError:
                    break
        if self.diagonal_valid_plus_plus() == True:
            for obj in self._board:
                try:
                    if self._board[row_num + count][column_num + count] == player_turn(current_turn):
                            self._board[row_num + count][column_num + count] = current_turn
                            count += 1
                except IndexError:
                    break
        if self.diagonal_valid_minus_minus() == True:
            for obj in self._board:
                if self._board[row_num - count][column_num - count] == player_turn(current_turn):
                        self._board[row_num - count][column_num -count] = current_turn
                        count += 1



    def is_valid_move(self):
        hor_plus = self.horizontal_valid_plus()
        hor_min = self.horizontal_valid_minus()
        ver_plus = self.vertical_valid_plus()
        ver_minus = self.vertical_valid_minus()
        diagonal_plus = self.diagonal_valid_plus_plus()
        diagonal_minus = self.diagonal_valid_minus_minus()
        diagonal_plus_minus = self.diagonal_valid_plus_minus()
        diagonal_minus_plus = self.diagonal_valid_minus_plus()
        if hor_plus  == True or hor_min == True:
            return True
        if ver_minus == True or ver_plus == True:
            return True
        if diagonal_minus == True or diagonal_minus_plus == True or diagonal_plus == True or diagonal_plus_minus == True:
            return True
        else:
            return False


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


