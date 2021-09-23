import time

wrongArr = ["________	",
	    "|       |  ",
            "|       O  ",
            "|      /|\\",
            "|      / \\", 
            "|          ",
	    "|		"]
print ("write a word.")

word = input()
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