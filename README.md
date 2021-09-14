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
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(A/S/M/D): ")

    # check if choice is one of the four options
    if choice in ('A', 'S', 'M', 'D'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 'A':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == 'S':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == 'M':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == 'D':
            print(num1, "/", num2, "=", divide(num1, num2)) 
```
