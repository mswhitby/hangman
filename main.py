# import the module "random"
import random

def hangman():


   
  # 1. Create a wordbank using a list of strings
  wordbank = [
    'hello', 'how', 'is', 'your', 'money',
  ]

  # 2. Randomly select a word from the wordbank for each new game.
  # Look up "list methods" to see how to randomly select an item from a list  
  word = random.choice(wordbank)
  
  # 3. Set the number of guesses
  limit = 5
  
  # 4. Create a variable to store correct guesses
  correct_letters = []
  for letter in word:
    correct_letters.append('_')


  # 5. Create a loop to check user guesses          
  while True:
   
    # 6. Ask the user to guess a letter.
    # Look up how to get an input from a user
    user_guess = input(f"guess the letters in the {correct_letters}, you have {limit} guesses") 

    # 7. Check to see if the letter is in the word
    # Look up string 
    if user_guess in word:
      for i in range(len(word)):
        letter = word[i]
        if letter == user_guess:
          correct_letters[i] = letter
      print(f"The letter {user_guess} is in the word {correct_letters}")

    else:
      limit = limit - 1 
      print(f"if guess incorrect {user_guess} not in the word {correct_letters}")




hangman()

  