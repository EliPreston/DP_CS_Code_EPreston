# # # THIS FILE IS USED TO BUILD AND TEST TOOLS FILES


# n = 10

# for k in range(1, n):
#     for j in range(1, n):
#         if k == j:
#             k = str(k)
#             print("k is " + k)

N = 10
while (k < N):
    k += 1
    j += 1

    # # See bottom for theory:

    # def base10toBase2(n):

    #     result = ""

    #     while (n > 0):

    #         result = str(n % 2) + result
    #         n = n // 2

    #     return result

    # print(base10toBase2(45))

    # def base10toBaseB(n, b):

    #     result = ""

    #     while (n > 0):

    #         result = str(n % 3) + result
    #         n = n // b

    #     return result

    # print(base10toBaseB(11, 3))

    # # #
    # # #
    # # #
    # # #
    # # #
    # # #
    # # #
    # # #
    # # #
    # # #
    # # #
    # # #
    # # #
    # # #
    # # #
    # # #
    # # #
    # # #

    # # # def maxMinSumAvg(lst):

    # # #     MAX = lst[0]
    # # #     MIN = lst[0]
    # # #     SUM = 0
    # # #     AVG = 0

    # # #     for i in lst:
    # # #         if i > MAX:
    # # #             MAX = i
    # # #         elif i < MIN:
    # # #             MIN = i
    # # #         else:
    # # #             pass

    # # #         SUM += i
    # # #         print(i)

    # # #     length = len(lst) + 1
    # # #     # Do + 1 because otherwise its going to divide the sum by 9, but there's 10 numbers (starts at 0, 1, 2, 3 for indices)

    # # #     print(length)
    # # #     AVG = SUM/length

    # # #     print(MAX, MIN, SUM, AVG)

    # # # lst = [234, 2, 4, 3, 274, 78, 12, 90, 144]
    # # # maxMinSumAvg(lst)


def vendingMachine():

    vm = {
        'A1': {'item': "Lays Chips", "price": "1.50"},
        'A2': {'item': "Ketchup Chips", 'price': "1.75"},
        'B1': {'item': "Kitkat", 'price': "2.00"},
        'B2': {'item': "Snickers", 'price': "2.00"},
        'C1': {'item': "Water", 'price': "2.50"},
        'C2': {'item': "Milk", 'price': "1.75"}
    }

    for i in vm:
        print(i)
        for n, m in vm[i].items():
            print(n, " --> ", m)
        print("-----")

    selection = input("What would you like? Please select a location.\n")

    for item in vm:
        if item == selection:
            print("Item is available.")
            # print(vm['A1']['item'])
            break
        # else:
            # print("invalid selection")
            # break
        if item != selection:
            print("invalid selection")

    # for i in vm['A1']:
    #     print(i)

    # for i in vm:
    #     # print(i)
    #     for d in vm[i]:
    #         print(d[])
    # print(vm['A1']['item'])

    # select = input(("What item would you like? Choose a location.\n"))

    # if select in vm:
    #     print("available")
    # else:
    #     print("unavailable")


# d = {
#     'dict1': {'foo': 1, 'bar': 2},
#     'dict2': {'baz': 3, 'quux': 4}}

# for i in d:
#     for j, k in d[i].items():
#         print(j, "->", k)


vendingMachine()
