'''
Description; The method takes a Strings and returns the string in reverse
Parameters; String s
Return; String
Pre-conditions; s is a valid string of any length.
Post-conditions;

'''


def reverseWordA(s):

    a = ""

    for i in range(len(s) - 1, -1, - 1):
        a += s[i]
    print(a)


s = "cat"
reverseWordA(s)


'''
Using a list method
'''
# def reverseWordA(s):

#     reverse = []

#     # notation for slicing(start, stop, step) this reverses through the string in this case
#     for i in range(len(s) - 1, - 1, - 1):
#         l = s[i]
#         reverse.append(l)

#     print("".join(reverse))


# s = "cat"
# reverseWordA(s)
