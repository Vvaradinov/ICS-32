from pathlib import Path

# * = wildcard
p = Path("D:\ICS32\Lecture Notes")
print(p)
print(type(p))


def sum_numbers(numlist: [[int]]) -> int:
    total = 0
    for sub_list in numlist:
        for num in sub_list:
            total += num
    return total

assert(sum_numbers([1,2,3,4,5] == 15))
assert(sum_numbers([]) == 0)



def sum_numbers(numlist: [int or [int]]) -> int:
    total = 0

    for element in numlist:
        if type(element) == int:
            total += element
        else:
            for num in element:
                total += num
    return total




# A nested list of integer is a list in which every element
#is either
#    * an integer
#    * a nested list of integers

def sum_of_numbers(numlist: "nested list of integers") -> int:
    total = 0
    for element in numlist:
        if type(element) == int:
            total += element
        else:
            total += sum_numbers(element) # recursion leap of faith

        return total