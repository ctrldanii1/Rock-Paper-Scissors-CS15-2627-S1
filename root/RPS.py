
import random

from root.main import ties


def get_cpu_choice():
    cpu_choice = random.choice(["rock", "paper", "scissors"])
    return cpu_choice

def get_player_choice():
    while True:
        player_choice = input("Choose your choice: rock, paper, or scissors: ") .lower()
        if player_choice == "rock" or player_choice == "paper" or player_choice == "scissors":
            return player_choice

def check_winner(cpu_choice, player_choice):
    if player_choice == cpu_choice:
         winner = "Tie"
    elif cpu_choice == "rock":
        if player_choice == "paper":
             winner = "PLAYER"
        else:
             winner = "CPU"


    elif cpu_choice == "paper":
        if player_choice == "scissors":
            winner = "PLAYER"
        else:
            winner = "CPU"

    elif player_choice == "paper":
            winner = "CPU"
    else:
            winner = "PLAYER"
    return winner


def play_round():
    cpu_choice = get_cpu_choice()
    player_choice = get_player_choice()
    winner = check_winner(cpu_choice, player_choice)
    return winner


player_wins = 0
cpu_wins = 0
ties = 0
while True:
    winner = play_round()
    if winner == "Tie":
        ties += 1
    elif winner == "PLAYER":
        ties += 1
    elif winner == "CPU":
        ties += 1
    else:
        pass

    print("Player:", player_wins)
    print("CPU:", cpu_wins)
    print("Ties:", ties)

    if player_wins == 3 or cpu_wins == 3:
        break

 if player_wins == 3
     print("PLAYER WINS!!!")
 else:
     print("CPU WINS!!!")

