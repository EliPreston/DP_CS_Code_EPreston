

def convertUnit(u, val):

    if val < 0:
        return -1

    if u == "cm":
        val = val/100

    elif u == "dm":
        val = val/10

    elif u == "mm":
        val = val/1000

    print(str(val) + " meters")


# convertUnit("m", 1471)

# *************************
# def myfunction():
#     return 3+3

# print(myfunction())
# *************************


# def findMeters(val, unit):

#     if val < 0:
#         return -1
#     if unit == "mm":
#         return val/1000
#     elif unit == "cm":
#         return val/100
#     elif unit == "dm":
#         return val/10
#     elif unit == "m":
#         return val/1

#     return -1


# print(findMeters(23325, "mm"))

# *************************************
def convertUnits(val, u1, u2):

    factor = ["mm", "cm", "dm", "m"]

    try:
        v1 = factor.index(u1)
        v2 = factor.index(u2)
    except:
        return -1

    conv = v2 - v1

    return val/(10**conv)


try:
    print(convertUnits(100, "mm", "cm"))
except:
    print("Invalid")


# # def convertUnit(u, h):
# #     if u == "cm":
# #         h = h*10

# #     elif u == "dm":
# #         h = h*100

# #     elif u == "m":
# #         h = h*1000

# #     print(h)


# # convertUnit("m", 1.89)
