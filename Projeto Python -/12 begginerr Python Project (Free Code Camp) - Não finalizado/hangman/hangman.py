import random
import string
from hangman.words import words

def get_valid_word(words):
    word = random.choice(words)

    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    while len(word_letters) > 0 and lives > 0:

        print(f"You have {lives} life\n")
        print("You have used these letters: ", ' '.join(used_letters))
        

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                live =- 1
                print(f"\nYour letter, {user_letter} is not in the word.")

        elif user_letter in user_letter:
            print(f"You have already used that character. Please try again.")

        else:
            print("Invalid character. Please try again.")
    
    if lives == 0:
        print("You died, SORRY. The word was", word)
    
    else:
        print("YAY! You guessesd the word", word, "!")


if __name__ == '__main__':
    hangman()