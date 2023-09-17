# I added extra creativity by using two words and telling the program to choose any of the two words randomly for the user to guess as seen in line 6-10.
# I also added extra creativity by setting the number of guesses at 10, taking into account the number of potential random words in my list, and I displayed a message to let the players know when they had gone over the limit, if applicable.

import random

# define the list of possible secret words
word_list = ["heaven" , "nephi"]

# select a random secret word from the list
secret_word = random.choice(word_list)

# create a variable to hold the number of user's guesses
player_guesses = 0

# create initial hint for the user to have base knowlege of the number of letters in the secrete word
hint = '_' * len(secret_word)
print('HINT: the Number of underscores are equivalent to the number of letters in the c=secret word.', hint)


# create a loop to play the game
while player_guesses < 0:
    # ask the user for their guess
    guess = input("Please what is your guess: ").lower()

    # increment guesses on each iteration
    player_guesses += 1

    # create a hint for the user based on their guess
    hint = ''

    # check if the guess is the wrong length
    if len(guess) != len(secret_word):
        print("Your guess must have exactly", len(secret_word), "letters.")
        continue

    # check if the guess is the entire secret word
    if guess == secret_word:
        print("Congratulations! You win!")
        print("It took you", player_guesses, "guesses to guess the word.")
        break

    # check if the guess contains all the letters of the secret word but not in the correct order
    if set(guess) == set(secret_word) and guess != secret_word:
        print("Your guess contains all the letters of the secret word, but not in the correct order.")
        continue

    # generate a hint for the user based on their guess
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint += guess[i].upper()
        elif guess[i] in secret_word:
            hint += guess[i].lower()
        else:
            hint += '_'
    print("Your hint is:", hint)

    # check if the user has guessed the whole word
    if hint == secret_word.upper():
        print(f"Congratulations! {guess} You win!")
        print("It took you", player_guesses, "guesses to guess the word.")
        break

    if player_guesses == 10:
        print('\n Game Over! \n You have exceeded the maximum number of tries, Restart and try again')
