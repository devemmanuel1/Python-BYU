import random

# I started the game with a list of words, and select a random word for the secret word using imported random module

# define the list of possible secret words
# print welcome message
print('Welcome to CALIBRAIN OWRD PUZZLE!!!\n')

words_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "jicama", "kiwi", "lemon", "mango", "nectarine", "orange", "peach", "quince", "raspberry", "strawberry", "tangerine", "ugli", "vanilla", "watermelon", "xigua", "zucchini"]

# select a random secret word from the list
secret_word = random.choice(words_list)

# create a list to hold the user's guesses
player_guesses = []

hint = '_' * len(secret_word)
print('Take the number of the underscores to be the number of letters contained in the secret word :',hint)
# create a loop to play the game
while True:
    # create a hint for the user
    hint = ""
    for letter in secret_word:
        if letter in player_guesses:
            hint += letter.upper()
        else:
            hint += "_"

    # ask the user for their guess
    guess = input("Guess a letter or the whole word: ").lower()

    # check if the guess is the entire secret word
    if guess == secret_word:
        print("Congratulations! You win! The secrete word is", guess.upper())
        print("It took you", len(player_guesses), "player_guesses to guess the word.\n Wrong Guesses:", player_guesses)
        break
    # check if the guess is the wrong length
    elif len(guess) != len(secret_word):
        print("Your guess must have", len(secret_word), "letters.")
        continue

    # add the guess to the list of player_guesses
    player_guesses.append(guess)

    # create a hint for the user based on their guess
    hint = ""
    for i, letter in enumerate(secret_word):
        if letter == guess[i]:
            hint += letter.upper()
        elif letter in player_guesses:
            hint += letter.lower()
            print('Guesses that contain some letters included the secrete word \n', player_guesses)
        else:
            hint += "_"
    print("Your hint is:", hint)

