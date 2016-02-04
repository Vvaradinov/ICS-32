# Vladislav Varadinov  32979197 #Linxuan Xin 11311415
import connectfour
import ICS32CFSP
import Connectfour_ui

def col_num() -> int:
    '''Get the col number. If the col number is invalid, raise the ValueError.
    And ask again for a new col number.
    '''
    while True:
        try:
            user_input = int(input('Enter the column number:  ' )) -1
            connectfour._require_valid_column_number(user_input)
            return user_input
        except ValueError:
            print('Choose the number between 1 to {}'.format(connectfour.BOARD_COLUMNS))

def drop_or_pop() -> str:
    '''Get the user's move. If this move is invalid, raise the Error.
    And ask again for a new move.
    '''
    while True:
        user_input = input('POP OR DROP: ').upper().strip()
        if user_input == 'DROP':
            return 'DROP'
        elif user_input == 'POP':
            return 'POP'
        else:
            print('ERROR: Wrong Command.')

def game_board(game_state: connectfour.GameState) -> None:
    """
    Prints out a visual of the game board
    """
    board = game_state.board
    for col in range(connectfour.BOARD_COLUMNS):
        print(col+1, end = ' ')
    print('\n')
    for row in range(connectfour.BOARD_ROWS):
        space = ''
        for col in range(connectfour.BOARD_COLUMNS):
            if board[col][row] == connectfour.NONE:
                space += '. '
            if board[col][row] == 1:
                space += 'R '
            if board[col][row] == 2:
                space += 'Y '
        print(space)

def make_choice(game_state: connectfour.GameState, choice: str, col: int) -> tuple:
    '''Input the move and col number. If the move or col number is invaild,
    raise the InvalidMoveError ask and ask again. If the Game already over, raise
    GameOverError. Return a tuple include a new game state and the input message
    '''
    while True:
        try:
            if choice == 'DROP':
                updated = Connectfour_ui.drop_to_board(game_state, col)
                return updated, choice + ' ' + str(col + 1)
            else:
                updated = Connectfour_ui.pop_out_of_board(game_state, col)
                return updated, choice + ' '+ str(col + 1)

        except connectfour.InvalidMoveError:
            print('ERROR. InvalidMoveError. Try again.')
            choice = drop_or_pop()
            col = col_num()
        except connectfour.GameOverError:
            print('ERROR. Game is over.')
            break

def get_message(message: str) -> tuple:
    '''Transfer the message 'DROP/POP number' to a tuple(DROP/POP, number)'''
    text = message.split()
    step = text[0]
    col = text[1]
    return step, col

def get_state(message: ICS32CFSP.ServerResponse, state: connectfour.GameState) -> connectfour.GameState:
    step = message.response
    col_num = message.col_num
    _require_valid_move(step)
    connectfour._require_valid_column_number(col_num)
    game_state, message = make_choice(state, step, col_num)
    return game_state

def new_game() -> bool:
    '''Ask whether start a new game, Y for play again, N for Game over'''
    new_game = input('Play again?(Y/N)  ' ).upper().strip()
    if new_game == 'Y':
        return True
    elif new_game == 'N':
        return False
    else:
        print('ERROR: Wrong Command.')
        new_game()

def _require_valid_move(move: str) -> None:
    '''Check the input move is valid'''
    if move == 'DROP' or move == 'POP':
        return None
    else:
        raise connectfour.InvalidMoveError
