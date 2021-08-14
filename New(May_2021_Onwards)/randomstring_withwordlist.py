import random

fhand = open('woordenHARD.txt')
wordlist = list()

for allwords in fhand:
    words = allwords.split()
for word in words:
    wordlist.append(word)


while True:
    inp = input("Length of string? ")
    try:
        inp = int(inp)
        break
    except:
        print("Not an integer, try again")

print("string will be %d characters long" % inp)

alf = "abcdefghijklmnopqrstuvwxyz"
newlist = list()
for i in range(inp):
    picknum = random.randint(0,25)
    newlist.append(alf[picknum])

endstring = ''.join(newlist)
print("End result is", endstring)

itemslot = 0
record = 0
for item in range(len(newlist)):
    # print("Current item:", newlist[item])
    # print("This was in slot number: ", itemslot)
    try:
        test = newlist[itemslot+1]
    except:
        break
    score = 1
    x = 1
    while newlist[item] == newlist[itemslot+x]:
        score += 1
        x += 1
        try:
            test = newlist[itemslot+x]
        except:
            break
    if score > record:
        record = score
        print("new record = ", record)
        print("found @ itemslot %d upto itemslot %d " % (itemslot, itemslot+x))
        rfis, rlis = itemslot, itemslot+x

    itemslot += 1


print("Record chain of same characters is: %d! It was a chain of \"%s\" characters! This chain can be found @ itemslot %d upto itemslot %d" % (record, newlist[rfis], rfis, rlis))
print("Now to check for existing words...")

wordsfound = list()
longestword = ''
for item in wordlist:
    if len(item) < 6:
        pass
    elif item in endstring:
        print("Found the word:",item)
        wordsfound.append(item)
        if len(item) > len(longestword):
            longestword = item


print("I found these existing words", wordsfound)
print("Longest word I found was \"%s\", which was %d letters long" % (longestword, len(longestword)))
