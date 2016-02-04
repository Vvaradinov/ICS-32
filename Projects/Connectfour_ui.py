# Vladislav Varadinov  32979197 #Linxuan Xin 11311415

import collections
import connectfour
import common_functions




def welcome_banner() -> "Welcome banner":
    print("Welcome to Connect Four")
    print("------------------------")
    print("Columns should be selected by typing a number between 1 and 7")



def drop_to_board(game_state, column_num):
    """
    Drops obj to the board, and updates the board.
    If invalid move is made raises Error
    """
    return connectfour.drop(game_state,column_num)


def pop_out_of_board(game_state,column_num):
    """
    Pops obj out of the board and updates the board.
    If invalid move is made raises Error
    """
    return connectfour.pop(game_state,column_num)

def player_wins(game_state):
    """
    Executed when a players wins the game
    """
    if connectfour.winner(game_state) != 0:
        if connectfour.winner(game_state) == 1:
            print("Red Player Wins")
        elif connectfour.winner(game_state) == 2:
            print("Yellow Player Wins")



def play_game():
    """
    Executing the game logic with 2 players taking turns
    """
    welcome_banner()
    GameState = connectfour.new_game()
    while True:
        user_input = input("Would you like to pop or drop: ")
        if user_input.strip() == "pop":
            GameState = pop_out_of_board(GameState,common_functions.col_num())
            common_functions.game_board(GameState)
        elif user_input.strip() == "drop":
            GameState = drop_to_board(GameState,common_functions.col_num())
            common_functions.game_board(GameState)
        else:
            print("Please enter a valid input")
        if connectfour.winner(GameState) != 0:
            player_wins(GameState)
            break
        print("\n")
if __name__ == "__main__":
    play_game()