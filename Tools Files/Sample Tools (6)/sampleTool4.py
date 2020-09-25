'''
Description; The method takes a list of doubles and returns the sum of the digits.
Parameters; double[] data
Return; int
Pre-conditions;
Post-conditions;

'''


def findModSum4(lst):

    NUMS = []
    SUM = 0

    for i in lst:
        i = str(i)
        i = i.replace('.', '')
        NUMS.append(str(i))

    for i in NUMS:
        num = int(i)

        while num > 0:
            SUM += num % 10
            num = num // 10
    print(SUM)


lst = [1.2, 3.14, 7.89]
findModSum4([1.2, 3.14, 7.89])
