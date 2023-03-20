[Open on Replit](https://replit.com/@whs-spring-2023/Hangman-Tips-whs-spring-2023)

# Hangman (due 3/24/23)

Create a program that simulates a game of Hangman. The program should randomly select a word from a list and then prompt the user to guess letters in the word. The user should have a limited number of guesses before the game ends.

```
def hangman():
  
  # 1. Create a wordbank using a list of strings
  wordbank = []

  # 2. Randomly select a word from the wordbank for each new game.
  # Look up "list methods" to see how to randomly select an item from a list
  word = ...


  # 3. Ask the user to guess a letter.
  # Look up how to get an input from a user
  user_guess = ...


  # 4. Check to see if the letter is in the word
  # Look up string methods
  is_correct = ...
  
```