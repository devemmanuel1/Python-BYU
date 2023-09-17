import random

play_again = True # Flag

while play_again:

    magic_number = random.randint(1, 100)
    cont = 0
    exit = False # Flag

    while not exit:
        cont+=1
        guess = int(input('What is your guess? '))

        if magic_number > guess:
            print('Higher')
        elif magic_number < guess:
            print('Lower')
        else:
            exit = True
            print('You guessed it!')

    print(f'Tries: {cont}')

    ans = input('Do you want to play again? (yes | no) ').lower()
    if ans == 'no':
        play_again = False