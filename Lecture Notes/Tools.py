def square(n: "number") -> "number":
    return n * n

def cube(n:"number")-> "number":
    return n * n * n

if __name__ == "__main__":
    n = int(input("NUMBER: "))
    print("The square {} is {}".format(n, square(n)))
    print("THE cube {} is {}".format(n, cube(n)))