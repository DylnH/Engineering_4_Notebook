# Engineering_4_Notebook
Dylan Hensley's Engineering 4 Notebook

## Circuit Python

### Hello Python
   
   ``` python
# Automatic Dice Roller

# Written by [Dylan J. Hensley]

print ("🎲Automatic Dice Roller🎲:") # Title

import random
roll_dice = input("🎲Roll The Dice ⬇") # Telling you to Roll the Dice

if roll_dice == "Roll": # What you write to roll the Dice
   posiblle_results = [6, 5, 4, 3, 2, 1] # possible outcomes
   result = random.choice(posiblle_results) # Picks out a random number
   print("You rolled a... " + str(result)) # Tells you the random number 
```
___________________________________________________________________________________________________________________________________________________________________________________

### Python Program 01 – Calculator (Hello Functions)
   
   ``` python
# Kalculator

# Written by [Dylan J. Hensley]
   
def add(x, y): # adds two numbers
    return x + y
def subtract(x, y): # subtracts two numbers
    return x - y
def multiply(x, y): # multiply two numbers
    return x * y
def divide(x, y): # divide two numbers
    return x / y


print("Select operation.") # Shows options/what you want to calculate
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    
    choice = input("Enter choice(A/S/M/D): ") # what you write to Add/Subtract/Multiply/Divide

    if choice in ('A', 'S', 'M', 'D'): # check if choice is one of the four options
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 'A':
            print(num1, "+", num2, "=", add(num1, num2)) # setup for Adding

        elif choice == 'S':
            print(num1, "-", num2, "=", subtract(num1, num2)) # setup for subtracting

        elif choice == 'M':
            print(num1, "*", num2, "=", multiply(num1, num2)) # setup for multiplying

        elif choice == 'D':
            print(num1, "/", num2, "=", divide(num1, num2)) # setup for Dividing 
```
_________________________________________________________________________________________________________________________________________________________________________________

### Python Program 02 – # Quadratic Solver

   ``` python
# Quadratic Solver

# Written by Dylan J. Hensley 

import math
a=float(input("Enter the coefficient a ")) # type in coefficient a
b=float(input("Enter the coefficient b ")) # type in coefficient b
c=float(input("Enter the coefficient c ")) # type in coefficient c
d=b*b-4*a*c;

if d>0:
    r1 = (-b + math.sqrt(d)) / (2 * a) # show answer
    r2 = (-b - math.sqrt(d)) / (2 * a)
    print("Roots are real and unequal ",r1, " and ",r2) # if roots are real and unequal
elif d==0:
    r1=-b/(2*a)
    print("Roots are real and equal ",r1) # if roots are real
else:
    print("No real roots ") # if there's no roots

```
