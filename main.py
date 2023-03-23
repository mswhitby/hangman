import random

wordbank = [
  "apples", "banana", "orange", "mango", "pineapple", "kiwi", "strawberry",
  "watermelon", "grapes", "blueberries"
]


def hangman(remaining_guess=6):
  word = random.choice(wordbank)

  # remaining_guess = 6

  guessed_letters = ["_" for letter in word]

  # guessed_letters = []
  # for letter in word:
  #   guessed_letters.append("_")

  while True:
    print(" ".join(guessed_letters))
    print("Remaining guesses: {}".format(remaining_guess))

    guess = input("Enter a letter: ").lower()

    if guess in word:
      for i in range(len(word)):
        if word[i] == guess:
          guessed_letters[i] = guess
    else:
      remaining_guess -= 1

    if "_" not in guessed_letters:
      print("congratulations! You won The word is {}.".format(word))
      break
    elif remaining_guess == 0:
      print("Sorry, you lost. The word was {}.".format(word))
      break


hangman()