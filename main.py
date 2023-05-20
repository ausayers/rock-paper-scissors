import random


def get_choices():
    # get player choice, computer choice, and return a dictionary of values
    player_choice = input("Enter a choice (rock, paper, scissors): ")

    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    # compare player and computer choices, return an explanatory string
    print(f"You chose {player}, computer chose {computer}.")

    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose..."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose."
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose."
    else:
        return "Invalid Choice.."


choices = get_choices()  # dictionary containing player and computer choices
result = check_win(choices["player"], choices["computer"])

print(result)
