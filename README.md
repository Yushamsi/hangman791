# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Files
- Hangman.py: Hangman Class and 'play_game' Function to run game successfully. The game randomly selects a word from a predefined list, the user has to guess the characters in of the word one by one, for each incorrect guess the user loses a life (default 5 lives). If the user guesses all the correct characters to the word and has >= 1 life then they Win.

### Hangman.py Classes and Functions

- Hangman Class has three methods: 

    1. '__init__' - this constructer randomly selects a word from the input list ('word_list') and sets the number of lives ('num_lives') to 5 by default. It also creates a list of '_''s of the length of characters found in the word. This list is called 'word_guessed'.
    2. 'ask_for_input' - this method prompts the player for an input and checks this input is alphabetical and a single character.
    3. 'check_guess' - this method checks that the user input charcter is in the word, if it is the 'word_guessed' list is filled in with the corresponding character. If the user input isn't in the word then a life is deducted. 

- 'play_game' Function: takes in the 'word_list' and runs the 'Hangman' class if the number of letters left to guess and number of lives is > 0 . It determines whether the user has won or lost by checking the 'num_lives' variable and the number of unique characters left to guess.



## Installation & Usage
Requires base level Python 3 (=< 3.8) and Python dependencies.

## Licence
MIT Licence:
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)