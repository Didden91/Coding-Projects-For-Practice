import sqlite3

def convtostr(org_list, seperator=' '):
    return seperator.join(org_list)

conn = sqlite3.connect('pokedex.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Pokedex;

CREATE TABLE Pokedex (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    LocalDex INTEGER,
    NationalDex  INTEGER,
    Sprite  TEXT,
    Pokémon  TEXT,
    Type  TEXT,
    Type2  TEXT
);
''')

inp = input("Please enter a filename: ")
if len(inp) < 1:
    inp = 'Pokedex.txt'

try:
    fhand = open(inp)
except:
    print("invalid filename")
    quit()
idcounter = 0

for line in fhand:
    line = line.strip()
    line = line.replace('#', '')
    line = line.replace('â™€', '\u2640') #FEMALE
    line = line.replace('â™‚', '\u2642') #MALE
    print(line)
    parts = line.split()

    #NORMAL SCENARIO
    if parts[1].isdigit() == True:
        print('TRUE')
        idcounter += 1
        cur.execute('''INSERT INTO Pokedex
                (LocalDex, NationalDex, Sprite, Pokémon, Type) VALUES ( ?, ?, ?, ?, ? )''',
                ( parts[0], parts[1], parts[2], parts[3], parts[4] ) )


        if len(parts) == 6:
            cur.execute('''UPDATE Pokedex SET Type2 = ? WHERE id = ? ''',
                        ( parts[5], idcounter ) )

        conn.commit()

    #WEIRD SCENARIO

    else:
        print('FALSE')
        idcounter += 1
        cur.execute('''INSERT INTO Pokedex
                (NationalDex, Sprite, Pokémon, Type) VALUES ( ?, ?, ?, ? )''',
                (parts[0], parts[1], parts[2], parts[3]  ) )
        if len(parts) == 5:
            cur.execute('''UPDATE Pokedex SET Type2 = ? WHERE id = ? ''',
                        ( parts[4], idcounter ) )
        conn.commit()
