

def triangleTimes():

    a1 = int(input())
    a2 = int(input())
    a3 = int(input())

    if a1 == a2 == a3:
        print("Equilateral")
        return

    if a1 + a2 + a3 == 180:
        if a1 == a2 or a1 == a3 or a2 == a3:
            print("Isosceles")
            return
        else:
            print("Scalene")
            return
    print("Error")


triangleTimes()
