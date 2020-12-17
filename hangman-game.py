import random
from words import words
import string

# Removing words with '-' or whitespace
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.lower()

def hangman():
    print("*********Welcome to the Hangman's Game*********")
    print("You have to Guess the letters that fits the blanks below which indicate a word")
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_lowercase)
    used_letters = set()
    lives = 10
    while len(word_letters) > 0 and lives > 0:
        print('You have used these letters:',used_letters)
        print('You have {} lives left..'.format(lives))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Curent word: ',' '.join(word_list))
        user_input = input('Guess a letter: ').lower()
        if user_input in (alphabet - used_letters):
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)

            else:
                lives -= 1

        elif user_input in used_letters:
            print('You have already used that letter!')
        else:
            print("Invalid character!")

    if len(word_letters) == 0:
        print("Congrats! you have guessed the word {} correctly!".format(word.upper()))
    elif lives == 0:
        print("Sorry! You Lost all your lives & your hangman dies!")
        print("The word was:",word.upper())

hangman()
