
def distinctDate():

    y = int(input())
    distinct = 'no'

    while distinct != 'yes':
        y += 1
        l = []

        for i in str(y):
            if i not in l:
                l.append(i)
                distinct = "yes"
            else:
                distinct = "no"
                break

    print(y)


distinctDate()


# Francesco's Solution
def findYear():

    y = input()

    testYear = int(y)
    digits = []

    while True:
        # while 1 == 1:

        testYear = str(int(testYear) + 1)
        digits = []
        for i in testYear:
            digits.append(i)

        contains_duplicates = any(digits.count(
            element) > 1 for element in digits)

        if contains_duplicates == False:
            print(testYear)
            return


findYear()
