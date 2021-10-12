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

<details><summary>Calculator</summary>
 
## Calculator

### Assignment Description


### Evidence 
 
<details><summary>Code</summary>
 
 
 ``` python
 
 # Kalculator

# Written by [Dylan J. Hensley]

def doMath(x,y,z):
    if(z==1):#addition
        return x + y
    if(z==2):#subtraction
         return x - y
    if(z==3):#mulitplication
         return x * y
    if(z==4):#division
         return round(x / y, 2)
    if(z==5):#modulo
         return x % y

while True:

        x = float(input("Enter 1st number: ")) #type in first input
        y = float(input("Enter 2nd number: ")) #type in second input

        print("Sum:        ", doMath(x,y,1)) #print out possible outcomes
        print("Difference: ", doMath(x,y,2))
        print("Product:    ", doMath(x,y,3))
        print("Quotient:   ", doMath(x,y,4))
        print("Modulo:     ", doMath(x,y,5))
        break 

```
 
</details>
 
<img src="https://github.com/DylnH/Engineering_4_Notebook/blob/main/Screenshot%202021-10-05%2010.40.39%20PM.png?raw=true" alt="Screenshot 2021-10-05 10.40.39 PM.png"/>
 
 Onces you start, Type in one number, then the second, and you'll get 5 different outcomes (addition,subraction,multiplication,division,moduli)

### Wiring

N/A
 
### Reflection

 
</details>

<details><summary>Quadratic Calculator</summary>
 
## Quadratic Calculator

### Assignment Description


### Evidence 
 
<details><summary>Code</summary>
 
 
 ``` python
 
#Quadratic Solver


#Written by: Dylan J. Hensley

def quadCalc(a,b,c): # quadCalc = do quadratic/advanced math calculations
  intA = int(a)
  intB = int(b) 
  intC = int(c) 
  disc = ((intB*intB)-(4*intA*intC)) 
  Q1 = (-intB / (2*intA))
  if disc < 0: # if disc < 0 = calculate, then if answer is determind to have no real roots,print
    return("no real roots.".format(intA, intB, intC))
  if disc == 0: # if disc == 0 = calculate, then if answer is determind to have real roots,print
    return("The root =: {0}".format(Q1)) 
  if disc > 0: 
    pos = ((disc**0.5)/(2*intA)) 
    w = round((Q1 - pos),5) 
    x = round((Q1 + pos),5) 
    return([w,x]) 

while True:
    print("Enter coefficients") #Asking for user input
    a = input("Enter 1st coefficient: ") #input of 1st number
    b = input("Enter 2nd coefficient: ") #input second number
    c = input("Enter 3rd coefficient: ") #input third number
    returnVal = quadCalc(a,b,c)
    if isinstance(returnVal,list): 
      print("Two roots:")
      for root in returnVal:
        print(root)
    else:
      print(returnVal) 

```
 
</details>
 
<img src="https://github.com/DylnH/Engineering_4_Notebook/blob/main/Screenshot%202021-10-05%2010.58.30%20PM.png?raw=true" alt="Screenshot 2021-10-05 10.58.30 PM.png"/>
 
 Onces you start, Type in one number, then the second, then the third and you'll get your answer. (real roots or no real roots as well)

### Wiring

N/A
 
### Reflection

 
</details>

<details><summary>MSP</summary>
 
## Hangman Game
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

<details><summary>String and Loop</summary>
 
## String and Loop

### Assignment Description


### Evidence 
 
 <img src="https://github.com/DylnH/Engineering_4_Notebook/blob/main/Screenshot%20(15).png?raw=true">
 
<details><summary>Code</summary>
 
 
 ``` python
