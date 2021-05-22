import random
import time

loops = 10

while loops > 0:


    maxheight = random.randint(10,200)
    maxheightstart = maxheight
    # print("Max height will be:",maxheight)

# for iter in range(1,10):
#     print(iter*':')

    while maxheight > 0:
        print(maxheight*':')
        maxheight = maxheight - 1
        time.sleep(0.003)

    while maxheight < maxheightstart:
        print(maxheight*':')
        maxheight = maxheight + 1
        time.sleep(0.003)


    loops = loops - 1
