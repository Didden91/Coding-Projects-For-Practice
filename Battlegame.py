from art import *
import random
import time

strongaccroll = 0
carefulaccroll = 0
recklessaccroll = 0
enemyroll = 0
enemychoice = 0
playerscore = 0
enemyscore = 0


#strongattackdmg = 50
#strongattackacc = 3

#carefulattackdmg = 20
#carefulattackacc = 8

#recklessattackdmg = 90
#recklessattackselfdmg = 30
#recklessattackacc = 1

while True:

    enemyhp = 100
    playerhp = 100
    tprint("OH     NOOOOOOOOOOOOOOO")
    time.sleep(1)
    tprint("AN      ENEMY      APPEARED")
    time.sleep(1)

    while enemyhp > 0 and playerhp > 0:

        while True:
            userchoice = input("Choose an attack:\nSTRONG (S) or CAREFUL (C) or RECKLESS (R): ")
            if userchoice in ('S', 's', 'C', 'c', 'R', 'r'):
                break

            else:
                time.sleep(0.5)
                print("...")
                time.sleep(0.5)
                print("That's not an attack mate")
                continue


        time.sleep(0.5)
        if userchoice == 's' or userchoice == 'S':
            print("You attempt a STRONG attack...")
            time.sleep(1)
            strongaccroll = random.randint(1, 10)
            if strongaccroll <= 3:
                print("Your attack was a HIT! You dealt 50 damage!")
                enemyhp = enemyhp - 50
                if enemyhp < 0:
                    enemyhp = 0
            else:
                print("Your attack was a MISS! You dealt NO damage!")


        elif userchoice == 'c' or userchoice == 'C':
            print("You attempt a CAREFUL attack...")
            time.sleep(1)
            carefulaccroll = random.randint(1, 10)
            if carefulaccroll <= 8:
                print("Your attack was a HIT! You dealt 20 damage!")
                enemyhp = enemyhp - 20
                if enemyhp < 0:
                    enemyhp = 0
            else:
                print("Your attack was a MISS! You dealt NO damage!")


        elif userchoice == 'r' or userchoice == 'R':
            print("You attempt a RECKLESS attack...")
            time.sleep(1)
            recklessaccroll = random.randint(1, 10)
            if recklessaccroll == 1:
                print("Your attack was reckless, but it HIT! You dealt 90 damage!! WOW!")
                enemyhp = enemyhp - 90
                if enemyhp < 0:
                    enemyhp = 0
            else:
                print("Your attack was way too reckless! You MISSED and hurt yourself! OH NO!")
                print("You lost 20 HP")
                playerhp = playerhp - 20
                if playerhp < 0:
                    playerhp = 0


        time.sleep(1)
        print("The enemy has",enemyhp,"HP left")
        time.sleep(1)

# ENEMY TURN

        if enemyhp > 0 and playerhp > 0:
            print("Now it's the enemy's turn, look out!")
            time.sleep(1)
            enemychoice = random.randint(1, 10)
            if enemychoice == 1:
                print("The enemy used a RECKLESS attack")
                time.sleep(1)
                recklessaccroll = random.randint(1, 10)
                if recklessaccroll == 1:
                    print("The enemy hits you HARD! OUCH!! You lose 90 HP!")
                    playerhp = playerhp - 90
                    if playerhp < 0:
                        playerhp = 0
                else:
                    print("The enemy's attack was way too reckless! It missed and the enemy hurt itself! HAHA SUCKER!")
                    print("The enemy lost 20 HP")
                    enemyhp = enemyhp - 20
                    if enemyhp < 0:
                        enemyhp = 0


            elif enemychoice >= 2 and enemychoice <= 4:

                print("The enemy used a STRONG attack")
                time.sleep(1)
                strongaccroll = random.randint(1, 10)
                if strongaccroll <= 3:
                    print("The attack was a HIT! You take 50 damage! OUCH!")
                    playerhp = playerhp - 50
                    if playerhp < 0:
                        playerhp = 0
                    time.sleep(1)
                else:
                    print("The attack was a MISS! You take 0 damage! Phew...")
                    time.sleep(1)
            else:
                print("The enemy used a CAREFUL attack")
                time.sleep(1)
                carefulaccroll = random.randint(1, 10)
                if carefulaccroll <= 8:
                    print("The attack was a HIT! You take 20 damage!")
                    playerhp = playerhp - 20
                    if playerhp < 0:
                        playerhp = 0
                    time.sleep(1)
                else:
                    print("The attack was a MISS! Woo, nice!")
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
    else:
        tprint("  :  (  ")
        tprint("YOU     LOST")
        enemyscore = enemyscore + 1


    print("The current score is:")
    print("Enemy   ",enemyscore," - ",playerscore,"     You")

    while True:
        answer = str(input("Do you want to play again? (y/n): "))
        if answer in ('y', 'n'):
            break
        print ("Invalid input mate")
    if answer == 'y':
        continue
    else:
        print("Thank you for playing! Bye bye")
        break






#for i in range(10):
#    x = random.random()
#    choice = random.choice(c)
