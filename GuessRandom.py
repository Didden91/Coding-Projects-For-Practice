import random
import time

c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


userchoice = input("Please choose a number between 1 and 10: ")

try:
    userchoice = int(userchoice)
except:
    print("Wrong input, exiting...")
    quit()

y = random.randint(1, 10)

print("Now to rollllll the dice.....")
time.sleep(1)
print("...")
time.sleep(1)
print("..")
time.sleep(1)
print(".")
time.sleep(1)
print("Your choice was...",userchoice)
time.sleep(1)
print("The roll returned...",y)
time.sleep(1)

if y == userchoice:
    print("CONGRATULATIONS YOU WON")
else:
    print("Too bad, you LOST")


