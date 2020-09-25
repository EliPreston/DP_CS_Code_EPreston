'''
Description; The method takes a list of integers and two integer values, returning the sum of all the elements that are between a (exclusive) and b (exclusive)
Parameters; int[] arr, int a, int b
Return; int
Pre-conditions; arr is a list of integers 
Post-conditions; n/a

'''


def findModSum2(lst, a, b):

    SUM = 0
    MIN = min(a, b)
    MAX = max(a, b)

    for i in lst:
        if MIN + 1 <= i <= MAX - 1:
            SUM += i
        else:
            pass

    print(SUM)


lst = 2, 3, 10, 9, 14, 25, 3, 100
a = 25
b = 5
findModSum2(lst, a, b)
