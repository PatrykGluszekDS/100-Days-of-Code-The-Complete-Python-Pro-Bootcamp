import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in chosen_word:
    display.append('_')
guess = input("Guess a letter: ").lower()

count = 0
for letter in chosen_word:
    if letter == guess:
        display[count] = letter
    count += 1


print(display)
