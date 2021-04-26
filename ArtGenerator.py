from art import *
import time


def GenRandomArt():
    art_1 = art("random")
    print(art_1,"\n")
    time.sleep(0.5)

loops = input("How many beautiful pieces of art do you wish to generate? ")
artnumber = 0

start_time = time.time()

try:
    loops = int(loops)
except:
    print("Wrong input, exiting...")
    quit()

while loops >= 1:
    artnumber += 1
    print("This is artwork number:",artnumber)
    GenRandomArt()
    loops -= 1

print("Generating this art gallery took approximately %s seconds" % (time.time() - start_time))
