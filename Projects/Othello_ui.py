# 32979197 Vladislav Varadinov
import Othello_logic
print("FULL")

def initial_inputs():
    """
    Takes initial 4 inputs and stores
    them into a list for later usage
    """
    line_list = []
    for obj in range(2):
        line_list.append(int(input()))
    for obj in range(3):
        line_list.append(input())
    return line_list


#if __name__ == "__main__":
   # pass


