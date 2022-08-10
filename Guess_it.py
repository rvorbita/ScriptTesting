import random


life = 0 #number of tries
guesses = 0 #track number of guess


#FUNCTIONS
def Gen_Rdm_Num(n):

    if n == 1:
        n = random.randint(1, 9)
    elif n == 2:
        n = random.randint(1, 30)
    elif n == 3:
        n = random.randint(1, 50)
    return n

def Game_Summary(name,guesses):

    print("************")
    print("Game Summary")
    print(f"Hello,{name}")
    print(f"Number of guess {guesses}")
    print("************")
    print("")


def Game_Validation(user_guess, r_number):

    if user_guess < r_number:
        print("Your guess is to low.")

    elif user_guess > r_number:
        print("Your guess is to high.")

    else:
        print("Your guess is correct!.")
        Game_Summary(username, guesses)


#GAMELOOP.
while True:

    print("")
    #START PROGRAM.
    print("******************************************************")
    print("             Welcome to Guessing Game                 ")
    print("     Type 1-EASY(1-9), 2-MEDIUM(1-30), 3-HARD(1-50)   ")
    print("You can only Guess '3' times > Type 'exit' to Stop.   ")
    print("System will reply if low , high or you guess it right.")
    print("******************************************************")

    #player username before game start.
    username = input("Enter your Name: ")

    #difficulty
    diff_option = int(input("Enter number of difficulty >  "))
    print(f"You have chosen the number '{diff_option}' ")

    #generate random number to be guess.
    r_number = Gen_Rdm_Num(diff_option)

    print("Generating Random Number...")
    print("....")
    print("..")
    print(".")
    print("Random Number Generated.")
    print(r_number) #for testing purposes.


    guesses += 1
    life += 1


    user_guess = input("Enter your guess number: > ")

    if life == 3:
        print("You have exceeded the maximum number of guesses.")
        Game_Summary(username, guesses)
        break
        

    if user_guess.lower() == "exit":
        print("Thank you for playing the game!")
        break

    #convert the user guess into int.
    user_guess = int(user_guess)

    #guess checking
    Game_Validation(user_guess, r_number)

    play_again=input("You want to play again? Type 'Y' to play. > ")

    if play_again.lower() == 'n':
        print("Thank you for playing the Game!")
        break







