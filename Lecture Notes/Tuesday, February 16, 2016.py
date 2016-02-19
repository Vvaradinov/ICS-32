a = [1,2,3,4]
b = a # same refernce if you call it
print(a)
print(b)
c = a[:]
a.append(5)
print(c)
print(a)
print(b)

x = [[1,2,3],[1,2,3],[1,2,3]]
x[0].append(4)
print(x)

def sum_all(x:[[int]])-> int:
    the_sum = 0

    for sublist in x:
        for num in sublist:
            the_sum += num

    #magic happens here

    return the_sum

def increment_all(x: [[int]]):
    for sublist in x:
        for num in sublist:

            num += 1
#print(increment_all([[1,2,3],[1,2,3],[1,2,3]]))
