import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = list('_' * len(self.word))
        self.num_unique_letters = len(set(self.word))

        self.num_lives = num_lives
        self.word_list = word_list

        self.list_of_guesses = []

    def check_guess(self, guess):
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

    def ask_for_input(self): #removed while loop as manualy calling function anyway via play_game()
        guess = input('Guess a Letter: ')
        if not (guess.isalpha() and len(guess) == 1):
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)


def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print('\n---You Lost!---\n')
            break
        elif game.num_unique_letters > 0:
            game.ask_for_input()
        elif game.num_lives != 0 and not (game.num_unique_letters > 0):
            print('\n---Congratulations. You won the game!---\n')
            break

fruit = ['apple', 'pear', 'mango', 'tomato', 'grape']
play_game(fruit)