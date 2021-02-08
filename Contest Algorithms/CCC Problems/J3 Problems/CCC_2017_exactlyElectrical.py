
# NOT WORKING
start = input()
destination = input()
energy = int(input())

start.split()
destination.split()

# X values
a = int(start[0])
c = int(destination[0])

# Y values
d = int(destination[2])
b = int(start[2])

xDistance = abs(abs(a) - abs(c))
yDistance = abs(abs(b) - abs(d))
totalDistance = (xDistance + yDistance)*2

if totalDistance == energy:
    print("Y")
else:
    print("N")
