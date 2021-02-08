
def rotatingLetters():
    word = input()

    for i in word:
        if i != "I" and i != "O" and i != "S" and i != "H" and i != "Z" and i != "X" and i != "N":
            print("NO")
            return

    print("YES")


rotatingLetters()
