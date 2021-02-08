# THE SORT ALGORITHM IS THE LAST PART OF THIS CONTEST PROBLEM


# This was the problem of reading a file and the printing the tallest people
# from that list of people (given name, height, and unit of measurement).

# In order to do this, I created a dictionary which held the names and heights
# of everyone in the file, and then from this dictionary I sorted it based
# on the VALUE of the KEY: VALUE pairs.

# sorted_keys = sorted(heightDictionary, key=heightDictionary.get, reverse=True)
#  for w in sorted_keys:
#         sorted_dict[w] = heightDictionary[w]

# This method sorts from smallest to largest, so putting the reverse=True means
# the sort is from largest to smallest instead.


# Then, I looped through the first n KEYS and printed those names, which were the tallest people.
#  for i in list(sorted_keys)[0:5]:
# print(i)


def dictionaryTry():

    # **********************************************************
    # The txt file is opened and read. The first line is read (an integer) and that then
    # tells the for loop how many lines to read next. For each line in the file, the name, height,
    # and unit of measurement for the height are appended to respective lists.

    file = open("DWITE_tallestTEST.txt", "r")
    lines = int(file.readline())

    name = []
    height = []
    unit = []

    for i in range(0, lines, 1):

        temp = file.readline().replace("\n", "")
        temp = temp.split(" ")

        name.append(temp[0])
        height.append(temp[1])
        unit.append(temp[2])


# **********************************************************
# This takes the height and unit lists that have been created and loops through
# both, getting the unit (which if not already meters) and converting teh corresponding
# height into meters before replacing the value with the new converted value.

    for i in range(0, len(name), 1):

        u = unit[i]
        h = height[i]
        h = float(h)

        if u == "cm":
            h = h/100
            h = round(h, 3)
            height[i] = h

        elif u == "dm":
            h = h/10
            h = round(h, 3)
            height[i] = h

        elif u == "mm":
            h = h/1000
            h = round(h, 3)
            height[i] = h

        height[i] = h

# **********************************************************
# This creates a dictionary of KEY: VALUE pairs, with the key being the names
# of the people, and the value being the height (which is stored as a float).

    heightDictionary = {}

    for i in range(0, len(height), 1):

        nameI = name[i]
        heightI = height[i]
        heightI = float(heightI)

        heightDictionary[nameI] = heightI


# **********************************************************
# This portion takes the dictionary of names and the corresponding heights that has been created,
# and sorts it based on the value of the KEY: VALUE pairs in the dictionary.
# This new sorted dictionary is then looped through to get the first 5 KEYS, which are the
# names of the people.

    sorted_dict = {}
    sorted_keys = sorted(
        heightDictionary, key=heightDictionary.get, reverse=True)

    for w in sorted_keys:
        sorted_dict[w] = heightDictionary[w]

    for i in list(sorted_keys)[0:5]:
        print(i)


dictionaryTry()
