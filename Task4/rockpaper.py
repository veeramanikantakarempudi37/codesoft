import random

user_score = 0
computer_score = 0

while True:
    print("\n--- Rock Paper Scissors Game ---")
    print("Choose: rock, paper, or scissors")

    user = input("Enter your choice: ").lower()

    if user not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please try again.")
        continue

    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    # Game Logic
    if user == computer:
        print("Result: It's a Tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("Result: You Win!")
        user_score += 1

    else:
        print("Result: Computer Wins!")
        computer_score += 1

    # Display Scores
    print("\nScores:")
    print("User Score:", user_score)
    print("Computer Score:", computer_score)

    # Play Again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nFinal Scores:")
        print("User Score:", user_score)
        print("Computer Score:", computer_score)
        print("Thanks for playing!")
        break