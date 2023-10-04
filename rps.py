import sys
import random

print("")
playerdecision = input("Enter ... \n1 for Rock,\n2 for Paper, or\n3 for Scissors:\n\n")
playa = int(playerdecision)

if playa < 1 or playa > 3:
    sys.exit("Please enter the right character.")

computerdecision = random.choice("123")

computer =int(computerdecision)

print("")
print("You chose "+ playerdecision + ".")
print("Python chose "+ computerdecision + ".")
print("")

if playa == 1 and computer == 3:
    print("🥳🎆You won!")
elif playa == 2 and computer == 1:
    print("🥳🎆You won!")
elif playa == 3 and computer == 2:
    print("🥳🎆You won!")
elif playa == computer:
    print("Great minds🤯...")
else:
    print("Python wins!🐍🐉")