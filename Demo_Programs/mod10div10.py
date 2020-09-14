
# # Any number Mod 10 (x%10) gives you ONLY the units digit
# x = 327343%10
# print(x)

# # Any number Div 10 (y//10) chops off ONLY the units digit
# y = 123232//10
# print(y)


# # This takes the initial number and mods it by 10, giving the units value (in this case 5),
# # then by integer dividing 375 it chops off the units value leaving 34 as the new num.
# # This process then repeats until the number integer divded by 10 is 0 at which point it stops.
# # This allows you to access each of the digits in the number


# a = 123
# total = 0
# while (a > 0):
#     total = total + a%10
#     a = a//10
# print(total)



num = 375
total = 0

while (num > 0):
    # print(num%10)
    total = total + num%10
    num = num//10

total = str(total)
print("Digits In Number Added Together = " + total)