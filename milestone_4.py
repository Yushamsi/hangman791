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
        else: 
            print(f"Sorry, {guess} is not in the word. Try again")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input('Guess a Letter: ')
            if not (guess.isalpha() and len(guess) == 1):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

fruit = ['apple']

test = Hangman(fruit)
test.ask_for_input()