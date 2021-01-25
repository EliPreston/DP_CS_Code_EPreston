
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
