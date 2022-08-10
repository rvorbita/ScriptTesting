#Rock Paper Scissors Game
#Rock beats scissors
#Scissors beats paper
#Paper beats rock
import random


p1_score=0
cpu_score=0
draw=0
turn=0
game=True


def Turn_Generator():

    cpu = ['rock', 'paper', 'scissors']
    turn = random.choice(cpu)

    return turn

def Check_Wins(p1, cpu):

    global p1_score, cpu_score, draw
    
    if p1.lower() == 'rock' and cpu == 'scissors':
        p1_score += 1
        print("P1 Wins!")
    elif p1.lower() == 'scissors' and cpu =='rock':
        cpu_score += 1
        print("CPU Wins!")
    elif p1.lower() == 'scissors' and cpu == 'paper':
        p1_score += 1
        print("P1 Wins")
    elif p1.lower() == 'paper' and cpu == 'scissors':
        cpu_score += 1
        print("CPU Wins")
    elif p1.lower() == 'paper' and cpu == 'rock':
        p1_score += 1
        print("P1 Wins")
    elif p1.lower() == 'rock' and cpu == 'paper':
        cpu_score += 1
        print("CPU Wins")


    if p1.lower() == 'rock' and cpu == 'rock':
        draw += 1
        print("Draw No One Wins!")

    elif p1.lower() == 'paper' and cpu == 'paper':
        draw += 1
        print("Draw No One Wins!")

    elif p1.lower() == 'scissors' and cpu == 'scissors':
        draw += 1
        print("Draw No One Wins!")

while game:
    print("")
    print("******************************************")
    print("*Welcome to the Rock Paper Scissors Game!*")
    print("******************************************")
    print("Choose from Rock, Paper, Scissors and Type 'Q' to Quit the Game.")
    print("---")

    p1=input("P1 Turn > ")

    if p1.lower() == 'q':

        print("")
        print("******************************")
        print(": GAME SUMMARY :")
        print(f"P1 Wins = {p1_score}")
        print(f"CPU wins = {cpu_score}")
        print(f"Game Draws = {draw}")
        print(f"Number of Game Turns = {turn}")
        print("---")

        print("Thank you for playing!")
        print("*******************************")
        print("")

        break

    if p1.lower() != 'rock' and p1.lower() != 'paper' and p1.lower() != 'scissors':
        print("Invalid Parameters")
        print("Type Only Rock, Paper, Scissors or 'Q' to quit")
    else:
        cpu = Turn_Generator()
        print(f"CPU Choose > {cpu}")
        Check_Wins(p1, cpu)
        turn += 1






