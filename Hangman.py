import random

# List of 5 predefined words
words = ["python", "school", "computer", "student", "coding"]

# Choose a random word
word = random.choice(words)

# Create blanks for the word
guessed_word = ["_"] * len(word)

# Store letters that have already been guessed
guessed_letters = []

# Number of incorrect guesses allowed
incorrect_guesses = 0
max_guesses = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")

# Game loop
while incorrect_guesses < max_guesses and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Guessed letters:", guessed_letters)
    print("Incorrect guesses:", incorrect_guesses, "/", max_guesses)

    # Get a letter from the player
    guess = input("Enter a letter: ").lower()

    # Check if the input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter only.")

    elif guess in guessed_letters:
        print("You already guessed that letter.")

    else:
        guessed_letters.append(guess)

        # Check if the letter is in the word
        if guess in word:
            print("Correct guess!")

            # Reveal the correct letter
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess

        else:
            incorrect_guesses += 1
            print("Incorrect guess!")

# Check the result
if "_" not in guessed_word:
    print("\nCongratulations!")
    print("You guessed the word:", word)

else:
    print("\nGame over!")
    print("The correct word was:", word)