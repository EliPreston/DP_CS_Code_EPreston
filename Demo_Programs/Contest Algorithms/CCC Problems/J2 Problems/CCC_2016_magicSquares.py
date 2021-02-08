

# total = []

# vertical1 = 0
# vertical2 = 0
# vertical3 = 0
# vertical4 = 0

# count = 0
# for i in range(0, 4, 1):
#     horizontal = 0
#     new = input()
#     line = new.split()

#     vertical1 += int(line[0])
#     vertical2 += int(line[1])
#     vertical3 += int(line[2])
#     vertical4 += int(line[3])

#     for i in range(0, len(line), 1):
#         horizontal += int(line[i])
#     total.append(horizontal)

# total.append(vertical1)
# total.append(vertical2)
# total.append(vertical3)
# total.append(vertical4)


# for i in range(len(total)):
#     if total[0] != total[i]:
#         count += 1

# if count == 0:
#     print("magic")
# else:
#     print("not magic")

# ************************************

in1 = input()
in2 = input()
in3 = input()
in4 = input()

list1 = in1.split()
list2 = in2.split()
list3 = in3.split()
list4 = in4.split()


horizontal1 = 0
for i in list1:
    i = float(i)
    horizontal1 += i

horizontal2 = 0
for i in list1:
    i = float(i)
    horizontal2 += i

horizontal3 = 0
for i in list1:
    i = float(i)
    horizontal3 += i

horizontal4 = 0
for i in list1:
    i = float(i)
    horizontal4 += i


if horizontal1 == horizontal2 == horizontal3 == horizontal4:

    count = 0

    for i in range(0, 4, 1):
        t1 = list1[i]
        t1 = float(t1)

        t2 = list2[i]
        t2 = float(t2)

        t3 = list3[i]
        t3 = float(t3)

        t4 = list4[i]
        t4 = float(t4)

        column = t1 + t2 + t3 + t4

        if column == horizontal1:
            count += 1

    if count == 4:
        print("magic")
    else:
        print("not magic")

else:
    print("not magic")
