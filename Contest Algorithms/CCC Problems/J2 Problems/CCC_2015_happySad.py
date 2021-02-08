

message = input()


happy = 0
sad = 0


for i in range(len(message)):

    if message[i] == ":" and message[i+1] == "-" and message[i+2] == ")":
        happy += 1
    elif message[i] == ":" and message[i+1] == "-" and message[i+2] == "(":
        sad += 1

if happy > sad:
    print("happy")
elif sad > happy:
    print("sad")
elif happy > 0 and sad > 0:
    if happy == sad:
        print("unsure")
else:
    print("none")
