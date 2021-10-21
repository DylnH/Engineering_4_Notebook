# Engineering_4_Notebook
## Dylan Hensley's Engineering 4 Notebook
 
<details><summary>Dice Roller</summary>
 
## Dice Roller

### Assignment Description

In this assignment, we created a number generator that would pick a random number from 1-6. For this assignment, we needed to use "import random" which is a function that is used to select random results out of possible outcomes. The prgram can also be exited out or give you the option to roll again. This assignment, if done correctly, should have relatively clean code and should be really fun to use.

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

In this assignment we were tasked to create a calculator that could add, subtracted, multiply ,and divide. The catch however, was to do all that, using only one function. By using "doMath" you are able to "do math" and solve simple math equations. The program can be exited out of and can give you the option to calculate again. This assignment will nt take you long, if you know which function to use.

### Evidence 
 
<details><summary>Code</summary>
 
 
 ``` python
 
 # Kalculator

def doMath(x,y,z):
    if(z==1):#addition
        return x + y
    if(z==2):#subtraction
         return x - y
    if(z==3):#mulitplication
         return x * y
    if(z==4):#division
         return round(x / y, 2)

while True:

        x = float(input("Enter 1st number: ")) #type in first input
        y = float(input("Enter 2nd number: ")) #type in second input

        print("Sum:        ", doMath(x,y,1)) #print out possible outcomes
        print("Difference: ", doMath(x,y,2))
        print("Product:    ", doMath(x,y,3))
        print("Quotient:   ", doMath(x,y,4))
        break 

```
 
</details>
 
<img src="https://github.com/DylnH/Engineering_4_Notebook/blob/main/Screenshot%202021-10-05%2010.40.39%20PM.png?raw=true" alt="Screenshot 2021-10-05 10.40.39 PM.png"/>
 
 Onces you start, Type in one number, then the second, and you'll get 4 different outcomes (addition,subraction,multiplication,division)

### Wiring

N/A
 
### Reflection

For this assignment, I had a hard time narrowing my code to 1 function. my original code had 4 function (def add, def subtract, def multiply, and def divide). It took me awhile to learn about the doMath function, but after I did, I was able to finish the assignment "properly" (both ways work the same way if you want to make your own calculator).

 
</details>

<details><summary>Quadratic Calculator</summary>
 
## Quadratic Calculator

### Assignment Description

This program computes roots of a quadratic equation when coefficients a, b and c are typed by the user. for this assignment I used 
"def quadCalc" as the main function. I have trouble with Quadratics in reality so coding I thought would be dificult, but is will not be as bad as it may seem.
	
### Evidence 
 
<details><summary>Code</summary>
 
 
 ``` python
 
#Quadratic Solver


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

In This assignment, I had some problem with the inputs, however that was just a typo I had that I didn't see. I didn't really have any issues. Also, with any assignment, Looking something up will help you understand what is happening and what you need to do. Additinally follow intructions, At first, I didn't read the desrciption for this assignment and just did my own thing. DON'T. I had to redo this one multiple times because of it.
 
</details>

<details><summary>MSP</summary>
 
## Hangman Game
### Assignment Description

In this assignment, we created a hangman game,that can be played by two people. The first player would type in a word, and the game with begin. The second player would guess and a stick figure will gradually form, depending on if the player answers wrong. The concept is pretty staight forward, a standard hangman game. This look a little longer than the rest of the assignments, but thats due to difficulty.

### Evidence 
	
<details><summary>Code</summary>
 
 
 ``` python

 #hangboy

import time

wrongArr = ["________	", # will print one row for every wromg answer
	    "|       |  ",
            "|       O  ",
            "|      /|\\",
            "|      / \\", 
            "|          ",
	    "|		"]
print ("write a word.")

word = input() # Player #1 input setup
time.sleep(1)

print ("\n" * 50)
print ("Guess")
time.sleep(0.5)

guesses = ' '
turns = len(wrongArr)
save = turns
while turns > 0:
    failed = 0 
    for char in word:
        if char in guesses:
            print (char) 

        else:
            print ("_")
            failed += 1

    if failed == 0:
        print ("You won :)")# if you win, print
        break
    print
    guess = input() 
    guesses += guess 

    if guess not in word:
        turns -= 1
        for i in range(save - turns): 
       	    print (wrongArr[i])
        print ("You have", + turns, 'more guesses') # number of guesses

        if turns == 0:
            print ("You lost (x_x)") # death

    print ("_______________________________")

```
 
</details>
 
 <img src="https://github.com/DylnH/Engineering_4_Notebook/blob/main/Screenshot%202021-10-12%20at%203.20.22%20PM.png?raw=true">	
 <img src="https://github.com/DylnH/Engineering_4_Notebook/blob/main/Screenshot%202021-10-12%20at%203.19.39%20PM.png?raw=true">
 
  
 Onces you start, Type in "Roll" and Taa Daa, you should get a number between 1-6. Then if you want to roll again, press "enter", if not, "X"

### Wiring

N/A
 
### Reflection

For this assignment, I had difficulty with the "player input aspect of the assignment. I tried to get away with it by making a random word generator so you can play with yourself,but thats a different project. After I figure that out This helped me solve my issues. [Link to Hangman code](https://inventwithpython.com/invent4thed/chapter8.html)
	
</details>

<details><summary>String and Loop</summary>
 
## String and Loop

### Assignment Description
	
For this assignment, We were tasked to make a program that would print out sentences were written out by a user. In this assignmnt I used numpy array with is a function that can be used to make compact lists in certain formats in very quick time. by using it, you can get your code to look really clean, because there isn't that much to do.


### Evidence 
 
<details><summary>Code</summary>
 
 ``` python
 
 # Loops and string

# Written by Dylan J. Hensley


import numpy 

txt = input("Write somethin' ")

letters = list(txt)
array1 = numpy.array(letters) # formats letters vertically in a list format

for i in letters:
    newStr = i.replace(' ', '-')  # instead of space, it a "-"
    print(newStr)
 
 ```
</details>

 <img src="https://github.com/DylnH/Engineering_4_Notebook/blob/main/Screenshot%20(15).png?raw=true">

First type out some sentences,words,phrase, anythings for that matter, and press "enter" then your program will print it out vertically.
 
