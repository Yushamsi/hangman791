import random

fruit_list = ['banana', 'apple', 'melon', 'grapes', 'tomato']
print(fruit_list)

random_word = random.choice(word_list)
print(random_word)

guessed_letter = input('Enter a single letter:')

if len(guessed_letter) == 1 and guessed_letter.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

