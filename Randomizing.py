import random
import time

l = list()

def getWinners(d, u, w):


    for i in range(1,d):
        x = random.randint(1, u)
        print(x)
        if x >= w:
            print("WINNERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
            time.sleep(1)
            l.append(x)
    return l


draws = int(input("How many numbers should I draw? "))
numcap = int(input("Upper bound number? "))
wincap = int(input("How high a number constitutes a winner, needs to be below %s ... " % numcap))

winlist = getWinners(draws,numcap,wincap)

print(winlist)

winpercent = (numcap - wincap) / numcap
expectedwins = winpercent * draws

print('Win chance should be:', winpercent * 100, "%")
print('Expected amount of wins:', expectedwins)
print('Actual amount of wins:', len(winlist))
print('Actual win percentage:', (len(winlist) / draws) * 100, "%")
