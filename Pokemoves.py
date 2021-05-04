import sqlite3

def convtostr(org_list, seperator=' '):
    return seperator.join(org_list)

conn = sqlite3.connect('pokemoves.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Pokemoves;

CREATE TABLE Pokemoves (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    Number INTEGER,
    Name  TEXT,
    Type  TEXT,
    Category  TEXT,
    Contest  TEXT,
    PP  INTEGER,
    Power  INTEGER,
    Accuracy  INTEGER,
    Generation  TEXT
);
''')

inp = input("Please enter a filename: ")
if len(inp) < 1:
    inp = 'Pokemoves.txt'

try:
    fhand = open(inp)
except:
    print("invalid filename")
    quit()

biglist = list()
movenumber = list()
movename = list()
movetype = list()
movecat = list()
movecon = list()
movepp = list()
movepower = list()
moveacc = list()
movegen = list()

typedic = dict()
catdic = dict()
accdic = dict()


for line in fhand:
    line = line.strip()
    line = line.replace('%', '')
    line = line.replace('*', '')
    line = line.replace('â€”', '0')
    line = line.replace('???', 'Unknown')
    print(line)
    parts = line.split()
    movenumber.append(parts[0])
    if len(parts) == 9:
        movename.append([parts[1]])
        movetype.append(parts[2])
        movecat.append(parts[3])
        movecon.append(parts[4])
        movepp.append(parts[5])
        movepower.append(parts[6])
        moveacc.append(parts[7])
        movegen.append(parts[8])

        cur.execute('''INSERT INTO Pokemoves
            (Number, Name, Type, Category, Contest, PP, Power, Accuracy, Generation) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ? )''',
            ( parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8] ) )
        conn.commit()
    else:
        x = len(parts) - 7
        movename.append(parts[1:x])
        movetype.append(parts[x])
        movecat.append(parts[x+1])
        movecon.append(parts[x+2])
        movepp.append(parts[x+3])
        movepower.append(parts[x+4])
        moveacc.append(parts[x+5])
        movegen.append(parts[x+6])
        strlist = convtostr(parts[1:x])

        cur.execute('''INSERT INTO Pokemoves
            (Number, Name, Type, Category, Contest, PP, Power, Accuracy, Generation) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ? )''',
            ( parts[0], strlist, parts[x], parts[x+1], parts[x+2], parts[x+3], parts[x+4], parts[x+5], parts[x+6] ) )
        conn.commit()
    biglist.append(parts)

# print(biglist)
# print(movenumber)
counter = 0
for item in movename:
    if len(item) > 2:
        print(item)
        counter += 1
print("Total Count:",counter)

for type in movetype:
    typedic[type] = typedic.get(type, 0) + 1
print(typedic)

for cat in movecat:
    catdic[cat] = catdic.get(cat, 0) + 1
print(catdic)

for acc in moveacc:
    accdic[acc] = accdic.get(acc, 0) + 1
print("ACCCCCCCCCCCC")
print(accdic)

#Make dict into a list that can be sorted.
#In this case to sort move types, which are in typedic
print("TEST BEGINT HIER:")

lst = list()
for type, count in typedic.items():
    newtuple = (count, type)
    lst.append(newtuple)
lst = sorted(lst, reverse=True)

for value, key in lst:
    if len(key) > 6:
        print(key,'\t', value)
    else:
        print(key,'\t\t', value)
