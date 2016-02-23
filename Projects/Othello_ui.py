# 32979197 Vladislav Varadinov
import Othello_logic
print("FULL")

def board_inputs():
    """
    Takes initial 2 inputs and stores
    them into a list for later usage
    """
    line_list = []
    for obj in range(2):
        line_list.append(int(input()))
    return line_list

def specific_inputs():
    """
    Takes the last 3 inputs and stores
    them into a list for later usage
    """
    line_list = []
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



#if __name__ == "__main__":
 #   print(insert_input())



