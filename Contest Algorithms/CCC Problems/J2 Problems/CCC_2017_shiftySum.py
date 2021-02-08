
n = int(input())
k = int(input())


total = n
for i in range(k):
    n = n*10
    total = total + n

print(total)
