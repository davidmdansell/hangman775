import random
#creates list of fruits, assigns to the variable "hangman_word_list"
def secret_word():
    hangman_word_list = ['apple', 'grape', 'orange', 'watermelon', 'banana']
    print(hangman_word_list)
#prints a random choice from the list and assigns to a variable "word"
    secret_word = random.choice(hangman_word_list)
    return(secret_word)
print (secret_word)
#requests and validates user input to choose a letter, assigns to variable "choice"
def ask_for_input():
            choice = input("Welcome to Hangman, please enter a letter:")
            print("You chose:" + choice)
            if len(choice) == 1 and choice.isalpha():
                      print("Thankyou")
            else: 
                    print("Oops! That is not a valid input. Please enter a single letter")
            check_guess(choice)


       