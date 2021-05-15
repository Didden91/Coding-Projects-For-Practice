import sqlite3
import random

conn = sqlite3.connect('pokeDB.sqlite')
cur = conn.cursor()

pnum = random.randint(1, 876)
m1 = random.randint(1, 826)
m2 = random.randint(1, 826)
m3 = random.randint(1, 826)
m4 = random.randint(1, 826)

poke = cur.execute('SELECT Pokémon, Type, Type2, LocalDex FROM Pokedex WHERE id = ?' , (pnum, ))
for i in poke:
    print("A wild %s appeared!" % i[0])
    if i[3] == None:
        print("It's Alolan Form! WoooooW")
    if i[2] == None:
        print("It's %s type" % i[1])
    else:
        print("It's %s and %s type" % (i[1], i[2]))


moveone = cur.execute('SELECT Name FROM Pokemoves WHERE id = ?' , (m1, ))
for i in moveone: print(i[0])
movetwo = cur.execute('SELECT Name FROM Pokemoves WHERE id = ?' , (m2, ))
for i in movetwo: print(i[0])
movethree = cur.execute('SELECT Name FROM Pokemoves WHERE id = ?' , (m3, ))
for i in movethree: print(i[0])
movefour = cur.execute('SELECT Name FROM Pokemoves WHERE id = ?' , (m4, ))
for i in movefour: print(i[0])
