
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Dictionary
word_list = ["aardvark", "baboon", "camel", "book", "cat", "country", "afghanistan","sky", "city",
             "computer"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# number of lives
lives = 6

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

is_game_over = False
while not is_game_over:
    print(display)
    guess = input("Guess a letter: ").lower()
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    # Check for number of lives
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            is_game_over = True
            print("You run out of life")
    # Check if user guessed all
    if "_" not in display:
        is_game_over = True

if is_game_over:
    print(f"The chosen word was {chosen_word}")
