fhand = open('PokestatsNEW.txt')
counter = 0
for line in fhand:
    parts = line.split()

    if len(parts) == 13:
        counter += 1
        specialtype = parts[11] + ' ' + parts[12]
        specialtype = specialtype.replace('(', '')
        specialtype = specialtype.replace(')', '')
        print('specialtype',specialtype)


print('COUNT:', counter)


# 0 lines are 12 parts long
# 791 lines are 11 long
# 145 are 13 long
#
# 0 are 10 long

# 0 are 14 long
# 0 are  15 long

# = 936 IS ALL
