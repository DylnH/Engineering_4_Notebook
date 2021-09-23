import numpy 

txt = input("Write somethin' ")

letters = list(txt)
array1 = numpy.array(letters)

for i in letters:
    newStr = i.replace(' ', '-') 
    print(newStr)