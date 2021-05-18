import random

while True:
    unum = input("please enter a number:")
    if unum == 'done':
        break
    unum = float(unum)
    result = random.randint(0, unum)
    print(result)
