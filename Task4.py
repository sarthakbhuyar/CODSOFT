import random

def get_user_choice():
    print("Choose rock, paper, or scissors:")
    user_choice = input().lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors:")
        user_choice = input().lower()
    return user_choice

def get_computer_choice():
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'Tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return 'User'
    else:
        return 'Computer'

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    print(f"User chose {user_choice}, computer chose {computer_choice}.")
    print(f"{winner} wins!")

def play_again():
    print("Do you want to play again? (yes/no)")
    return input().lower() == 'yes'

def main():
    while True:
        play_game()
        if not play_again():
            break

if __name__ == "__main__":
    main()