'''
Description; The method takes a string and jumbles the indexes 
Parameters; String s
Return; String
Pre-conditions; s is a string of any length.
Post-conditions; 
'''

import random


def mixWords(word):

    if len(word) > 1:
        mixed = ""
        s = []
        for i in word:
            s.append(i)

        for i in range(0, len(s)):
            mixed += s.pop(random.randint(0, len(s) - 1))

        print(mixed)
    else:
        print("Won't make a difference.")


a = "word"
mixWords(a)
