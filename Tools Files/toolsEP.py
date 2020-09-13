#  Function isEven takes an integer (a >=0) and returns True if even, and False if odd

def isEven(a):
    
    if a % 2 == 0:
        return True
    return False

# Testing isEven
print(isEven(78))
print(isEven(99))
print(isEven(36))

for i in range(1, 200, 1):
    print(str(i)+" --> "+str(isEven(i)))






# Funciton missing_char takes a string (str) and a number (n)
# and returns a new string where the character at index n has been removed

def missing_char(str, n):
    return str[0:n] + str[n+1:]

# Testing missing_char
print(missing_char('hello', 2))
print(missing_char('goodbye', 6))
print(missing_char('abcdefghijklmnopqrstuvwxyz', 17))






# Binary conversion function; converts a binary input to base 10 output

def base2to10(str):

	n = 0
	total = 0

	for i in range(len(str) - 1, -1, -1):
		total = total + int(str[i]) * 2**n
		n = n + 1

	return total

# Testing base2To10
print(base2to10("101"))
print(base2to10("111111"))
print(base2to10("10111111"))







# Sum of digits inputted (123 --> 1+2+3); Using Mod and Div 10

def sumDigits(a):

	total = 0

	while (a > 0):
		total = total + a%10
		a = a//10
	return total

# Testing sumDigits
print(sumDigits(123))
print(sumDigits(92343))
print(sumDigits(123456789))
