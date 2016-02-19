class Always300:
    def __len__(self):
        return 300

z = Always300()
print(len(z))


print(3/4)

# __init__ new object of that class     \

def foo(x):
    return x.upper() * 2

class ABC:
    def upper(self):
        return 13

print(foo(ABC()))