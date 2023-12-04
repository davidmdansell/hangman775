import random


class Hangman:
    def __init__(self, word_list, num_lives=5):

        """Initializes the Hangman game with the provided word_list and optional num_lives"""
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        word_list = ['apple', 'orange', 'banana', 'watermelon', 'peach', 'grapes']

    def display_word(self):
        """returns the word to guess from the list"""
        return ' '.join(self.word_guessed)

    def display_guesses(self):
        """returns list of guessed letters"""
        return ', '.join(self.list_of_guesses)

    def ask_letter(self):
        """Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method"""
    
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
            

word_list = ['apple', 'orange', 'banana', 'watermelon', 'peach', 'grapes']
play_game = Hangman(word_list)
"""initiates instance of the hangman game with 5 lives and using the fruits listed in word_list"""
print("Welcome to Hangman!")
print("Word to guess:", play_game.display_word())
print("Number of lives:", play_game.num_lives)

while '_' in play_game.word_guessed and play_game.num_lives > 0:
    guess = input("Enter a letter: ").lower()

    if guess in play_game.list_of_guesses:
        print("You already guessed that letter. Try again.")
    else:
        play_game.list_of_guesses.append(guess)
        if guess in play_game.word:
            for i in range(len(play_game.word)):
                if play_game.word[i] == guess:
                    play_game.word_guessed[i] = guess
            print("Good guess!")
        else:
            play_game.num_lives -= 1
            print("Incorrect guess. Lives remaining:", play_game.num_lives)

        print("Word:", play_game.display_word())
        print("Previous guesses:", play_game.display_guesses())

if '_' not in play_game.word_guessed:
    print("Congratulations! You won the game:", play_game.word)
else:
    print("Sorry, you ran out of lives. The correct word was:", play_game.word)

    def check_letter(self, letter):
        """Checks if the letter is in the word. If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1."""
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
            print(f"Sorry, {letter} is not in the word", self.num_lives)
            print(f"You have {self.num_lives} left")

        print("Word:", self.display_word())
        print("Previous guesses:", self.display_guesses())
        
   





