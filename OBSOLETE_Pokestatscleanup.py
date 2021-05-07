import re

fhand = open('Pokestats.txt', 'r')
fhand2 = open('PokestatsNEW.txt', 'w')

for line in fhand:

    stuff = re.findall('[(].*[)]', line)

    if len(stuff) > 0:
        print('KIJK HIER, ORIGINAL LINE:',line)
        updline = line.replace(stuff[0], '')
        print('NEW UPDATE LINE:', updline)
        updline = updline.replace('\n', '') + '\t' + stuff[0] + '\n'
        print('UPDATE 222222:', updline)

        line = updline
        print('FINAL CHECK:',line)
        fhand2.write(line)
    else:
        fhand2.write(line)


fhand.close()
fhand2.close()
