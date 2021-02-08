
xVal = int(input())
yVal = int(input())


if xVal > 0:
    if yVal > 0:
        print(1)
    else:
        print(4)
elif xVal < 0:
    if yVal > 0:
        print(2)
    else:
        print(3)
