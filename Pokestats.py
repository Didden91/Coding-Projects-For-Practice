import sqlite3

def convtostr(org_list, seperator=' '):
    return seperator.join(org_list)

conn = sqlite3.connect('pokeDB.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Pokestats;

CREATE TABLE Pokestats (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    NationalDex  INTEGER,
    Sprite  TEXT,
    Pokémon  TEXT,
    HP  INTEGER,
    Attack  INTEGER,
    Defense  INTEGER,
    SpAttack  INTEGER,
    SpDefense  INTEGER,
    Speed  INTEGER,
    Total  INTEGER,
    Average  REAL,
    SpecialForm  TEXT

);
''')

inp = input("Please enter a filename: ")
if len(inp) < 1:
    inp = 'PokestatsNEW.txt'

try:
    fhand = open(inp)
except:
    print("invalid filename")
    quit()


for line in fhand:
    line = line.strip()
    line = line.replace('â™€', '\u2640') #FEMALE
    line = line.replace('â™‚', '\u2642') #MALE
    print(line)
    parts = line.split()

    #NORMAL SCENARIO
    if len(parts) == 11:
        print('11 part line')

        cur.execute('''INSERT INTO Pokestats
                (NationalDex, Sprite, Pokémon, HP, Attack, Defense, SpAttack, SpDefense, Speed, Total, Average) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )''',
                ( parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8], parts[9], parts[10] ) )


        conn.commit()

    #WEIRD SCENARIO

    else:
        print('13 part line')

        specialtype = parts[11] + ' ' + parts[12]
        specialtype = specialtype.replace('(', '')
        specialtype = specialtype.replace(')', '')



        cur.execute('''INSERT INTO Pokestats
                (NationalDex, Sprite, Pokémon, HP, Attack, Defense, SpAttack, SpDefense, Speed, Total, Average, SpecialForm) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )''',
                ( parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8], parts[9], parts[10], specialtype ) )

        conn.commit()
