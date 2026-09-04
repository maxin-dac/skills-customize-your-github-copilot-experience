
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a playable Hangman game in Python. Practice string manipulation, loops, conditionals, user input, and random selection while managing the state of a game.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description

Prepare the data and variables needed to start a Hangman game. Use the word list provided in `starter-code.py` and select one word at random.

#### Requirements

Completed program should:

- Randomly select one secret word from the predefined list.
- Create a collection to track the letters guessed by the player.
- Set a maximum number of incorrect guesses and track the remaining attempts.

### 🛠️ Implement the Game Loop

#### Description

Create the main game loop so the player can guess letters and reveal the secret word before running out of attempts.

#### Requirements

Completed program should:

- Display the current progress with unguessed letters hidden, such as `_ _ _ _`.
- Ask the player for a letter and update the guessed letters.
- Reduce the remaining attempts when the player guesses an incorrect letter.
- End when the player guesses the complete word or has no attempts left.
- Display a clear win message or lose message at the end of the game.
