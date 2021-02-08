
def countVotes():

    # v = int(input())
    l = input()

    aCount = 0
    bCount = 0

    for i in l:
        if i == "A":
            aCount += 1
        else:
            bCount += 1

    if aCount > bCount:
        print("A")
        return
    elif aCount == bCount:
        print("Tie")
        return
    print("B")
    return


countVotes()
