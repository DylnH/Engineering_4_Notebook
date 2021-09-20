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