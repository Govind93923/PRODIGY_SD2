import random


def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Welcome to the Guessing Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")

    while not guessed:
        # Prompt the user for a guess
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            # Provide feedback
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    guessing_game()
