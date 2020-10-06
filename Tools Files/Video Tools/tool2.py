'''
Description; The method takes a string and jumbles the indexes 
Parameters; String s
Return; String
Pre-conditions; s is a string of any length.
Post-conditions; Initial string is unchanged
'''

import random
# This is importing a module which can be called, this is an example of abstraction


def mixWords(string):
    # This is the function header, it declares the funciton and states that it takes one variable (string)

    # If statement checks if the length of the string is greater than 1
    if len(string) > 1:

        # Assignment: Declares mixed and initializes it to ""
        mixed = ""

        # Assignment: Initializes an empty list
        s = []

        # Counted loop: Loops through each index of the string and appends it to the list s
        for i in string:
            s.append(i)

        # Counted loop: Loops from 0 to the length of list s
        for i in range(0, len(s)):
            # Uses the random module to get a random integer that is within
            # the length of list s. It then adds the string at the random index
            # to  "mixed".
            mixed += s.pop(random.randint(0, len(s) - 1))

        # Prints the mixed String
        print(mixed)

    # Other end of the if statement, in this case if the length of the string is
    # 1 or less, then it won't make a difference to run the rest of the code
    else:
        print("Won't make a difference.")


s = "word"
mixWords(s)
