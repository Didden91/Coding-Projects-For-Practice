import random
import time

def playerPlays():

    while True:
        inp = input("Please enter a number between 1 and 1000: ")

        try:
            inp = int(inp)
        except:
            print("Not a number, try again...")
            continue

        if inp <= 0 or inp > 1000:
            print("Number not in range, try again...")
            continue
        break

    return inp

def computerPlays():
    num = random.randint(1,1000)
    return num

def computerPlaysTillWin():
    count = 0
    while True:
        count += 1
        trynumber = random.randint(1, 1000)
        numresult = random.randint(1, 1000)
        print("your number was:",trynumber)
        print("Roll returned:",numresult)
        if trynumber == numresult:
            print("WINNEEERRRRRRRRRRR")
            print("Only took %d tries!!" % count)
            break


while True:

    whoplays = input("Play (y)ourself, let (c)omputer play, let computer play until he (w)ins, or (q)uit: ")

    if whoplays == 'y':
        trynumber = playerPlays()
        numresult = random.randint(1, 1000)
        print("your number was:",trynumber)
        print("Roll returned:",numresult)

    elif whoplays == 'c':
        trynumber = computerPlays()
        numresult = random.randint(1, 1000)
        print("your number was:",trynumber)
        print("Roll returned:",numresult)


    elif whoplays == 'w':
        computerPlaysTillWin()
        print("Thanks for playing")
        break

    elif whoplays == 'q':
        print("Thanks for playing!")
        quit()

    else:
        print("Incorrect input")
        continue
