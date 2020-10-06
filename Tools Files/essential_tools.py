# Essential Tools


'''
Description; This method takes a base 10 value, and converts it to a base 2 value
Parameters; Integer n
Return; String result
Pre-conditions; n/a
Post-conditions; n/a

'''


def base10ToBase2(n):

    result = ""

    while n > 0:

        result = str(n % 2) + result
        n = n//2

    return result


print(base10ToBase2(53))
print(base10ToBase2(62))
print(base10ToBase2(45))


#
#
#
#


'''
Description; This method takes a base 2 value in string form, and converts it to a base 10 value
Parameters; String str
Return; String total
Pre-conditions; String can only contain 0s and 1s (valid base 2 values)
Post-conditions; n/a

'''


def base2to10(str):

    n = 0
    total = 0

    for i in range(len(str) - 1, -1, -1):
        total = total + int(str[i]) * 2**n
        n = n + 1

    return total


# Testing base2To10
print(base2to10("101"))
print(base2to10("111111"))
print(base2to10("10111111"))
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
Description:  This function takes a string, representing a binary value.
If s is invalid then the function returns "-1"
Parameter: String s
Return: String result
precoditions: n/a
postconditions: n/a
'''


def base2ToHex(s):

    HEX = ["0", "1", "2", "3", "4", "5", "6", "7",
           "8", "9", "A", "B", "C", "D", "E", "F"]

    # Assignment Statement: Declares result and initializes it to ""
    # This line stores the resulting Hex value that is returned
    result = ""

    # This line adds the appropriate amount of zeros to make the length of s divisible by 4
    # Python Specific: 2 * "str" = "strstr"
    s = (4 - len(s) % 4) * "0" + s

    # Counted loop: Looping through s in increments of 4
    for i in range(0, len(s), 4):

        # Using substring string to access 4 characters at a time and store the result in v
        v = s[i: i + 4]

        # Accesses each index of v and multiplies it by the corresponding power of 2
        # to generate base 2 value of the 4 digits
        # Casting strings to integer values. Casting is the process of changing type.
        index = int(v[0])*8 + int(v[1])*4 + int(v[2])*2 + int(v[3])*1

        # By converting the 4 digit base 2 number to base 10, can use that as the index in
        # HEX to get the value.
        result = result + HEX[index]

    return result


BIN = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111",
       "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"]

for i in range(0, len(BIN), 1):
    print(base2ToHex(BIN[i]))


print(base2ToHex("1011110101"))
print(base2ToHex("1110111110110"))
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
Description; This method takes a hexadecimal value and converts it to a base 2 value
Parameters; String s (hex value)
Return; String result (base 2 value)
Pre-conditions; Valid hexadecimal characters used
Post-conditions; n/a

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
Description; This method takes an integer and adds up each digit, returning the sum
Parameters; Integer a
Return; Integer total
Pre-conditions; valid input
Post-conditions; n/a

'''


def sumDigitsA(a):

    total = 0

    while (a > 0):
        total = total + a % 10
        a = a//10
    return total


# Testing sumDigits
print(sumDigitsA(-123))
print(sumDigitsA(92343))
print(sumDigitsA(123456789))
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
Description; The method takes a list of integers and returns the sum of all the elements that are multiples of 3
Parameters; int[] data
Return; int
Pre-conditions; data is a list of integers. 
Post-conditions; n/a

'''


def findModSum1(lst):

    SUM = 0

    for i in lst:
        if i % 3 == 0:
            SUM += i
        # else:
        #     pass
    print(SUM)


lst = [234, 346, 67, 46, 43, 487, 21, 3, 9, 6]
lst2 = [21, 4, 6, 9, 10, 12]
findModSum1(lst)
findModSum1(lst2)
#
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
Description; The method takes a list of integers and two integer values, returning the sum of all the elements that are between a (exclusive) and b (exclusive)
Parameters; int[] arr, int a, int b
Return; int
Pre-conditions; arr is a list of integers 
Post-conditions; n/a

'''


def findModSum2(lst, a, b):

    SUM = 0
    MIN = min(a, b)
    MAX = max(a, b)

    for i in lst:
        if MIN + 1 <= i <= MAX - 1:
            SUM += i
        # else:
        #     pass
    print(SUM)


lst = 2, 3, 10, 9, 14, 25, 3, 100
a = 25
b = 5
findModSum2(lst, a, b)
#
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
Description; The method takes a list of integers and two integer values then returns the sum of all the elements that are multiples of a and b
Parameters; int[] values, int a, int b
Return; int
Pre-conditions; values is a list of integers of any size and a and b are valid positive integer values.
Post-conditions; n/a

'''


def findModSum3(lst, a, b):

    SUM = 0
    for i in lst:
        if i % a == 0 and i % b == 0:
            SUM += i
        else:
            pass

    print(SUM)


lst = [21, 30, 10, 99, 14, 2, 100]
a = 5
b = 2
findModSum3(lst, a, b)
#
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
Description; The method takes a list of doubles and returns the sum of the digits.
Parameters; double[] data
Return; int
Pre-conditions; valid list
Post-conditions; none

'''


def findModSum4(lst):

    NUMS = []
    SUM = 0

    for i in lst:
        i = str(i)
        i = i.replace('.', '')
        NUMS.append(str(i))

    for i in NUMS:
        num = int(i)

        while num > 0:
            SUM += num % 10
            num = num // 10
    print(SUM)


lst = [1.2, 3.14, 7.89]
findModSum4([1.2, 3.14, 7.89])
#
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
Description; The method takes a Strings and returns the string in reverse
Parameters; String s
Return; String
Pre-conditions; s is a valid string of any length.
Post-conditions; none

'''


def reverseWordA(s):

    a = ""

    for i in range(len(s) - 1, -1, - 1):
        a += s[i]
    print(a)


s = "cat"
reverseWordA(s)
#
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
Description; The method takes a list of Strings and returns a new string of each word constructed in reverse
Parameters; String[] s
Return; String
Pre-conditions; s is a list of any length and it contains strings of any length
Post-conditions; none

'''


def reverseWordB(lst):

    both = []
    for i in lst:
        reverse = []

        # notation for slicing(start, stop, step) this reverses through the string in this case
        for x in range(len(i) - 1, - 1, - 1):
            l = i[x]
            reverse.append(l)
            both.append(l)

    print("".join(both))


lst = ["cat", "dog", "cow"]
reverseWordB(lst)
#
#
#
#
#
#
#
#
#
#
#
