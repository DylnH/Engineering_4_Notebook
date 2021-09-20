# Automatic Dice Roller

# Written by [Dylan J. Hensley]

print ("🎲Automatic Dice Roller🎲:") # Title

import random
roll_again = ""
while roll_again == "":
    roll_dice = input("🎲Roll The Dice ⬇") # Telling you to Roll the Dice

    if roll_dice == "Roll": # What you write to roll the Dice
        posiblle_results = [6, 5, 4, 3, 2, 1] # possible outcomes
        result = random.choice(posiblle_results) # Picks out a random number
        print("You rolled a... " + str(result)) # Tells you the random number
    roll_again = input("X to exit / Enter to Roll again🎲")