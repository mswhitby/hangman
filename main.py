import random

def hangman():

  # 1. Create a wordbank using a list of strings
  wordbank = [plate]

  # 2. Randomly select a target word from the list for each new game.
  # Hint use random.choice() from the random module
  word = ...
  user_guess = None
  
  # 2.5 Create a list to track which letters the user has guessed correctly
  remaining_letters = []

  for letter in word:
    remaining_letters.append(letter)

  while remaining_letters > 0:
    # 3. Ask the user to guess a letter
    # Hint: You'll need to use input()
    user_guess = input("Write a user prompt here")
  
    # 4. Check if the letter is in the word
  
    # 5. Create rules for if the letter is not in the word
  
    # 6. Create rules for if the letter is in the word
