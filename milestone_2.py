import random
#creates list of fruits, assigns to the variable "word_list"
word_list = ['apple', 'grape', 'orange', 'watermelon', 'banana']
print(word_list)
#prints a random choice from the list and assigns to a variable "word"
word = random.choice(word_list)
print (word)
#requests and validates user input to choose a letter, assigns to variable "choice"
choice = input("Welcome to Hangman, please enter a letter:")
print("You chose:" + choice)
#if the input is a single letter, prints "good guess", otherwise tells the user that the input is not acceptable
if len(choice) == 1 and choice.isalpha():
        print("Good guess")
else:
        print("Oops! That is not a valid input. Please enter a single letter")
       