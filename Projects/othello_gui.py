# Vladislav Varadinov #32979197
import tkinter
import Othello_logic


class Othello_gui():
    def __init__(self):
        self._root_window = tkinter.Tk()

        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(0, weight =1)
        self._root_window.columnconfigure(1, weight = 1)

        self._canvas = tkinter.Canvas(
            master = self._root_window, width = 800, height = 800,
            background = "#e5f4f8")

        self._canvas.grid(
            row = 1, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._root_window.bind('<Return>', self.game_specifics)
        self._canvas.bind('<Configure>', self.when_canvas_is_resized)
        self._canvas.bind('<Button-1>', self.when_canvas_is_clicked)
        self._canvas.bind('<Button-3>',self.when_canvas_is_clicked_right)
        self._canvas.bbox('<Button-1>',self.game_rules)
        self._rules_text = tkinter.StringVar()
        self._rules_text.set("GAME RULES - ENTER THE 5 INPUTS IN THE BOX AND CLICK THE BUTTON TO CONTINUE "'\n'
                             "NOTE: THIS GUI VERSION OF THE GAME ASSUMES THE USER IS FAMILIAR WITH THE GAME RULES."'\n'
                             "1. CLICK WITH THE LEFT MOUSE BUTTON TO PLACE A CHIP" '\n'
                             "2. IF THE CURRENT PLAYER TURN DOES NOT HAVE A LEGAL MOVE BUT THE OPPOSITE COLOUR HAS A TURN:"'\n'
                             "CLICK THE RIGHT MOUSE BUTTON ON THE BOX TO SWITCH PLAYERS"'\n'
                             "3. EVERYTHING ELSE IS AUTOMATIC"'\n'
                             "ENJOY YOUR GAME. CLICK ANYWHERE TO CONTINUE TO THE INPUT SCREEN")
        self._rules = tkinter.Button(master = self._root_window,textvariable= self._rules_text,command= lambda :self.game_rules(),font= ("Helvetica Black",15))
        self._rules.grid(row=0,column=0,sticky= tkinter.W)



        self._NONE = []
        self._BLACK = []
        self._WHITE = []

        self._current_turn = tkinter.StringVar()
        self._chip_count = tkinter.StringVar()

        self._input_box = tkinter.Entry(master= self._root_window,font= ("Helvetica Black",20))
        self._input_box.grid(row= 1, column=1 ,sticky= tkinter.E)

        self._input_directions = tkinter.StringVar()
        self._input_directions.set("Row Number - Between 4-16")

        self._game_initial_inputs = []
        self._counter = 0

        self._button = tkinter.Button(master = self._root_window,textvariable= self._input_directions,command= lambda : self.game_specifics(), font= ("Helvetica Black",15))
        self._button.grid(row=1,column=0,sticky=tkinter.W)

    def game_rules(self):
        """
        """
        self._rules.grid_forget()

    def game_specifics(self):
        """
        Takes the initial user inputs
        and starts the actual game-play
        """
        conditions = ["Column Number - Between 4-16", "Who Will Go First: (B or W)", "Starting Pieces (B or W)", "Win Condition > or < ",""]
        user_inputs = self._input_box.get()
        self._game_initial_inputs.append(user_inputs)
        self._input_box.delete(0, 'end')
        self._input_directions.set(conditions[self._counter])
        self._counter += 1
        if self._counter > 4:
            self._root_window.unbind('<Return>')
            self._input_box.grid_forget()
            self._button.grid_forget()
            self.game_logic()
            self.make_board()
            self.make_the_chips()
            self.create_shapes()
            self.keep_score_and_turn()

    def when_canvas_is_resized(self,event: tkinter.Event):
        """
        When the canvas gets the proper re-sizing
        add the initial 4 chips and draw the boxes
        of the game board
        """
        self.create_shapes()

    def when_canvas_is_clicked(self,event: tkinter.Event):
        """
        When the user interacts with the board.
        All of our game logic invoking regarding
        the rules is in this function.
        """
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        inputs = self._game_initial_inputs

        x = 1/ int(inputs[1])
        y = 1/ int(inputs[0])

        col_frac = event.x /width
        row_frac = event.y /height

        col = round(col_frac/x - 0.5)
        row = round(row_frac/y - 0.5)


        valid = self._game_obj.check_validity([row,col])
        if valid == True and self._game_obj.insert_check([row,col]) == True:
            self._game_obj.flip_horizontal([row,col])
            self._game_obj.flip_vertical([row,col])
            self._game_obj.flip_diagonal([row,col])
            self.make_the_chips()
            self.create_shapes()
            self.update_score_and_turn()
            self._game_obj._turn = self._game_obj.player_turn()


        if self._game_obj.full_board() == True or self._game_obj.check_both_players() == False:
            player_won = self._game_obj.winner()
            self._win = tkinter.Label(master = self._root_window, text = player_won, font = ('Helvetica Black', '15'))
            self._win.grid(row = 3, columnspan = 2)

    def when_canvas_is_clicked_right(self,event:tkinter.Event):
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        inputs = self._game_initial_inputs

        x = 1/ int(inputs[1])
        y = 1/ int(inputs[0])

        col_frac = event.x /width
        row_frac = event.y /height

        col = round(col_frac/x - 0.5)
        row = round(row_frac/y - 0.5)
        valid = self._game_obj.check_validity([row,col])
        self.update_score_and_turn()
        if valid == False:
            self._game_obj._turn = self._game_obj.player_turn()

    def game_logic(self):
        """
        Creates our game logic objects
        and creates us an empty board
        """
        inputs = self._game_initial_inputs
        self._game_obj = Othello_logic.GameLogic(Othello_logic.new_othello_board(inputs),inputs[2],inputs[4])
        self._game_board = Othello_logic.initial_four_chips(self._game_obj._board,inputs)

    def make_board(self):
        """
        Makes the game-board using
        the initial inputs the user gives
        and appends everything to a list
        """

        inputs = self._game_initial_inputs
        col = 1/ int(inputs[1])
        row = 1/ int(inputs[0])
        for r in range(int(inputs[0])):
            for c in range(int(inputs[1])):
                box = [col*c, row*r, col*(c+1), row*(r+1)]
                self._NONE.append(box)
    def make_the_chips(self):
        """
        Keeps track of the chips played and appends them to
        a list accordingly
        """
        self._BLACK = []
        self._WHITE = []
        inputs = self._game_initial_inputs

        col = 1/ int(inputs[1])
        row = 1/ int(inputs[0])

        convert_row = row/ 10
        convert_column = col/ 10

        for r in range(int(inputs[0])):
            for c in range(int(inputs[1])):
                final = [col*c + convert_column, row*r + convert_row, col*(c+1) -convert_column, row*(r+1) -convert_row]
                if self._game_obj._board[r][c] == "B":
                    self._BLACK.append(final)
                elif self._game_obj._board[r][c] == "W":
                    self._WHITE.append(final)

    def keep_score_and_turn(self):
        """
        Keeps score and the player turn
        Based on the GameLogic
        """
        self._current_turn.set(self._game_obj._turn)
        self._turn_print =  tkinter.Label(master = self._root_window, textvariable = self._current_turn, font = ('Arial Black', '20'))
        self._turn_print.grid(row = 0, column = 0)

        self._chip_count.set(self._game_obj.count_of_chips())
        self._count_print = tkinter.Label(master = self._root_window, textvariable = self._chip_count, font = ('Arial Black', '20'))
        self._count_print.grid(row = 0, column = 1)

    def update_score_and_turn(self):
        """
        Updates the turn and score board
        Based on the GameLogic
        """
        self._current_turn.set(self._game_obj.player_turn())
        self._chip_count.set(self._game_obj.count_of_chips())

    def create_shapes(self):
        """
        Creates our shapes for the:
        Boxes and Circles( game chips)
        """
        self._canvas.delete(tkinter.ALL)
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        for obj in self._NONE:
            self._canvas.create_rectangle(obj[0]*width, obj[1]*height, obj[2]*width, obj[3]*height)
        for obj in self._BLACK:
            self._canvas.create_oval(obj[0]*width, obj[1]*height, obj[2]*width, obj[3]*height, fill= 'black')
        for obj in self._WHITE:
            self._canvas.create_oval(obj[0]*width, obj[1]*height, obj[2]*width, obj[3]*height, fill= 'white')


if __name__ == "__main__":
    Othello_gui()._root_window.mainloop()