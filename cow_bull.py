from msilib import gen_uuid
import random
#create a game cows and bulls
#correct guess cows + 1
#incorrect guess bulls + 1
#track number of guesses 



def generate_random_number():
    number_list = []
    for i in range(4):
        n = random.randint(1,10)
        number_list.append(n)
    #for testing purpse only.
    # print(number_list)
    return number_list

#generate random number.
number_to_guess = generate_random_number()
# print(number_to_guess) #testing only

#track number of guesses.
guesses = 0

while True:

    #track number of cows and bulls.
    cows = 0
    bulls = 0


    #introduction 
    print("Welcome to the Cows and Bulls Game!")
    print("Random Number has been generated!")
    print("Guess a 4-digit number. ")
    print("")

    print("Enter a number")
    my_number = input(">>> ")
    number_list = list(map(int,my_number))

    print(number_list)
    print("-----------------------")


    guesses += 1 #count number of guesses.

    for i in range(4):
        #compare the number_list and number_to_guess to determine
        #if number is in the list
        if number_list[i] == number_to_guess[i]:
            cows += 1
        else:
            bulls += 1

    #check the number of guesses;
    #if number guesses not exceeded continue to guesses.
    if guesses == 4:
        print("You have exceeded the number of guess")
        print(f"number of attempt {guesses}")
        break
    else:

        if cows == 4:
            print("Congrats you have succeeded guessing the numbers!")
            print(f"COWS:{cows}, BULLS:{bulls}")
            print(f"Number of Guesses: {guesses}")
            break
        else:
            print(f"COWS:{cows}, BULLS:{bulls}")
