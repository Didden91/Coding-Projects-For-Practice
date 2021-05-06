import os

inp = input("Please enter a path: ")
try:
    files = os.listdir(inp)
except:
    print('invalid path')
    quit()

os.chdir(inp)


for file in files:
    os.rename(file, file.replace('0', ''))
