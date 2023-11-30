def check_guess(choice): #checks to see if the random word contains the players' guess
          guess = choice.lower()
          if guess in secret_word:
                    print(f"You have chosen wisely, {guess} is in the word")
          else:
                    print(f"You have chosen unwisely {guess} is not in the word. The hangman's noose is tightening.")

check_guess('a')
