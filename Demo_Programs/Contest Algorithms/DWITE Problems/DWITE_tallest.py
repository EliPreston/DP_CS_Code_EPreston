

# OLIVER'S SOLUTION
# N=int(input())
# people=[]
# cons={"m":1, "dm":0.1, "cm":0.01, "mm":0.001}

# for i in range(N):
#     people.append(input().split())

myfile = open("DWITE_tallest.txt", "r")
item = myfile.read().split("\n")
N = int(item[0])
people = []

for i in range(1, N+1):
    people.append(item[i].split())

cons = {"m": 1, "dm": 0.1, "cm": 0.01, "mm": 0.001}
myfile.close()


for i in range(N):
    people[i][1] = float(people[i][1])*cons[people[i][2]]

people.sort(key=lambda x: x[1])
# print(people)

for i in range(N-1, N-6, -1):
    print(people[i][0])


# MY SOLUTION
# def dictionaryTry():

#     file = open("DWITE_tallestTEST.txt", "r")
#     lines = int(file.readline())

#     name = []
#     height = []
#     unit = []

#     for i in range(0, lines, 1):

#         temp = file.readline().replace("\n", "")
#         temp = temp.split(" ")

#         name.append(temp[0])
#         height.append(temp[1])
#         unit.append(temp[2])

#     for i in range(0, len(name), 1):

#         u = unit[i]
#         h = height[i]
#         h = float(h)

#         if u == "cm":
#             h = h/100
#             h = round(h, 3)
#             height[i] = h

#         elif u == "dm":
#             h = h/10
#             h = round(h, 3)
#             height[i] = h

#         elif u == "mm":
#             h = h/1000
#             h = round(h, 3)
#             height[i] = h

#         height[i] = h

#     heightDictionary = {}
#     for i in range(0, len(height), 1):

#         nameI = name[i]
#         heightI = height[i]
#         heightI = float(heightI)

#         heightDictionary[nameI] = heightI

#     sorted_dict = {}
#     sorted_keys = sorted(
#         heightDictionary, key=heightDictionary.get, reverse=True)

#     for w in sorted_keys:
#         sorted_dict[w] = heightDictionary[w]

#     for i in list(sorted_keys)[0:5]:
#         print(i)


# dictionaryTry()
