
import random


def get_cpu_choice():
    cpu_choice = random.choice(["rock", "paper", "scissors"])
    return cpu_choice


def get_player_choice():
    while True:
        player_choice = input("Choose rock, paper, or scissors: ").lower()

        if player_choice == "rock" or player_choice == "paper" or player_choice == "scissors":
            return player_choice
        else:
            print("Invalid input. Please try again.")


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
    else:
        if player_choice == "rock":
            winner = "PLAYER"
        else:
            winner = "CPU"

    return winner


def play_round():
    cpu_choice = get_cpu_choice()
    player_choice = get_player_choice()

    winner = check_winner(cpu_choice, player_choice)

    print("CPU chose:", cpu_choice)

    if winner == "PLAYER":
        print("Ur the boss! You win this round!")
    elif winner == "CPU":
        print("You are wrong, silly goose! CPU wins this round!")
    else:
        print("It's a tie!")

    return winner


# Tournament
player_wins = 0
cpu_wins = 0
ties = 0

while player_wins < 3 and cpu_wins < 3:
    print("\n--- New Round ---")

    winner = play_round()

    if winner == "PLAYER":
        player_wins += 1
    elif winner == "CPU":
        cpu_wins += 1
    else:
        ties += 1

    print("\nCurrent Score:")
    print("Player:", player_wins)
    print("CPU:", cpu_wins)
    print("Ties:", ties)

# Overall winner
print("\n--- Tournament Over ---")

if player_wins == 3:
    print("Ur the boss! You won the tournament!")
else:
    print("CPU won the tournament! Better luck next time, boss man!")
