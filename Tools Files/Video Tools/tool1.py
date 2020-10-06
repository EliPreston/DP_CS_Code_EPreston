'''
Description; The method sums the even numbers of the fibonacci sequence
that are less than the inputted value

Parameters; Integer n
Return; Integer SUM
Pre-conditions; n is an Integer
Post-conditions; n/a
'''


def evenFibonacci(n):
    # Function header

    # Could use this method of casting (changing type) to make sure n is an integer
    # n = int(n)

    # Initializes the list "sequence" with values 1 and 2
    sequence = [1, 2]

    # Declares SUM and sets it to 0
    SUM = 0

    # While loop: In this case the while loop states that while the last index
    # of "sequence", obtained by going to the negative index, is greater than
    # the number inputted, the loop will run
    while sequence[-1] < n:

        # Initializes "nxt" and adds the last two numbers in the list "sequence",
        # again gotten by going into the negative indices.
        nxt = sequence[-1] + sequence[-2]

        # Appends the variable nxt to end of list sequence, and then goes back to the top of the loop.
        sequence.append(nxt)

    # After the loop has been exited, because the number at the last index of "sequence" is
    # already there, it has to be deleted as it exceeds the cut off number inputted
    del sequence[-1]

    # For loop: Loops through each value in "sequence", getting the value
    for i in sequence:

        # If statement: checks if the value i is even. It does this using the modulo operator.
        # It returns the remainder of the value i when divided by 2, this is an easy check as
        # to whether it is an even number because if the remainder is 0 then it is even.
        if i % 2 == 0:

            # If the number is even, it is added to the SUM. Then it returns to the top of the loop
            # and does this for each number in "sequence".
            SUM += i

    # When the loop finally ends, the SUM is returned
    return SUM


print(evenFibonacci(4000000))
