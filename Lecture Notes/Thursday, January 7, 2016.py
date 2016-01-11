"""
f = open("D:/ICS-32/myfile.txt", "r")
print(f.read().split())

try:  # try something
    f = open("somethingsomething", "r")
except: # if something in the try does not work do the except
    print("Doh!")

"""
import math

try:
    x = math.sqrt(-1)
except ValueError:
    print("Doh!")
else:
    print("Woo-hoo")
finally:
    print("Sigh....")
