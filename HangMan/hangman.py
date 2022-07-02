import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words) # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hang_man():
    word = get_valid_word(words)
    word_letters = set(word) #letters in word
    alphabat = set(string.ascii_uppercase)
    used_letters = set() # what the user has gasssed 

    lives = len(word) * 2
    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join (['a', 'b', 'cd']) --> 'a b cd'
        print('You have ', lives, ' lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        # if letter is used by the user then it will print it othewise it show -
        word_list = [letter if letter in used_letters else '-' for letter in word] 
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabat - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives -1 # takes away a life if wrong
                print('Letter in not in word.')
        
        elif user_letter in used_letters:
            print('You have already used that character. please try another')

        else:
            print('Invalid character. Please try again.')

    # gets here when len(word_letters) == 0

    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('You guessed the word', word, '!!')
     

hang_man()