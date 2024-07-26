import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize the number of guesses
num_guesses = 0

while True:
    # Prompt the user to guess the number
    guess = int(input("Guess a number between 1 and 100: "))

    # Increment the number of guesses
    num_guesses += 1

    # Check if the guess is correct
    if guess == secret_number:
        print(f"Congratulations! You guessed the number in {num_guesses} guesses.")
        break
    elif guess < secret_number:
        print("Your guess is too low. Try again.")
    else:
        print("Your guess is too high. Try again.")