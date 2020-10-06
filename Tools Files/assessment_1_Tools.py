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


def mergeStrings(a, b):

    c = []

    if len(a) == len(b):
        for i in range(len(a)):
            c.append(a[i] + b[i])

    else:

        longer = a
        shorter = b

        if len(b) > len(a):
            longer = b
            shorter = a

        count = 0
        while count < len(shorter):
            c.append(longer[count] + shorter[count])
            count += 1

        for i in range(len(shorter), len(longer), 1):
            c.append(longer[i])

    return c


# Test cases
print(mergeStrings(["cat", "dog", "fish"], ["one", "two", "three"]))
print(mergeStrings(["cat", "dog", "fish"], ["one"]))
print(mergeStrings(["cat", "dog"], ["one", "two"]))
print(mergeStrings([], ["one", "two", "three"]))


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
Description; The method takes an array of strings (grocery items in this case) and
a String and searches the array for a string already in the array that matches it.
If it finds a match, it returns an affirmation that the item is in the array at
index n. If not, it returns that the item is not in the array.

Parameters; Array array, String s

Return; String ("Item is not on your grocery list." // or // "Item is on grocery list at index " + sL)

Pre-conditions; array contains only strings, lowercase ,

Post-conditions;

'''


def findS(array, s):
    # Linear search for a string:
    # for i in array:
    #     i.lower()

    if len(array) == 0:
        return "Invalid grocery list"

    if s == "":
        return "No item check."

    count = 0
    for i in range(0, len(array), 1):
        if array[i] == s:
            count += 1
            sL = str(i)

    if count == 0:
        return "Item is not on your grocery list."
    elif count == 1:
        return "Item is on grocery list at index " + sL
    elif count > 1:
        return "Duplicate item on list"


print(findS(["eggs", "milk", "bread", "jam", "fruit", "vegetables"], "jam"))
print(findS(["eggs", "milk", "bread", "jam", "fruit", "vegetables"], "jam"))
print(findS(["eggs", "milk", "bread", "jam", "fruit", "vegetables"], "butter"))
print(findS(["eggs", "milk", "bread", "jam", "fruit", "vegetables"], ""))
print(findS([], "jam"))


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
Description; Prints out the items in a nested dictionary
Parameters; A nested list
Return; A printed version of the nested dictionaries
Pre-conditions; Valid dictionary
Post-conditions; n/a

'''


def vendingMachine(array):

    for i in vm:
        print(i)
        for n, m in vm[i].items():
            print(n, " --> ", m)
        print("-----")

    print("These are the items currently in stock in the vending machine.")


vm = {
    'A1': {'item': "Lays Chips", "price": "1.50"},
    'A2': {'item': "Ketchup Chips", 'price': "1.75"},
    'B1': {'item': "Kitkat", 'price': "2.00"},
    'B2': {'item': "Snickers", 'price': "2.00"},
    'C1': {'item': "Water", 'price': "2.50"},
    'C2': {'item': "Milk", 'price': "1.75"}
}
vendingMachine(vm)
