import random

option = ("rock","paper","scissors")
playing = True

while playing:

    player = None
    computer = random.choice(option)

    while player not in option:
        player = input("enter a choice (rock, paper, scissors): ")

    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("it's a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer == "rock":
        print("you win")
    elif player == "scissors" and computer == "paper":
        print("you win")
    else:
        print("you lose")

    if not input("play again? (yes/no): ").lower() == "yes":
        playing = True

    print("thanks for playing")   
