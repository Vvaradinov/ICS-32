import os
import fnmatch
import shutil
from pathlib import Path
def First_Line():
    "First input line"
    first_input = input()
    while True:
        if Path(first_input).exists() and Path(first_input).is_dir():
            return Path(first_input)
        else:
            print("ERROR")
            return First_Line()
num_list = ["1","2","3","4","5","6","7","8","9","0"]
def Second_Line():
    "Second input line"
    second_input = input().split()
    while True:
        if second_input[0] in ["S","E","N"]:
            if second_input[0] == "S" and second_input[1][0] not in num_list:
                print("ERROR")
                return Second_Line()
            return second_input


def Third_Line():
    "Third input line"
    third_input = input()
    while True:
        if third_input not in ["P","F","D","T"]:
            print("ERROR")
            return Third_Line()
        else:
            return third_input

def Program(file_path:"Path", second_str: [str], third_str: str):
    "Main Program with second and third input"
    interesting_files = []
    for file in os.listdir(str(file_path)): # loop for first letters
        path_name1 = os.path.join(str(file_path), str(file)) # converting a path type to a file type
        if second_str[0] == "E" and file.endswith(second_str[1]):
            interesting_files.append(file)
        elif second_str[0] == "S" and os.stat(path_name1).st_size > int(second_str[1]):
            interesting_files.append(file)
        elif second_str[0] == "N" and fnmatch.fnmatch(file,second_str[1]):
            interesting_files.append(file)
    for obj in interesting_files: # loop for second letters
        path_name = os.path.join(str(file_path), str(obj))  # converting a path type to specify the operating system
        if third_str == "P":                                # works on every operating system
            print(os.path.abspath(obj))
        elif third_str == "F":
            print(obj)
            infile = open(path_name,"r").readline()
            print(infile)
        elif third_str == "D":
            duplicate = os.path.join(str(file_path), str(obj) + ".dup")
            print(obj)
            print(shutil.copy(path_name,duplicate))
        elif third_str == "T":
            print(obj)
            os.utime(path_name)
Program(First_Line(),Second_Line(),Third_Line())


