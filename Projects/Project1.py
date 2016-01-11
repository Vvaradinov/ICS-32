import os
import fnmatch



def Search():
    #first_input = input("Enter a path to a file:")
    #check = os.listdir(first_input)
   # second_input = input("")

    try:
        first_input = input("Enter a path to a file:")
        (os.listdir(first_input))
    except FileNotFoundError:
        print("Error!")
    second_input = input().split()
    if second_input[0] == "E":
        print(second_input[1])








Search()