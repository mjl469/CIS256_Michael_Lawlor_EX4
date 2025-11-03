import random

#Creating necessary initial variables
list = ['quality', 'dull', 'cherry', 'symbol', 'angel', 'evening', 'authorise', 'chemistry', 'marriage', 'disturbance']
choice = random.choice(list)
guess = ''
attempts = 5

for letter in choice:
    guess = guess + '*'

print('Guess the word one letter at a time!')

# Writing game logic
while guess != choice:

    print(f'Remaining attempts: {attempts}')
    print(f'{guess}\n')
    letter_choice = input('Enter a letter: ').lower()

    if len(letter_choice) == 1:

        if letter_choice in choice:
            new_guess = ''
            counter = 0
            for letter in choice:
                if choice[counter] == letter_choice:
                    new_guess = new_guess + letter_choice
                else:
                    new_guess = new_guess + guess[counter]
                counter = counter + 1
            guess = new_guess

        else:
            print(f'The word does not contain the letter: {letter_choice}\n')
            attempts = attempts - 1

    else:
        print('Please enter one letter guesses only.\n')



