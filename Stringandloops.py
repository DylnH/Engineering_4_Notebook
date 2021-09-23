import numpy 

txt = input("Write somethin' ")

letters = list(txt)
array1 = numpy.array(letters) # formats letters vertically

for i in letters:
    newStr = i.replace(' ', '-')  # instead of space, it a "-"
    print(newStr)
