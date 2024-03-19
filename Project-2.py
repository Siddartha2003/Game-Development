import random

def play_game():
    game_options = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0
    
    print("This game has three rounds!!!")
    
    for _ in range(3):
        while True:
            player_choice = input("Rock / Paper / Scissors: ").lower()
            if player_choice in game_options:
                break
            print("Please enter a valid input (Rock, Paper, or Scissors)")

        computer_choice = random.choice(game_options)
        
        if (player_choice == "rock" and computer_choice == "scissors") or \
           (player_choice == "paper" and computer_choice == "rock") or \
           (player_choice == "scissors" and computer_choice == "paper"):
            player_score += 1
        elif (player_choice == "rock" and computer_choice == "paper") or \
             (player_choice == "paper" and computer_choice == "scissors") or \
             (player_choice == "scissors" and computer_choice == "rock"):
            computer_score += 1
        
        print("Player\t\t\tComputer")
        print(f"{player_choice.capitalize()} - {player_score}\t{computer_choice} - {computer_score}")

    if computer_score > player_score:
        print("You Lost :(")
    elif player_score > computer_score:
        print("You won :)")
    else:
        print("Tie")

def main():
    play = input("Do you want to play? ").lower()
    if play != "yes":
        quit()
    
    while True:
        print("Okay! Let's play :)\n")
        play_game()
        play_again = input("Do you want to play again? (Yes/No): ").lower()
        if play_again != "yes":
            print("Game Over")
            break

if __name__ == "__main__":
    main()
