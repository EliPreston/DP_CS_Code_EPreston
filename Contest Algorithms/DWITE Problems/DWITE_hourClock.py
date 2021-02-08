

def convertTime(time):

    h = time[0:2]
    h = int(h)

    m = time[3:5]
    # m = int(m)

    # Assume time is AM
    x = "AM"

    if (12 <= h <= 23):
        x = "PM"
        h = h - 12

    print(str(h)+":"+str(m)+" "+x)


for i in range(0, 3, 1):
    t = input()
    convertTime(t)
