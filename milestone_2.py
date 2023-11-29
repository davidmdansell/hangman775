import random
word_list = ['apple', 'grape', 'orange', 'watermelon', 'banana']
print(word_list)
word = random.choice(word_list)
print (word)

choice = input("Welcome to Hangman, please enter a letter:")
print("You chose:" + choice)

if len(choice) == 1 and choice.isalpha():
        print("Good guess")
else:
        print("Oops! That is not a valid input. Please enter a single letter")
       