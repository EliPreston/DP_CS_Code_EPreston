'''
Description; The method takes a list of integers and two integer values then returns the sum of all the elements that are multiples of a and b
Parameters; int[] values, int a, int b
Return; int
Pre-conditions; values is a list of integers of any size and a and b are valid positive integer values.
Post-conditions;

'''


def findModSum3(lst, a, b):

    SUM = 0
    for i in lst:
        if i % 5 == 0 and i % 2 == 0:
            SUM += i
        else:
            pass

    print(SUM)


lst = [21, 30, 10, 99, 14, 2, 100]
a = 5
b = 2
findModSum3(lst, a, b)
