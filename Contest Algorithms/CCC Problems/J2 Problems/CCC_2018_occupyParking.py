chars = int(input())
yesterday = input()
today = input()

ydy = list(yesterday)
tdy = list(today)


occupiedBoth = 0
for i in range(chars):
    if ydy[i] == "C" and tdy[i] == "C":
        occupiedBoth += 1
    else:
        pass
print(occupiedBoth)
