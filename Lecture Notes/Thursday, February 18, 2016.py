def sum_all(x:[[int]]) -> int:
    the_sum = 0

    for sublist in x:
        for num in sublist:
            the_sum += num

    return the_sum

def increment_all(x: [[int]])-> None:
    for sublist in x:
        for num in range(len(sublist)):
            sublist[num] += 1

a = [[1,2],[3,4],[5,6]]
(increment_all(a))
#print(a)

"""
x = [1,2,3,4,5]
for y in x:
    y += 1

x = [] -> 1,2,3,4,5
y gets the first value of the first element of x # reference

y has nothing to do with the list it's a reference to the values in it!
y changes the value and not the list itself
changing what y refers to the value in the loop after it changes the value it moves to the next value and the previous
value gets stored in garbage collector

"""
x = [[1,2,3],[4,5,6],[7,8,9]]
y = [[1,2],[3,4],[5,6],[7,8]]

# 2D lists for incrementing
def increment_diagonal(x:[[int]])-> None: # Project 4 and 5 Game logic basis
    for i in range(len(x)):
        if i < len(x[i]):
            x[i][i] += 1


increment_diagonal(x)
print(x)
increment_diagonal(y)
print(y)


# [_1_,  2,  3,],
# [4,  _5_,  6],
# [7,   8,  _9_]]
# x[0][0]
# x[1][1]
# x[2][2]
# x[0][0] += 1
# x[1][1] += 1
# skip x[2][2]
# skip x[3][3]






