
in1 = input()
in2 = input()
in3 = input()
in4 = input()
in5 = input()
in6 = input()

count = 0

if in1 == "W":
    count += 1
if in2 == "W":
    count += 1
if in3 == "W":
    count += 1
if in4 == "W":
    count += 1
if in5 == "W":
    count += 1
if in6 == "W":
    count += 1

if count >= 5:
    print(1)
elif count == 3 or count == 4:
    print(2)
elif count == 1 or count == 2:
    print(3)
else:
    print(-1)
