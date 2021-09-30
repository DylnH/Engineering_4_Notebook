#Quadratic Solver


#Written by: Dylan J. Hensley

def quadCalc(a,b,c): 
  intA = int(a) 
  intB = int(b) 
  intC = int(c) 
  disc = ((intB*intB)-(4*intA*intC)) 
  Q1 = (-intB / (2*intA))
  if disc < 0: 
    return("no real roots.".format(intA, intB, intC))
  if disc == 0:
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
