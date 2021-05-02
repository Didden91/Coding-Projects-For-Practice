def enemydamagecalc(movecategory, movepower, movetype, userattack, userspattack, opponentdefense, opponentspdefense, enemytype1, enemytype2 = 'None'):
    damagerange = random.uniform(0.85, 1.00)
    crit = random.randint(1, 16)
    if crit == 16:
        crit = 1.5
    else:
        crit = 1.0
    effectiveness = howeffective(movetype, enemytype1, enemytype2 = 'None')


    if movecategory == 'Physical':
        print('used a PHYSICAL move')
        #The 50 is the level, for now all pokes are level 50
        #damage pre modifiers:
        damage = ((2 * 50 / 5 + 2) * movepower * userattack / opponentdefense / 50 + 2)
        #now apply modifiers
        damage = damage * crit * damagerange * effectiveness

    elif movecategory == 'Special':
        print('used a SPECIAL move')
        damage = ((2 * 50 / 5 + 2) * movepower * userspattack / opponentspdefense / 50 + 2)
        damage = damage * crit * damagerange * effectiveness
    else:
        print('used a STATUS move')
        damage = 0



    return damage, crit

#TEST CASE = playermove1

# movecategory = playermove1[5]
# movepower = playermove1[3]
# movetype = playermove[1]
# userattack = playerAttack
# userspattack = playerSpattack
# opponentdefense = enemyDefense
# opponentspdefens = enemySpdefense
# enemytype1 = enemypoke[1]
# enemytype2 = enemypoke[2]

# this length == 4 means there are two types
if len(enemypoke) == 4:
    damage, crit = enemydamagecalc(move[5],move[3],move[1], enemyAttack, enemySpattack, playerDefense, playerSpdefense, playerpoke[1], playerpoke[2] )
# otherwise one type
else:
    damage, crit = enemydamagecalc(move[5],move[3],move[1], enemyAttack, enemySpattack, playerDefense, playerSpdefense, playerpoke[1])
