import sys
import random

print("")
playerdecision = input("Enter ... \nA for Rock,\nB for Paper, or\nC for Scissors:\n\n")

if playerdecision != 'A' or playerdecision != 'B' or playerdecision != 'C':
    sys.exit("Please enter the right character.")

computerdecision = random.choice("ABC")

print("")
print("You chose "+ playerdecision + ".")
print("Python chose "+ computerdecision + ".")
print("")
