
a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

totalStepsTaken = 0
nikky = 0
byron = 0

while totalStepsTaken < s:

    nikky += (a-b)

    byron += (c-b)

    totalStepsTaken += nikky


if nikky > byron:
    print("Nikky")
elif byron > nikky:
    print("Byron")
elif nikky == byron:
    print("Tied")
