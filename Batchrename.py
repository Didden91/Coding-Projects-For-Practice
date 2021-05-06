import os
path = '/Users/Ivo/Desktop/pygame/Sprites/first99'
files = os.listdir(path)

os.chdir(path)


for file in files:
    os.rename(file, file.replace('0', ''))
