# This script prompts the user to guess a number between 1 and 100.
import random

def computerGuess(lowval,highval,randdum, count=0):
    if highval >= lowval:
        guess = lowval + (highval - lowval) // 2
        if guess ==randdum:
            return count
        elif guess >randdum:
            count += 1
            return computerGuess(lowval, guess - 1, randdum, count) 
        else:
            count += 1
            return computerGuess(guess + 1, highval, randdum, count)    
    else:
        return -1

randdum = random.randint(1,101)
count = 0
guess = -99

while (guess != randdum):
    guess = (int)(input("enter your guess between 1 and 100: "))
    if guess <randdum:
        print("Higher")
    elif guess >randdum:
        print("Lower")
    else:
        print("You guessed it right!")
        break
    count = count + 1
#end of while loop

print ("You took " + str(count) + " steps to guess the number.")
print ("The computer took " + str(computerGuess(1, 100, randdum)) + " steps to guess the number."   )