import math

# Reads the contents of the file name passed and copys it to a list, then returns that list
'''
Description;
Parameters;
Return;
Pre-conditions;
Post-conditions;

'''


def readFileToList(name):

    l = []
    file = open(name, "r")
    contents = file.read()

    for i in contents:
        if i == "\n":
            pass
        else:
            l.append(i)
    print(l)
    file.close()


readFileToList("../../API_KEYS/readFile.txt")


'''
Description;
Parameters;
Return;
Pre-conditions;
Post-conditions;

'''
# Take the passed file name and list, then copys the contents into the file


def writeListToFile1(name, lst):

    file = open(name, "w")
    for i in lst:
        file.write(str(i) + "\n")
    # file.close()


l = ["hola", "salut", "hi", "hello", "goodbye", "see you later"]
writeListToFile1("test1.txt", l)


def writeListToFile2(name, lst):

    file = open(name, "w")

    for i in range(0, len(lst)):
        lst[i] = int(lst[i])
    lst.sort()

    for i in lst:
        file.write(str(i) + "\n")
    # file.close()


l = ["243", "235", "43", "57", "2124", "73"]
writeListToFile2("test.txt", l)


def findReverse(num):

    rN = ""
    if num > 2:
        num = str(num)
        for i in range(len(num) - 1, - 1, - 1):
            rN = rN + num[i]
    print(rN)


num = 3356378424729
findReverse(num)


'''
Description; Takes two real arguments that represent the two legs of a right triangle, returns the hypotenuse
Parameters; int int or str str
Return; int
Pre-conditions;
Post-conditions;

'''


def findHyp(a, b):

    a = int(a) ** 2
    b = int(b) ** 2
    c = math.sqrt(a + b)

    hyp = round(c, 2)
    print(hyp)
    # print("The hypotenuse is " + str(hyp))


findHyp(3, 3)


'''
Description; Takes a string that represents a Hex value and converts it to base 2
Parameters; String s
Return; String
Pre-conditions; S contains only hex characters
Post-conditions;

'''


def hexToBase2(s):

    HEX = ["0", "1", "2", "3", "4", "5", "6", "7",
           "8", "9", "A", "B", "C", "D", "E", "F"]
    BIN = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111",
           "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"]

    result = ""

    for n in range(len(s) - 1, - 1, -1):
        for i in range(0, len(HEX), 1):
            if (HEX[i] == s[n]):
                result = BIN[i] + result
                break
    return result


print(hexToBase2("0F0F0F"))


def findX(array, x):
    # Linear search for an integer:

    x = int(x)

    for i in range(0, len(array), 1):
        # print(i)

        if array[i] == x:
            return "Element present at index " + str(i)
    return "not here"


print(findX([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))
print(findX([1, 2, 3, 4, 5, 6, 7, 8, 9], 8))
print(findX([1, 2, 3, 4, 5, 6, 7, 8, 9], 0))
