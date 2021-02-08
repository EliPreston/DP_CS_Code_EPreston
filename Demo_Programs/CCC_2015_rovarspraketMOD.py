
txt = input()

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

txt = txt.split()

newTxt = ""
for word in txt:

    newWord = ""
    for letter in word:

        newWord += letter

        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "," or letter == "." or letter == ":" or letter == ";" or letter == "?" or letter == "!":
            pass
        elif letter == "0" or letter == "1" or letter == "2" or letter == "3" or letter == "4" or letter == "5" or letter == "6" or letter == "7" or letter == "8" or letter == "9":
            pass
        else:
            letterList = alphabet[letter]
            newLetter = ""

            for i in range(len(letterList)):
                newLetter = newLetter + letterList[i]

            newWord += newLetter

    newTxt = newTxt + newWord + " "

print(newTxt)
