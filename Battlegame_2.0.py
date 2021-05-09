from art import *
import random
import time



rollresult = 0
strongaccroll = 0
carefulaccroll = 0
recklessaccroll = 0
enemyroll = 0
enemychoice = 0
playerscore = 0
enemyscore = 0
par = list()
cacount = 0
cahit = 0
camiss = 0
sacount = 0
sahit = 0
samiss = 0
racount = 0
ramiss = 0
rahit = 0

def accroll(accuracy):

    accroll = random.randint(1, 10)
    if accroll <= accuracy:
        rollresult = 1
        return rollresult
    else:
        rollresult = 0
        return rollresult

def logandprint(strinput,fhandname):
    print(strinput)
    fhandname.write(strinput)
    fhandname.write("\n")


#        print("Your attack was a",accresult,"!")

#        if accresult == 'HIT':
#            return power
#
#        else:
#            power = 0
#            return power
#
#        print("You did",power,"DAMAGE!")

#strongattackdmg = 50
#strongattackacc = 3

#carefulattackdmg = 20
#carefulattackacc = 8

#recklessattackdmg = 90
#recklessattackselfdmg = 30
#recklessattackacc = 1

randfilenumb = time.ctime()
randfilenumb = randfilenumb.replace(":","")
randfilename = randfilenumb + ' log.txt'
fhand = open(randfilename, 'w')

fhand.write("Start of new log:\n")

while True:

#    randfilenumb = random.randint(1000, 10000)
#


    enemyhp = 100
    playerhp = 100
    tprint("OH     NOOOOOOOOOOOOOOO")
    time.sleep(1)
    tprint("AN      ENEMY      APPEARED")
    time.sleep(1)
    fhand.write("START OF NEW ROUND\n")

    while enemyhp > 0 and playerhp > 0:

        while True:
            userchoice = input("Choose an attack:\nSTRONG (S) or CAREFUL (C) or RECKLESS (R): ")
            if userchoice in ('S', 's', 'C', 'c', 'R', 'r'):
                break

            else:
                time.sleep(0.5)
                print("...")
                time.sleep(0.5)
                print("That's not an attack, silly")
                continue


        time.sleep(0.5)
        if userchoice == 's' or userchoice == 'S':
            logandprint("You attempt a STRONG attack...",fhand)
            time.sleep(0.4)
            logandprint("o==[]::::::::::::::::::::::>",fhand)
            time.sleep(1)
            rollresult = accroll(3)
            if rollresult == 1:
                logandprint("Your attack was a HIT! You dealt 50 damage!",fhand)
                enemyhp = enemyhp - 50
                par.append('sh')
                if enemyhp < 0:
                    enemyhp = 0
            else:
                logandprint("Your attack was a MISS! You dealt NO damage!",fhand)
                par.append('sm')


        elif userchoice == 'c' or userchoice == 'C':
            logandprint("You attempt a CAREFUL attack...",fhand)
            time.sleep(0.4)
            logandprint("o==[]::::::>",fhand)
            time.sleep(1)
            carefulaccroll = random.randint(1, 10)
            if carefulaccroll <= 8:
                logandprint("Your attack was a HIT! You dealt 20 damage!",fhand)
                enemyhp = enemyhp - 20
                par.append('ch')
                if enemyhp < 0:
                    enemyhp = 0
            else:
                logandprint("Your attack was a MISS! You dealt NO damage!",fhand)
                par.append('cm')


        elif userchoice == 'r' or userchoice == 'R':
            logandprint("You attempt a RECKLESS attack...",fhand)
            time.sleep(0.4)
            logandprint("o==[]::::::::::::::::::::::::::::::::::::::::>",fhand)
            time.sleep(1)
            recklessaccroll = random.randint(1, 10)
            if recklessaccroll == 1:
                logandprint("Your attack was reckless, but it HIT! You dealt 90 damage!! WOW!",fhand)
                enemyhp = enemyhp - 90
                par.append('rh')
                if enemyhp < 0:
                    enemyhp = 0
            else:
                logandprint("Your attack was way too reckless! You MISSED and hurt yourself! OH NO!",fhand)
                logandprint("You lost 20 HP",fhand)
                playerhp = playerhp - 20
                par.append('rm')
                if playerhp < 0:
                    playerhp = 0


        time.sleep(1)
        print("The enemy has",enemyhp,"HP left")
        time.sleep(1)

