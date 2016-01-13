import os
import fnmatch
import shutil


def Search():
    while True:
        try:
            first_input = input()
            os.listdir(first_input)
        except FileNotFoundError:
            print("Error!")
        else:
            break
    second_input = input().split()
    interesting_files_list = []
    for file in os.listdir(first_input):
        pathname = os.path.join(first_input,file)
        if second_input[0] == "E" and file.endswith(second_input[1]):
            interesting_files_list.append(file)
        elif second_input[0] == "N" and fnmatch.fnmatch(file, second_input[1]):
            interesting_files_list.append(file)
        elif second_input[0] == "S" and os.stat(pathname).st_size > int(second_input[1]):
            interesting_files_list.append(file)
    third_input = input()
    for obj in interesting_files_list:
        pathname_2 = os.path.join(first_input,obj)
        if third_input == "P":
            print(os.path.abspath(obj))
        elif third_input == "F":
            print(os.path.abspath(obj))
            infile = open(pathname_2,"r").readline()
            print(infile)
        elif third_input == "D":
            duplicate = os.path.join(first_input,obj + ".dup")
            print(shutil.copy(pathname_2,duplicate))
        elif third_input == "T":
            os.utime(pathname_2)
(Search())