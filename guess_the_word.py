import random

list = ['quality', 'dull', 'cherry', 'symbol', 'angel', 'evening', 'authorise', 'chemistry', 'marriage', 'disturbance']
choice = random.choice(list)
guess = ''
attempts = 5

for letter in choice:
    guess = guess + '*'

print('Guess the word one letter at a time!')
# Write Logic
