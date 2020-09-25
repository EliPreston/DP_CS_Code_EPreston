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
Take the passed file name and list, then copys the contents into the file


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
writeListToFile2("test1.txt", l)
