import random

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
    print(newlist)

for item in newlist:
    if item == len(newlist)
    if item == item[+1]:
        print("FOUND a double", item)

endstring = ''.join(newlist)
print("End result is", endstring)
