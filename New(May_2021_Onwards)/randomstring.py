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

# slotnumber == 0
# for slot in range(len(newlist)):
#     for item in newlist:
#     if item == newlist[-1]:
#         print("last item is:", item)
#         break
#     slotnumber += 1

print("slot 3 is: ", newlist[3])
print("Slot 3:3+2 = ", newlist[3:3+2])

endstring = ''.join(newlist)
print("End result is", endstring)
