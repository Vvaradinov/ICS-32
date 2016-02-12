# duck_typing.py
#
# ICS 32 Winter 2016
# Code Example
#
# This module makes use of Python's "duck typing" feature by implementing
# six classes that all have the same interface, meaning that objects of
# these classes can be used interchangeably.  Each class represents some
# kind of operation that can be performed on a single input; asking an
# object of one of these classes to "calculate" is how you ask it to
# perform its operation.
#
# Collectively, we'll say that objects of these classes are "calcs"
# (i.e., you can ask them to calculate something, by giving them a value
# and expecting some value back).  In general, a "calc" (in our definition
# here) is an object that has a method "calculate" that takes a single
# parameter (in addition to "self") and returns the result of some arbitrary
# calculation on that input.
#
# It should be noted that all calcs don't necessarily take the same kind
# of input (e.g., a calc that squares a number works for numbers but not
# for lists, while a calc that finds the length of its input works for lists
# but not for numbers).  Ultimately, a calc will fail if given input
# incompatible with its operation, though this is no different than any
# other function in Python.

import math



class ZeroCalc:
    def calculate(self, n):
        return 0


class SquareCalc:
    def calculate(self, n):
        return n * n


class CubeCalc:
    def calculate(self, n: float) -> float:
        return n * n * n


class LengthCalc:
    def calculate(self, n):
        return len(n)


class SquareRootCalc:
    def calculate(self, n):
        return math.sqrt(n)


class MultiplyByCalc:
    def __init__(self, multiplier):
        self._multiplier = multiplier

    def calculate(self, n):
        return n * self._multiplier


# As an example of a function that uses these classes, consider this
# one called run_calcs, which takes a list of calcs and a starting
# value, and applies the calcs in sequence (i.e., the first calc is run
# against the starting value, the second is run against the result of
# the first, the third is run against the result of the second, and
# so on).  The result of the last calc in the list is the overall
# result.
#
# Note that I haven't written a type annotation for the starting_value
# parameter, and that I haven't specified a return type.  That's because
# what makes starting_value legal depends on the calcs, and the type of
# result also depends on the calcs; different kinds of calcs operate on
# different kinds of values and give back different kinds of results.


def run_calcs(calcs: ['Calc'], starting_value):
    current_value = starting_value

    for calc in calcs:
        current_value = calc.calculate(current_value)

    return current_value

print(run_calcs([SquareCalc(),SquareCalc()],4))
print(run_calcs([LengthCalc(), MultiplyByCalc(2)], 'Boo'))
print(run_calcs([], 80))
print(run_calcs([MultiplyByCalc(3), LengthCalc(), SquareCalc()], 'Boo'))

# The thing to notice about run_calcs is that it doesn't have any code
# in it that checks types.  There's nothing like this:
#
#     if type(x) == SquareCalc:
#         square the number
#     elif type(x) == MultiplyByCalc:
#         multiply the number
#     ...
#
# Why that's such a good thing is because we can add new kinds of
# calcs by simply writing new classes that implement the same
# interface (i.e., that have the appropriate calculate method),
# without ever having to touch run_calcs again, yet run_calcs will
# work automatically with the new kinds of objects.  One of the goals
# when we write ever-larger programs is isolating the effect of
# changes, so anything we can do to prevent one change from causing
# cascading changes in many other places is a big win.
#
# Try executing this module and then evaluating these expressions in
# the Python interpreter.  Before you evaluate each one, decide what
# you think its outcome should be.
#
#     run_calcs([SquareCalc(), SquareCalc()], 4)
#     run_calcs([LengthCalc(), MultiplyByCalc(2)], 'Boo')
#     run_calcs([], 80)
#     run_calcs([MultiplyByCalc(3), LengthCalc(), SquareCalc()], 'Boo')
#
# Now try writing a new class that implements the operation of your
# choice.  Re-execute this module (after writing your new class) and
# try calling run_calcs and passing it an object of your class.
# Voila!  Works fine!
#
# I should note here that this appears to be similar to the idea of
# passing functions as parameters to other functions, and, indeed, it
# is.  Where it differs, though, is that the objects we're creating
# are capable of carrying state with them, whereas functions are
# limited to accessing the parameters that are passed to them.
# So, for example, our MultiplyByCalc class takes a parameter to its
# constructor; its __init__ method stores it in an attribute, and that
# attribute is then available at the time the calculate() method is
# called.  This is not actually as mind-bending as it sounds; since
# calculate() is a method, it accepts an additional "self" parameter,
# and the attribute "_multiplier" actually belongs to the "self"
# object.