def evenFibonacci(n):

    sequence = [1, 2]
    SUM = 0

    # while last value in list is less than n
    while sequence[-1] < n:

        nxt = sequence[-1] + sequence[-2]
        sequence.append(nxt)

    del sequence[-1]

    for i in sequence:

        if i % 2 == 0:
            SUM += i
    return SUM


print(evenFibonacci(4000000))
