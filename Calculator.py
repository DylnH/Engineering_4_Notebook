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
