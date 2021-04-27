fhand = open('ingredienten.txt')
fhand2 = open('testoutput.txt', 'w')


for line in fhand:
    if len(line) > 1:
        dashpos = line.find('-')
        line = line[:dashpos]
        line = line.rstrip()
        line = line + ", "
    else:
        line = line.rstrip()
    fhand2.write(line)

fhand.close()
fhand2.close()