# ENEMY TURN

        if enemyhp > 0 and playerhp > 0:
            logandprint("Now it's the enemy's turn, look out!",fhand)
            time.sleep(1)
            enemychoice = random.randint(1, 10)
            if enemychoice == 1:
                logandprint("The enemy used a RECKLESS attack",fhand)
                time.sleep(0.4)
                logandprint("o==[]::::::::::::::::::::::::::::::::::::::::>",fhand)
                time.sleep(1)
                recklessaccroll = random.randint(1, 10)
                if recklessaccroll == 1:
                    logandprint("The enemy hits you HARD! OUCH!! You lose 90 HP!",fhand)
                    playerhp = playerhp - 90
                    if playerhp < 0:
                        playerhp = 0
                else:
                    logandprint("The enemy's attack was way too reckless! It missed and the enemy hurt itself! HAHA SUCKER!",fhand)
                    logandprint("The enemy lost 20 HP",fhand)
                    enemyhp = enemyhp - 20
                    if enemyhp < 0:
                        enemyhp = 0


            elif enemychoice >= 2 and enemychoice <= 4:

                logandprint("The enemy used a STRONG attack",fhand)
                time.sleep(0.4)
                logandprint("o==[]::::::::::::::::::::::>",fhand)
                time.sleep(1)
                strongaccroll = random.randint(1, 10)
                if strongaccroll <= 3:
                    logandprint("The attack was a HIT! You take 50 damage! OUCH!",fhand)
                    playerhp = playerhp - 50
                    if playerhp < 0:
                        playerhp = 0
                    time.sleep(1)
                else:
                    logandprint("The attack was a MISS! You take 0 damage! Phew...",fhand)
                    time.sleep(1)
            else:
                logandprint("The enemy used a CAREFUL attack",fhand)
                time.sleep(0.4)
                logandprint("o==[]::::::>",fhand)
                time.sleep(1)
                carefulaccroll = random.randint(1, 10)
                if carefulaccroll <= 8:
                    logandprint("The attack was a HIT! You take 20 damage!",fhand)
                    playerhp = playerhp - 20
                    if playerhp < 0:
                        playerhp = 0
                    time.sleep(1)
                else:
                    logandprint("The attack was a MISS! Woo, nice!",fhand)
                    time.sleep(1)
            print("You have",playerhp,"HP left!")
            time.sleep(1)
        else:
            time.sleep(1)
            break

    if enemyhp <= 0:
        tprint("AMAZING")
        time.sleep(1)
        tprint("YOU      WON!")
        playerscore = playerscore + 1
        logandprint("After that smashing victory...",fhand)
    else:
        tprint("  :  (  ")
        tprint("YOU     LOST")
        enemyscore = enemyscore + 1
        logandprint("After that crushing defeat...",fhand)


    logandprint("The current score is:",fhand)
    print("Enemy   ",enemyscore," - ",playerscore,"     You")

    while True:
        answer = str(input("Do you want to play again? (y/n): "))
        if answer in ('y', 'n'):
            break
        print ("Invalid input mate")
    if answer == 'y':
        continue
    else:

        # cacount = 0
        # cahit = 0
        # camiss = 0
        # sacount = 0
        # sahit = 0
        # samiss = 0
        # racount = 0
        # rmiss = 0
        # rhit = 0

        for i in par:
            if i == 'ch':
                cacount = cacount + 1
                cahit = cahit + 1
            if i == 'cm':
                cacount = cacount + 1
                camiss = camiss + 1
            if i == 'sh':
                sacount = sacount + 1
                sahit = sahit + 1
            if i == 'sm':
                sacount = sacount + 1
                samiss = samiss + 1
            if i == 'rh':
                racount = racount + 1
                rahit = rahit + 1
            if i == 'rm':
                racount = racount + 1
                ramiss = ramiss + 1

        time.sleep(0.5)
        print("Before you go, let's look at your stats!")
        time.sleep(0.5)
        print("You attempted %d careful attacks, of which %d were hits and %d were misses!" % (cacount, cahit, camiss))
        time.sleep(0.5)
        print("You attempted %d strong attacks, of which %d were hits and %d were misses!" % (sacount, sahit, samiss))
        time.sleep(0.5)
        print("You attempted %d reckless attacks, of which %d were hits and %d were misses!" % (racount, rahit, ramiss))
        time.sleep(0.5)
        print("Thank you for playing! Bye bye")
        break

fhand.close()






#for i in range(10):
#    x = random.random()
#    choice = random.choice(c)
