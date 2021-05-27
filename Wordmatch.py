import re

fhand = open('wlist_match1.txt')

for line in fhand:
    if re.match(r"(.*s.*e.*v.*e.*n.*)", line):
        print(line)

# print(len(words))
# for word in words:
#     if re.match(r"(s.*e.*v.*e.*n.*)", word):
#         print(word)
