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



def start_game():
    choices1 = starting_inputs()
    game_board = Othello_logic.new_othello_board(choices1)
    Othello_logic.initial_four_chips(game_board,choices1)
    count_of_chips(game_board)
    Othello_logic.visual_othello_board(game_board)
    current_turn = choices1[2]
    print("Turn:",current_turn)
    while True:
        if Othello_logic.full_board(game_board) == True:
            choices = insert_input()
            game_logic = Othello_logic.GameLogic(game_board,current_turn,choices,choices1[4])
            if game_logic.check_validity(choices[0],choices[1],current_turn) == True and game_logic.insert_check() == True:
                if game_logic.check_both_players() == True:
                    print("Valid")
                    game_logic.flip_vertical()
                    game_logic.flip_horizontal()
                    game_logic.flip_diagonal()
                    current_turn = Othello_logic.player_turn(current_turn)
                    count_of_chips(game_board)
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



