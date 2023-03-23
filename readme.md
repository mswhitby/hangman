[Open on Replit](https://replit.com/@whs-spring-2023/Hangman-Tips-whs-spring-2023-3)


# Hangman (due 3/24/23)

Create a program that simulates a game of Hangman. The program should randomly select a word from a list and then prompt the user to guess letters in the word. The user should have a limited number of guesses before the game ends.

```
import random

def hangman():

  # 1. Create a wordbank using a last of strings
  wordbank = ["toy", "nachos", "tacos", "chimichangas", "burritos", "enchiladas", "cheese", "guacamole", "bread", "salsa", "football", "school", "coding", "footnite", "potatos", "fries", "pizza", "waltuh", "extravagant", "Sasageyo", "wenomechainsama", "tumajarbisaun", "baller", "holler", "honors", "farded"]

  # 2. Randomly select a target word from the last for each new game.
  # Hint use random.choice() from the random module
  word = random.choice(wordbank)
  
  # 2.5 Create a list to track which letters the user has guessed correctly
  correct_letters = []
  for letter in word:
    correct_letters.append("_")

  remaining_guesses = 10

  while True:
    # 3. Ask the user to guess a letter
    # Hint: You'll need to use input()
    user_guess = input(f"""
    Guess a letter for the word {''.join(correct_letters)}, {remaining_guesses} guesses left
    """).lower()
  
    # 4. Check if the letter is in the word
    if user_guess in word:

      # 6. Create rules for if the letter is in the word
      for letter in range(len(word)):
        if word[letter] == user_guess:
          correct_letters[letter] = user_guess
    
          
    # 6. Create rules for of the letter as not on the word
    else:
     remaining_guesses = remaining_guesses - 1 
      
    # When should the loop stop?
    if not "_" in correct_letters:
      print(f"You have guessed the letters in {word} correctly, you win")
      break
      
    if remaining_guesses == 0:
      print(f"you were not able to guess the letters in {word}, please try again")
      break
      

hangman()




    

  ```