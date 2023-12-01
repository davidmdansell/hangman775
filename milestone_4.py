import random

class Hangman:
    def __init__(self, word_list, num_lives=5):

    #Initializes the Hangman game with the provided word_list and optional num_lives.
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def display_word(self):
        return ' '.join(self.word_guessed)

    def display_guesses(self):
        return ', '.join(self.list_of_guesses)

    def ask_letter(self):
    #Asks the user for a letter and checks two things:
    # 1. If the letter has already been tried
    # 2. If the character is a single character\
    # If it passes both checks, it calls the check_letter method.
    
        while True:
            # Ask the user for a letter
            letter = input("Enter a letter: ").lower()

            # Check if the letter is a single character
            if len(letter) != 1:
                print("Please, enter just one character.")
                continue

            # Check if the letter has already been tried
            if letter in self.list_of_guesses:
                print(f"{letter} was already tried.")
                continue

            # If the letter is valid, call the check_letter method
            self.check_letter(letter)
            break

    def check_letter(self, letter):
# Checks if the letter is in the word.
# If it is, it replaces the '_' in the word_guessed list with the letter.
# If it is not, it reduces the number of lives by 1.

        letter = letter.lower()
        if letter in self.word:
            # Replace '_' in the word_guessed list with the letter for each occurrence
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.word_guessed[i] = letter

            # Update the number of UNIQUE letters in the word that have not been guessed yet
            self.num_letters -= 1

            print("Good guess!")
        else:
            # Reduce the number of lives by 1
            self.num_lives -= 1
            print("Incorrect guess. Lives remaining:", self.num_lives)

        print("Word:", self.display_word())
        print("Previous guesses:", self.display_guesses())
