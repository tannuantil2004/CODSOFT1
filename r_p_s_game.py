import random

def winner(u1_name, u1_choice, u2_name, u2_choice):
    if u1_choice == u2_choice:
        return "It's a tie!"
    elif (u1_choice == 1 and u2_choice == 3) or \
         (u1_choice == 2 and u2_choice == 1) or \
         (u1_choice == 3 and u2_choice == 2):
        return f"{u1_name} wins!"
    else:
        return f"{u2_name} wins!"

def get_choice(user_name):
    while True:
        try:
            choice = int(input(f"{user_name}, enter your choice (1 for Rock, 2 for Paper, 3 for Scissors): "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice. Please choose 1 for Rock, 2 for Paper, or 3 for Scissors.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_with_computer(user_name):
    user_score = 0
    computer_score = 0
    
    while True:
        print(f"\nScore - {user_name}: {user_score}  Computer: {computer_score}")
        user_choice = get_choice(user_name)
        computer_choice = random.randint(1, 3)
        print(f"Computer chooses: {computer_choice}")
        
        result = winner(user_name, user_choice, "Computer", computer_choice)
        print(result)
        
        if result == f"{user_name} wins!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Game ended. Final scores:")
            print(f"{user_name}: {user_score}  Computer: {computer_score}")
            break

def play_with_friend(u1_name, u2_name):
    u1_score = 0
    u2_score = 0
    
    while True:
        print(f"\nScore - {u1_name}: {u1_score}  {u2_name}: {u2_score}")
        u1_choice = get_choice(u1_name)
        u2_choice = get_choice(u2_name)
        
        result = winner(u1_name, u1_choice, u2_name, u2_choice)
        print(result)
        
        if result == f"{u1_name} wins!":
            u1_score += 1
        elif result == f"{u2_name} wins!":
            u2_score += 1
        
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Game ended. Final scores:")
            print(f"{u1_name}: {u1_score}  {u2_name}: {u2_score}")
            break

def main():
    print("Welcome to Rock-Paper-Scissors Game!")
    print("Rules: 1 for Rock, 2 for Paper, and 3 for Scissors.")
    
    while True:
        print("\nChoose an option:")
        print("1. Play with computer")
        print("2. Play with a friend")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            user_name = input("Enter your name: ")
            play_with_computer(user_name)
        elif choice == '2':
            u1_name = input("Enter name of User 1: ")
            u2_name = input("Enter name of User 2: ")
            play_with_friend(u1_name, u2_name)
        elif choice == '3':
            print("Exiting Rock-Paper-Scissors Game. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
