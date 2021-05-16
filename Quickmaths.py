import time
import random
from threading import Timer

def testje():
    print("testje!")

t = Timer(5.0, testje)
t.start()

def generator():
    oper = random.randint(1,4)
    left = random.randint(1,20)
    right = random.randint(1,20)
    if oper == 1:
        answer = left + right
        quest = '%d + %d' % (left, right)
        task = 'ADDITION'
    elif oper == 2:
        answer = left - right
        quest = '%d - %d' % (left, right)
        task = 'SUBTRACTION'
    elif oper == 3:
        answer = left * right
        quest = '%d X %d' % (left, right)
        task = 'MULTIPLICATION'
    else:
        answer = left / right
        quest = '%d : %d' % (left, right)
        task = 'DIVISION'
    return task, quest, answer

lives = 3

print("Hello and welcome!")
time.sleep(0.5)
print("Time to do some quick maths")
time.sleep(0.5)
# print("You get 3 seconds to answer, and three lives.")
# time.sleep(0.5)
print("Good luck!")
time.sleep(0.5)
print("Let's get started!")
time.sleep(0.5)
print("The first assignment is...")

while True:

    while lives > 0:

        problem = generator()
        print(problem[0])
        print('What is:',problem[1])
        inp = input("Answer: ")
        try:
            inp = int(inp)
        except:
            print("ERROR")
            quit()
        if inp == problem[2]:
            print("CORRECT!")
            print("The next assignment is...")
        else:
            print("INCORRECT!")
            print("The correct answer was",problem[2])
            lives -= 1
            print("You lost a life, and have %d remaining" % lives)

    print("You have no lives remaining, you lose :(")
    break
