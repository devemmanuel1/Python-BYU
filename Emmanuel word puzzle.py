#I added extra creativity by adding my name to the welcome print function in line line 6
import random

# List of possible secret words
# print welcome message
print("Welcome to EMMANUEL'S WORD PUZZLE !!!\n")
secret_words = ['honey', 'pasta']

# Choose a random word from the list
secret_word = random.choice(secret_words)

# Initialize the number of guesses made by the user
num_guesses = 0

# Display the initial hint with underscores for each letter of the secret word
hint = '_' * len(secret_word)
print('Your hint is:', hint)

# Keep prompting the user for guesses until they guess the word correctly
while True:
    # Get a guess from the user and convert it to lowercase
    user_guess = input('Enter your guess: ').lower()

    # If the guess has a different number of letters than the secret word, display an error message
    if len(user_guess) != len(secret_word):
        print('Your guess must have', len(secret_word), 'letters.')
        num_guesses += 1
        continue

    # Increment the number of guesses made by the user
    num_guesses += 1

    # Check each letter of the guess against the secret word and build the hint
    hint = ''
    for i in range(len(secret_word)):
        if user_guess[i] == secret_word[i]:
            hint += user_guess[i].upper()
        elif user_guess[i] in secret_word:
            hint += user_guess[i].lower()
        else:
            hint += '_'

    # Display the hint
    print('Your hint is:', hint)

    # If the user guessed the word correctly, end the game and display the number of guesses made
    if user_guess == secret_word:
        print('Congratulations, you guessed the word in', num_guesses, 'guesses!')
        break


