in1 = input()
in2 = input()
in3 = input()
in4 = input()

list1 = in1.split()
list2 = in2.split()
list3 = in3.split()
list4 = in4.split()


add1 = 0
for i in list1:
    i = float(i)
    add1 += i

add2 = 0
for i in list1:
    i = float(i)
    add2 += i

add3 = 0
for i in list1:
    i = float(i)
    add3 += i

add4 = 0
for i in list1:
    i = float(i)
    add4 += i


if add1 == add2 == add3 == add4:

    count = 0

    for i in range(0, len(list1), 1):
        t1 = list1[i]
        t1 = float(t1)

        t2 = list2[i]
        t2 = float(t2)

        t3 = list3[i]
        t3 = float(t3)

        t4 = list4[i]
        t4 = float(t4)

        column = t1 + t2 + t3 + t4

        if column == add1:
            count += 1

    if count == 4:
        print("magic")
    else:
        print("not magic")

else:
    print("not magic")
