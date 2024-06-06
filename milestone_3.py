secret_word = 'apple'

def check_guess(guess):
    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.")
    else: 
        print(f"Sorry, {guess} is not in the word. Try again")

def ask_for_input():
    while True:
        guess = input('Guess a Letter: ')
        guess = guess.lower()
        if guess.isalpha() and len(guess) == 1:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

    check_guess(guess)


ask_for_input()

