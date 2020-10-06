
def pokerHands():

    l = []
    file = open("poker.txt", "r")
    contents = file.read()

    for line in contents:
        # print(line)

        if line == "\n":
            pass
        else:
            l.append(line)


'''

Reads and prints each line of a file

if data.find('!masters') != -1:
     f = open('masters.txt')
     lines = f.read().splitlines()
     f.close()
     for line in lines:
         print line
         sck.send('PRIVMSG ' + chan + " " + str(line) + '\r\n')
'''
