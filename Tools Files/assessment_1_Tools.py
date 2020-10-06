'''
Description; The method takes two lists and adds the strings
in the same index together in any order.
If one list is longer than the other the
none paired indexes should be included in c.

Parameters; String[] a, String[] b

Return; String[]

Pre-conditions; none

Post-conditions; The two passed lists remain unchanged.

'''


# def mergeStrings(a, b):

#     c = []

#     if len(a) == len(b):
#         for i in range(len(a)):
#             c.append(a[i] + b[i])

#     else:

#         longer = a
#         shorter = b

#         if len(b) > len(a):
#             longer = b
#             shorter = a

#         count = 0
#         while count < len(shorter):
#             c.append(longer[count] + shorter[count])
#             count += 1

#         for i in range(len(shorter), len(longer), 1):
#             c.append(longer[i])

#     return c


# # Test cases
# print(mergeStrings(["cat", "dog", "fish"], ["one", "two", "three"]))
# print(mergeStrings(["cat", "dog", "fish"], ["one"]))
# print(mergeStrings(["cat", "dog"], ["one", "two"]))
# print(mergeStrings([], ["one", "two", "three"]))


# #
# #
# #
# #
# #
# #
# #
# #
# #

# '''
# Description; The method takes an array of strings (grocery items in this case) and
# a String and searches the array for a string already in the array that matches it.
# If it finds a match, it returns an affirmation that the item is in the array at
# index n. If not, it returns that the item is not in the array.

# Parameters; Array array, String s

# Return; String ("Item is not on your grocery list." // or // "Item is on grocery list at index " + sL)

# Pre-conditions; array contains only strings, lowercase ,

# Post-conditions;

# '''


# def findS(array, s):
#     # Linear search for a string:
#     # for i in array:
#     #     i.lower()

#     if len(array) == 0:
#         return "Invalid grocery list"

#     if s == "":
#         return "No item check."

#     count = 0
#     for i in range(0, len(array), 1):
#         if array[i] == s:
#             count += 1
#             sL = str(i)

#     if count == 0:
#         return "Item is not on your grocery list."
#     elif count == 1:
#         return "Item is on grocery list at index " + sL
#     elif count > 1:
#         return "Duplicate item on list"


# print(findS(["eggs", "milk", "bread", "jam", "fruit", "vegetables"], "jam"))
# print(findS(["eggs", "milk", "bread", "jam", "fruit", "vegetables"], "jam"))
# print(findS(["eggs", "milk", "bread", "jam", "fruit", "vegetables"], "butter"))
# print(findS(["eggs", "milk", "bread", "jam", "fruit", "vegetables"], ""))
# print(findS([], "jam"))


#
#
#
#
#
#
#
#
#

'''
Description;
Parameters;
Return;
Pre-conditions;
Post-conditions;

Write any tool that incorporates a dictionary. A dictionary
is the data structure we explored when pulling data from an API.
You can find syntax information for Python here,

https://www.w3schools.com/python/python_dictionaries.asp

'''


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
