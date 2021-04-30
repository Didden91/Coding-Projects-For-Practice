import sqlite3
import random

conn = sqlite3.connect('pokemoves.sqlite')
cur = conn.cursor()

inp = input("Guess a move:")

cur.execute('SELECT Number FROM Pokemoves WHERE Name = ? ', (inp,))
line = cur.fetchone()
if line == None:
    print("Move not found")
    quit()
else:
    print("You guessed move number %d: %s" % (line[0], inp))
outcome = random.randint(1, 826)


cur.execute('SELECT Name FROM Pokemoves WHERE Number = ? ', (outcome,))
row = cur.fetchone()
for i in row:
    print("The outcome is move number %d: %s" % (outcome, i))

if outcome == line[0]:
    print("YAAAAAAAAAAY YOU WON!!")
else:
    print("Too bad, you lost")
