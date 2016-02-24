# 32979197 Vladislav Varadinov
import Othello_logic
print("FULL")

def starting_inputs():
    """
    """
    line_list = []
    for obj in range(2):
        line_list.append(int(input()))
    for obj in range(3):
        line_list.append(input())
    return line_list


def insert_input():
    """
    Returns the moves made by
    the user who's turn it is
    """
    user_input = []
    for obj in range(2):
        user_input.append(int(input()))
    return user_input

def count_of_chips(board:list):
    """
    Track the number of chips that
    each player has on the game board
    """
    count_black = 0
    count_white = 0
    for obj in board:
        for num in obj:
            if num == Othello_logic.BLACK:
                count_black += 1
            elif num == Othello_logic.WHITE:
                count_white += 1
    print("B:",count_black, "W:",count_white)



if __name__ == "__main__":
    choices1 = starting_inputs()
    game_board = Othello_logic.new_othello_board(choices1)
    Othello_logic.initial_four_chips(game_board,choices1)
    count_of_chips(game_board)
    Othello_logic.visual_othello_board(game_board)
    current_turn = choices1[2]
    print("Turn:",current_turn)
    while True:
        choices = insert_input()
        game_board = (Othello_logic.insert_check(game_board,choices))
        count_of_chips(game_board)
        Othello_logic.visual_othello_board(game_board)
        current_turn = Othello_logic.player_turn(current_turn)
        print("TURN:",current_turn)





