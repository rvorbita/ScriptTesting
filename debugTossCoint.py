import random

#find a way to incorporate the random numbers to the user inputs 
#key to value  #dic
#raise an exception if the user input non heads or tails.

print('Guess the coin toss! Enter heads or tails:')
guess = input()
guessConverter = {0: 'heads', 1: 'tails'}

if guess != 'heads' and guess != 'tails':
    raise Exception("Enter only string (heads or tails).")

toss = guessConverter[random.randint(0, 1)] # 0 is tails, 1 is heads

if toss == guess:
    print('You got it!')
    
else:
    print('Nope! Guess again!')
    guesss = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')