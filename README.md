 # Hangman 
 ## Table of contents
   | 1. | project description\
   | 2. | class - Hangman\
   | 3. | initialisation\
   | 4. | definition of functions and attributes\


1. ## Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

2.### Class Hangman
>this is the main code for the hsangman game, with 2 arguments num_lives and word_list
cdcd
>3. ### Functions and Attributes
>#### Attribute
word_list = list of words the computer selects from
>num_lives = number of lives (5)
>word = word selected at random for player to guess
>word_guessed = letters guessed by the player
>num_letters = number of unique letters in the secret word
>list_of_guesses = guesses made by player

>#### Functions

>__init__self, word_list, num_lives  - Initializes the Hangman game with the provided word_list and optional number of lives
> display_word - returns the word to guess from the list
> display_guesses - returns list of guessed letters
> ask_letter - Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method
> check_letter(self, letter) - Checks if the letter is in the word. If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1



