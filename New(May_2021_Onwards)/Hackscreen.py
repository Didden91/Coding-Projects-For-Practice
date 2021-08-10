import random
import time

def makeSpacesAround(printspot):
    # number between 0 and 237
    # how many spaces before, and how many after
    # case, number is 5
    # 237  = number

    #number itself -1 is spaces BEFORE
    #237 - number - 1 = spaces AFTER
    #if number = 0, no spaces
    #if number = 237, no minus 1, 236 spaces

    spaces = " "
    if printspot == 0:
        for x in range(random.randint(1,20)):
            print(randomchar())
            time.sleep(0.015)
    elif printspot == 237:
        for x in range(random.randint(1,20)):
            print(spaces*235,randomchar()) # takes space after comma into consideration by using 235
            time.sleep(0.015)
    else:
        for x in range(random.randint(1,20)):
            print(spaces*(printspot-1),randomchar(),spaces*(230-printspot-1))
            time.sleep(0.015)



def pickspot():
    x = random.randint(0,237)
    return x

def randomchar():
    c = random.randint(200,1000)
    return chr(c)

inp = input("how many lines? ")

for x in range(int(inp)):
    makeSpacesAround(pickspot())



# numbers = "0000000000"
# ones = "1111111111"
# twos = "2222222222"
# threes = "3333333333"
# fours = "4444444444"
# fives = "5555555555"
#
#
# print(spaces*10,"test",spaces*30,"nogeentest")
#
# print(numbers*4,ones*4,twos*4,threes*4,fours*4,fives*4)
#
# print(chr(0),chr(1),chr(2),chr(3),chr(4),chr(5), chr(1284))
#
# # 40 * 5
# # + 5
# # + 32
# # 237 slots
