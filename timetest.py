import time

p = time.ctime()

print(p)

# for letter in p:
#     if letter == ':':
#         letter = ' '
#     else:
#         continue
p = p.replace(":","")
print(p)
# print(time.ctime())
#
# print(time.time())
# time.sleep(1)
# print(time.time())
# time.sleep(1)
# print(time.time())
# time.sleep(1)
# print(time.time())
#
# print(time.ctime())
