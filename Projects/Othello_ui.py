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
    user_input = input().split(" ")
    return user_input




def start_game():
    choices1 = starting_inputs()
    game_board = Othello_logic.new_othello_board(choices1)
    Othello_logic.initial_four_chips(game_board,choices1)
    Othello_logic.count_of_chips(game_board)
    Othello_logic.visual_othello_board(game_board)
    current_turn = choices1[2]
    print("Turn:",current_turn)
    while True:
        if Othello_logic.full_board(game_board) == True:
            choices = insert_input()
            game_logic = Othello_logic.GameLogic(game_board,current_turn,choices1[4])
            if game_logic.check_validity(choices[0],choices[1],current_turn,choices) == True and game_logic.insert_check(choices) == True:
                if game_logic.check_both_players(choices) == True:
                    print("Valid")
                    game_logic.flip_vertical(choices)
                    game_logic.flip_horizontal(choices)
                    game_logic.flip_diagonal(choices)
                    current_turn = game_logic.player_turn(current_turn)
                    Othello_logic.count_of_chips(game_board)
                    Othello_logic.visual_othello_board(game_board)
                    print("Turn:",current_turn)
                else:
                    Othello_logic.winner(game_board,choices1[4])
                    break
            else:
                print("Invalid")
        else:
            Othello_logic.winner(game_board,choices1[4])
            break





if __name__ == "__main__":
    start_game()



