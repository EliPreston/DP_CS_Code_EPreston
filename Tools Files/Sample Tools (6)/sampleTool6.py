'''
Description; The method takes a list of Strings and returns a new string of each word constructed in reverse
Parameters; String[] s
Return; String
Pre-conditions; s is a list of any length and it contains strings of any length
Post-conditions;

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
