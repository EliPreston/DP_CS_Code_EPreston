

word = input()


#                      key(a string) :       value (a list)
# dictionary setup --> consonant: [closest vowel, next consonant]
alphabet = {
    'b': ["a", "c"],
    'c': ["a", "d"],
    'd': ["e", "f"],
    'f': ["e", "g"],
    'g': ["e", "h"],
    'h': ["i", "j"],
    'j': ["i", "k"],
    'k': ["i", "l"],
    'l': ["i", "m"],
    'm': ["o", "n"],
    'n': ["o", "p"],
    'p': ["o", "q"],
    'q': ["o", "r"],
    'r': ["o", "s"],
    's': ["u", "t"],
    't': ["u", "v"],
    'v': ["u", "w"],
    'w': ["u", "x"],
    'x': ["u", "y"],
    'y': ["u", "z"],
    'z': ["u", "z"]
}


newWord = ""

for letter in word:
    # print(letter)

    newWord += letter

    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        pass
    else:

        letterList = alphabet[letter]
        newLetter = ""

        for i in range(len(letterList)):
            # print(letterList[i])

            newLetter = newLetter + letterList[i]
            # print(newLetter)

        # print(newLetter)
        # print(letter + newLetter)

        newWord += newLetter


print(newWord)
