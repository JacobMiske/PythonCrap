high = 100
low = 0
guess = (high + low)/2  


print('Please think of a number between 0 and 100!')

guessing = True
while guessing:
    print('Is your secret number ' + str(guess) + '?')
    pointer = input("Enter 'h' to indicate the guess is too high. \
    Enter 'l' to indicate the guess is too low. \
    Enter 'c' to indicate I guessed correctly.")
    if pointer == 'h':
        high = guess
        guess = ((low + guess)/2)

    elif pointer == 'l':
        low = guess
        guess = ((high + guess)/2)

    elif pointer == 'c':
        guessing = False

print('Game over. Your secret number was: ' + str(guess))