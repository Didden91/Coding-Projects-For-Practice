# 1 = Addition
# 2 = Subtraction
# 3 = Multiplication
# 4 = Division

import time
from art import *

import os                                 #import os and time
def loading():
    loops = 0                                #make a function called loading
    spaces = 0                                      #making a variable to store the amount of spaces between the start and the "."
    while loops < 100:                                     #infinite loop
        print("\b"*spaces+"HUUUUUUuuuuuuuuuuuuuuuuuUUUUUUUUUUUuuuuuuuuuuuuuuuuU", end="uuuUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUuu", flush=True) #we are deleting however many spaces and making them " " then printing "."
        spaces = spaces+1                           #adding a space after each print
        time.sleep(0.02)                             #waiting 0.2 secconds before proceeding
        if (spaces>50):                              #if there are more than 5 spaces after adding one so meaning 5 spaces (if that makes sense)
            print("\b \b"*spaces, end="")           #delete the line
            spaces = 0                              #set the spaces back to 0
        loops += 1

Finaloperatorone = 0
Finaloperatortwo = 0

varone = 0
vartwo = 0
varthree = 0

varone = input("Please enter your first number: ")

try:
    varone = float(varone)
except:
    print("Error, not a valid number. Exiting...")
    quit()

vartwo = input("Please enter your second number: ")

try:
    vartwo = float(vartwo)
except:
    print("Error, not a valid number. Exiting...")
    quit()

varthree = input("Please enter your third number: ")

try:
    varthree = float(varthree)
except:
    print("Error, not a valid number. Exiting...")
    quit()

print("You entered:", varone, vartwo, varthree)

print("Now let's decide what to do with these numbers...")
operatorstringone = 'X'
operatorstringtwo = 'X'

operatorstringone = input("What should happen between the first and second number? \nAddition (A), Subtraction (S), Multiplication (M),  or Division (D): ")

try:
    operatorstringone = str(operatorstringone)
except:
    print("Error, not a valid input. Exiting...")
    quit()

if operatorstringone == 'A' or operatorstringone == 'a':
    finaloperatorone = 1
    tprint("+")
    print ("You have chosen Addition")
    tprint("                    +")
elif operatorstringone == 'S' or operatorstringone == 's':
    finaloperatorone = 2
    tprint("-")
    print ("You have chosen Subtraction")
    tprint("                    -")
elif operatorstringone == 'M' or operatorstringone == 'm':
    finaloperatorone = 3
    tprint("X")
    print ("You have chosen Multiplication")
    tprint("                    X")
elif operatorstringone == 'D' or operatorstringone == 'd':
    finaloperatorone = 4
    tprint("/")
    print ("You have chosen Division")
    tprint("                    /")
else:
    print("Invalid input, exiting...")
    quit()

time.sleep (0.5)

operatorstringtwo = input("What should happen between the second and third number? \nAddition (A), Subtraction (S), Multiplication (M),  or Division (D): ")

try:
    operatorstringtwo = str(operatorstringtwo)
except:
    print("Error, not a valid input. Exiting...")
    quit()

if operatorstringtwo == 'A' or operatorstringtwo == 'a':
    finaloperatortwo = 1
    tprint("+")
    print ("You have chosen Addition")
    tprint("                    +")
elif operatorstringtwo == 'S' or operatorstringtwo == 's':
    finaloperatortwo = 2
    tprint("-")
    print ("You have chosen Subtraction")
    tprint("                    -")
elif operatorstringtwo == 'M' or operatorstringtwo == 'm':
    finaloperatortwo = 3
    tprint("X")
    print ("You have chosen Multiplication")
    tprint("                    X")
elif operatorstringtwo == 'D' or operatorstringtwo == 'd':
    finaloperatortwo = 4
    tprint("/")
    print ("You have chosen Division")
    tprint("                    /")
else:
    print("Invalid input, exiting...")
    quit()

time.sleep (1.5)
print("Now to crunch those numbers...")
time.sleep (2.5)
print("Working really hard.......")
time.sleep (3)
print("Hnnnnggggggggg")
time.sleep (4)
print("Almost there.......")
time.sleep (4)

#x = 0

#while x < 100:
    #print("A \r"),
    #time.sleep (0.1)
loading()
#    x += 1

print("\n")

# FINAL CALCULATION

if finaloperatorone == 1 and finaloperatortwo == 1:
    print ("The endresult is: ", varone + vartwo + varthree)
elif finaloperatorone == 1 and finaloperatortwo == 2:
    print ("The endresult is: ", varone + vartwo - varthree)
elif finaloperatorone == 1 and finaloperatortwo == 3:
    print ("The endresult is: ", varone + vartwo * varthree)
elif finaloperatorone == 1 and finaloperatortwo == 4:
    print ("The endresult is: ", varone + vartwo / varthree)
elif finaloperatorone == 2 and finaloperatortwo == 1:
    print ("The endresult is: ", varone - vartwo + varthree)
elif finaloperatorone == 2 and finaloperatortwo == 2:
    print ("The endresult is: ", varone - vartwo - varthree)
elif finaloperatorone == 2 and finaloperatortwo == 3:
    print ("The endresult is: ", varone - vartwo * varthree)
elif finaloperatorone == 2 and finaloperatortwo == 4:
    print ("The endresult is: ", varone - vartwo / varthree)
elif finaloperatorone == 3 and finaloperatortwo == 1:
    print ("The endresult is: ", varone * vartwo + varthree)
elif finaloperatorone == 3 and finaloperatortwo == 2:
    print ("The endresult is: ", varone * vartwo - varthree)
elif finaloperatorone == 3 and finaloperatortwo == 3:
    print ("The endresult is: ", varone * vartwo * varthree)
elif finaloperatorone == 3 and finaloperatortwo == 4:
    print ("The endresult is: ", varone * vartwo / varthree)
elif finaloperatorone == 4 and finaloperatortwo == 1:
    print ("The endresult is: ", varone / vartwo + varthree)
elif finaloperatorone == 4 and finaloperatortwo == 2:
    print ("The endresult is: ", varone / vartwo - varthree)
elif finaloperatorone == 4 and finaloperatortwo == 3:
    print ("The endresult is: ", varone / vartwo * varthree)
elif finaloperatorone == 4 and finaloperatortwo == 4:
    print ("The endresult is: ", varone / vartwo / varthree)
else:
    print("Something must have gone wrong, exiting...")
    quit()

time.sleep (2)
print("Whew, that was rough...")
