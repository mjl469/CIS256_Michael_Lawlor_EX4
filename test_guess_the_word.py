import random
import pytest
from guess_the_word import word_list

def test_random_word_is_in_list():
    random_word = random.choice(word_list)
    assert random_word in word_list

def test_guess_processing():
    word = 'quality'
    guess = '*******'
    letter_choice = 'l'

    new_guess = ''
    counter = 0
    for letter in word:
        if word[counter] == letter_choice:
            new_guess = new_guess + letter_choice
        else:
            new_guess = new_guess + guess[counter]
        counter = counter + 1
    assert new_guess == '***l***'