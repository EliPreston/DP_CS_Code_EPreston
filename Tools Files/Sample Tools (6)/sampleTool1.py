'''
Description; The method takes a list of integers and returns the sum of all the elements that are multiples of 3
Parameters; int[] data
Return; int
Pre-conditions; data is a list of integers. 
Post-conditions; n/a

'''


def findModSum1(lst):

    SUM = 0

    for i in lst:
        if i % 3 == 0:
            SUM += i
        # else:
        #     pass
    print(SUM)


lst = [234, 346, 67, 46, 43, 487, 21, 3, 9, 6]
lst2 = [21, 4, 6, 9, 10, 12]
findModSum1(lst)
findModSum1(lst2)
