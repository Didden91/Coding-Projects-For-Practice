
def howeffective(movetype, enemytype1, enemytype2 = 'None'):

    effectiveness = 0
    # NORMAL
    if movetype == 'Normal':
        # is it effective AT ALL?
        if enemytype1 == 'Ghost' or enemytype2 == 'Ghost':
            effectiveness = 0
            print('doesnt affect')
        # is it SUPER effective?

        # is it NOT VERY effective?
        elif enemytype1 in ['Rock', 'Steel'] or enemytype2 in ['Rock', 'Steel']:
            effectiveness = 0.5
            print('not very')
        # none of the above means normal damage
        else:
            effectiveness = 1
            print('normal damage')

    # FIGHTING

    if movetype == 'Fighting':
        if enemytype1 == 'Ghost' or enemytype2 == 'Ghost':
            effectiveness = 0
            print('doesnt affect')
        elif enemytype1 in ['Normal', 'Rock', 'Steel', 'Ice', 'Dark'] or enemytype2 in ['Normal', 'Rock', 'Steel', 'Ice', 'Dark']:
            effectiveness = 2
            print('VERY effective')
        elif enemytype1 in ['Flying', 'Poison', 'Bug', 'Psychic', 'Fairy'] or enemytype2 in ['Flying', 'Poison', 'Bug', 'Psychic', 'Fairy']:
            effectiveness = 0.5
            print('not very')
        else:
            effectiveness = 1
            print('normal damage')

    # FLYING

    if movetype == 'Flying':
        if enemytype1 in ['Fighting', 'Bug', 'Grass'] or enemytype2 in ['Fighting', 'Bug', 'Grass']:
            effectiveness = 2
            print('VERY effective')
        elif enemytype1 in ['Rock', 'Steel', 'Electric'] or enemytype2 in ['Rock', 'Steel', 'Electric']:
            effectiveness = 0.5
            print('not very')
        else:
            effectiveness = 1
            print('normal damage')

    # POISON

    if movetype == 'Poison':
        if enemytype1 == 'Steel' or enemytype2 == 'Steel':
            effectiveness = 0
            print('doesnt affect')
        elif enemytype1 in ['Grass', 'Fairy'] or enemytype2 in ['Grass', 'Fairy']:
            effectiveness = 2
            print('VERY effective')
        elif enemytype1 in ['Poison', 'Ground', 'Rock', 'Ghost'] or enemytype2 in ['Poison', 'Ground', 'Rock', 'Ghost']:
            effectiveness = 0.5
            print('not very')
        else:
            effectiveness = 1
            print('normal damage')

    # GROUND

    if movetype == 'Ground':
        if enemytype1 == 'Flying' or enemytype2 == 'Flying':
            effectiveness = 0
            print('doesnt affect')
        elif enemytype1 in ['Poison', 'Rock', 'Steel', 'Fire', 'Electric'] or enemytype2 in ['Poison', 'Rock', 'Steel', 'Fire', 'Electric']:
            effectiveness = 2
            print('VERY effective')
        elif enemytype1 in ['Bug', 'Grass'] or enemytype2 in ['Bug', 'Grass']:
            effectiveness = 0.5
            print('not very')
        else:
            effectiveness = 1
            print('normal damage')

    # ROCK

    if movetype == 'Rock':
        if enemytype1 in ['Flying', 'Bug', 'Fire', 'Ice'] or enemytype2 in ['Flying', 'Bug', 'Fire', 'Ice']:
            effectiveness = 2
            print('VERY effective')
        elif enemytype1 in ['Fighting', 'Ground', 'Steel'] or enemytype2 in ['Fighting', 'Ground', 'Steel']:
            effectiveness = 0.5
            print('not very')
        else:
            effectiveness = 1
            print('normal damage')

    # BUG
    if movetype == 'Bug':
        if enemytype1 in ['Grass', 'Psychic', 'Dark'] or enemytype2 in ['Grass', 'Psychic', 'Dark']:
            effectiveness = 2
            print('VERY effective')
        elif enemytype1 in ['Fighting', 'Flying', 'Poison', 'Ghost', 'Steel', 'Fire', 'Fairy'] or enemytype2 in ['Fighting', 'Flying', 'Poison', 'Ghost', 'Steel', 'Fire', 'Fairy']:
            effectiveness = 0.5
            print('not very')
        else:
            effectiveness = 1
            print('normal damage')

    # GHOST

    if movetype == 'Ghost':
        if enemytype1 == 'Normal' or enemytype2 == 'Normal':
            effectiveness = 0
            print('doesnt affect')
        elif enemytype1 in ['Ghost', 'Psychic'] or enemytype2 in ['Ghost', 'Psychic']:
            effectiveness = 2
            print('VERY effective')
        elif enemytype1 == 'Dark' or enemytype2 == 'Dark':
            effectiveness = 0.5
            print('not very')
        else:
            effectiveness = 1
            print('normal damage')

    # STEEL

    if movetype == 'Steel':
        if enemytype1 in ['Rock', 'Ice', 'Fairy'] or enemytype2 in ['Rock', 'Ice', 'Fairy']:
            effectiveness = 2
            print('VERY effective')
        elif enemytype1 in ['Steel', 'Fire', 'Water', 'Electric'] or enemytype2 in ['Steel', 'Fire', 'Water', 'Electric']:
            effectiveness = 0.5
            print('not very')
        else:
            effectiveness = 1
            print('normal damage')

    # FIRE

    if movetype == 'Fire':
        if enemytype1 in ['Bug', 'Steel', 'Grass', 'Ice'] or enemytype2 in ['Bug', 'Steel', 'Grass', 'Ice']:
            effectiveness = 2
            print('VERY effective')
        elif enemytype1 in ['Rock', 'Fire', 'Water', 'Dragon'] or enemytype2 in ['Rock', 'Fire', 'Water', 'Dragon']:
            effectiveness = 0.5
            print('not very')
        else:
            effectiveness = 1
            print('normal damage')

    # WATER

    if movetype == 'Water':
        if enemytype1 in ['Ground', 'Rock', 'Fire'] or enemytype2 in ['Ground', 'Rock', 'Fire']:
            effectiveness = 2
            print('VERY effective')
        elif enemytype1 in ['Water', 'Grass', 'Dragon'] or enemytype2 in ['Water', 'Grass', 'Dragon']:
            effectiveness = 0.5
            print('not very')
        else:
            effectiveness = 1
            print('normal damage')

    # GRASS
    if movetype == 'Grass':
        if enemytype1 in ['Ground', 'Rock', 'Water'] or enemytype2 in ['Ground', 'Rock', 'Water']:
            effectiveness = 2
            print('VERY effective')
        elif enemytype1 in ['Flying', 'Poison', 'Bug', 'Steel', 'Fire', 'Grass', 'Dragon'] or enemytype2 in ['Flying', 'Poison', 'Bug', 'Steel', 'Fire', 'Grass', 'Dragon']:
            effectiveness = 0.5
            print('not very')
        else:
            effectiveness = 1
            print('normal damage')

    # ELECTRIC

    if movetype == 'Electric':
        if enemytype1 == 'Ground' or enemytype2 == 'Ground':
            effectiveness = 0
            print('doesnt affect')
        elif enemytype1 in ['Flying', 'Water'] or enemytype2 in ['Flying', 'Water']:
            effectiveness = 2
            print('VERY effective')
        elif enemytype1 in ['Grass', 'Electric', 'Dragon'] or enemytype2 in ['Grass', 'Electric', 'Dragon']:
            effectiveness = 0.5
            print('not very')
        else:
            effectiveness = 1
            print('normal damage')

    # PSYCHIC

    if movetype == 'Psychic':
        if enemytype1 == 'Dark' or enemytype2 == 'Dark':
            effectiveness = 0
            print('doesnt affect')
        elif enemytype1 in ['Fighting', 'Poison'] or enemytype2 in ['Fighting', 'Poison']:
            effectiveness = 2
            print('VERY effective')
        elif enemytype1 in ['Steel', 'Psychic'] or enemytype2 in ['Steel', 'Psychic']:
            effectiveness = 0.5
            print('not very')
        else:
            effectiveness = 1
            print('normal damage')

    # ICE

    if movetype == 'Ice':
        if enemytype1 in ['Flying', 'Ground', 'Grass', 'Dragon'] or enemytype2 in ['Flying', 'Ground', 'Grass', 'Dragon']:
            effectiveness = 2
            print('VERY effective')
        elif enemytype1 in ['Steel', 'Fire', 'Water', 'Ice'] or enemytype2 in ['Steel', 'Fire', 'Water', 'Ice']:
            effectiveness = 0.5
            print('not very')
        else:
            effectiveness = 1
            print('normal damage')

    # DRAGON

    if movetype == 'Dragon':
        if enemytype1 == 'Fairy' or enemytype2 == 'Fairy':
            effectiveness = 0
            print('doesnt affect')
        elif enemytype1 == 'Dragon' or enemytype2 == 'Dragon':
            effectiveness = 2
            print('VERY effective')
        elif enemytype1 == 'Steel' or enemytype2 == 'Steel':
            effectiveness = 0.5
            print('not very')
        else:
            effectiveness = 1
            print('normal damage')

    # DARK
    if movetype == 'Dark':
        if enemytype1 in ['Ghost', 'Psychic'] or enemytype2 in ['Ghost', 'Psychic']:
            effectiveness = 2
            print('VERY effective')
        elif enemytype1 in ['Fighting', 'Dark', 'Fairy'] or enemytype2 in ['Fighting', 'Dark', 'Fairy']:
            effectiveness = 0.5
            print('not very')
        else:
            effectiveness = 1
            print('normal damage')

    # FAIRY

    if movetype == 'Fairy':
        if enemytype1 in ['Fighting', 'Dragon', 'Dark'] or enemytype2 in ['Fighting', 'Dragon', 'Dark']:
            effectiveness = 2
            print('VERY effective')
        elif enemytype1 in ['Poison', 'Steel', 'Fire'] or enemytype2 in ['Poison', 'Steel', 'Fire']:
            effectiveness = 0.5
            print('not very')
        else:
            effectiveness = 1
            print('normal damage')

    return effectiveness


effectmult = howeffective('Fire', 'Steel', 'Grass')
print(effectmult)
