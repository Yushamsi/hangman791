import random

class Hangman:
    """
    A class to represent the Hangman game.

    Attributes:
    word_list (list): List of words to choose from for the game.
    num_lives (int): Number of lives the player has.
    word (str): The word to be guessed, chosen randomly from word_list.
    word_guessed (list): List representing the current state of the guessed word.
    num_unique_letters (int): Number of unique letters in the word.
    list_of_guesses (list): List of letters that have been guessed.

    Methods:
    __init__(word_list, num_lives=5): Initialises the Hangman game with a word list and a number of lives.
    check_guess(guess): Checks if the guessed letter is in the word and updates the game state accordingly.
    ask_for_input(): Prompts the player to guess a letter and processes the guess.
    """
    def __init__(self, word_list, num_lives=5):
        """
        Initialises the Hangman game with a word list and a number of lives.

        Parameters:
        word_list (list): List of words to choose from for the game.
        num_lives (int): Number of lives the player has. Default is 5.
        """
        self.word_list = word_list
        self.num_lives = num_lives

        self.word = random.choice(self.word_list)
        self.word_guessed = list('_' * len(self.word))
        self.num_unique_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        Checks if the guessed letter is in the word and updates the game state accordingly.

        Parameters:
        guess (str): The letter guessed by the player.
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for position, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[position] = guess 
            self.num_unique_letters -= 1
            print(self.word_guessed)
        else: 
            print(f"Sorry, {guess} is not in the word. Try again")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """
        Prompts the player to guess a letter and processes the guess.
        """
        guess = input('Guess a Letter: ') 
        if not (guess.isalpha() and len(guess) == 1): 
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)


def play_game(word_list):
    game = Hangman(word_list)
    while True:
        if game.num_lives == 0:
            print('\n---You Lost!---\n')
            break
        elif game.num_unique_letters > 0:
            game.ask_for_input()
        else:
            print('\n---Congratulations. You won the game!---\n')
            break

fruit = ['apple', 'pear', 'mango', 'tomato', 'grape'] 
play_game(fruit)

### Future Improvements:
### Scale it to make it more advanced - multiple characters when guessing
### More Words in List
### Limit to how many guesses
### tqdm status bar