# Engineering_4_Notebook
## Dylan Hensley's Engineering 4 Notebook
 
<details><summary>Dice Roller</summary>
 
## Dice Roller

### Assignment Description

In this assignment, we created a number generator that would pick a random number from 1-6. For this assignment, we needed to use "import random" which is a function that is used to select random results out of possible outcomes. This assignment, if done correctly, should have relatively clean code and should be really fun to use.

### Evidence 
 
<details><summary>Code</summary>
 
 
 ``` python
 
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

```
 
</details>
 
<img src="https://github.com/DylnH/Engineering_4_Notebook/blob/main/Screenshot%202021-10-05%209.55.41%20PM.png?raw=true" alt="Screenshot 2021-10-05 9.55.41 PM.png"/>
 
 Onces you start, Type in "Roll" and Taa Daa, you should get a number between 1-6. Then if you want to roll again, press "enter", if not, "X"

### Wiring

N/A
 
### Reflection

The assignment wasn't hard at all, however, it was SO hard to follow Mr Miller's demands. Eventhough my code was working, he made me redo it over and over and over again, because I didn't "follow intructions". What kind of monster does that??? Anyway, if you want to do this assignment, look at the for the .py file in my readme.Personally, feel like I understand things more when I get to see it write in front of my face.
 
</details>
