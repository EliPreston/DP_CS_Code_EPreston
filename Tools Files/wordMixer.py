import random


def mixWords(a):
    length = len(a) - 1
    print(length)
    initial = []

    for i in a:
        print(i)
        initial.append(str(i))
    print(initial)

    mixed = []

    for i in initial:

        randNum = random.randint(1, length - 1)

        if i == initial[0]:
            mixed.append(str(i))
        elif i == initial[-1]:
            pass
        else:
            pass

    # print(randNum)
    print(mixed)
    separator = ""
    print(separator.join(initial))


a = "amazing"
mixWords(a)
