import collections
GameState = collections.namedtuple('GameState', ['board', 'turn'])




def new_game() -> GameState:
    """
    returns a GameState representing a brand new game in which no moves have been made yet
    """
    return GameState(board = new_game_board())

