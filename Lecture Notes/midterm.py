
def something():
    while True:
        user_input = input("enter a ID: ")
        if user_input not in ["0","1","2","3","4","5","6","7","8","9"] and len(user_input) != 8:
            print("Error")
            return something()
        else:
            return int(user_input)



def something_recursive(all: "list of lists"):
    count = 0
    for x in all:
        if x == list:
            count += something_recursive(x)
        else:
            count += 1

    return count

print(something_recursive(["something",["something",10,],10]))
