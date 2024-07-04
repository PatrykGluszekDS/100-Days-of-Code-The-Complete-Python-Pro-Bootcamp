import random
from art import logo

print(logo)
number = random.randint(1, 100)
print(f"Test {number}")
print("I think of a number between 1 and 100")

level = input("What level do you want to play? (easy/hard): ")
if level == 'easy':
    lives = 10
else:
    lives = 5

while True:
    guess = int(input("Guess a number: "))
    if guess == number:
        print("You guessed correctly! You won!")
        break
    elif guess < number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
    lives -= 1
    if lives == 0:
        print("You have 0 lives/life! You lost!")
        break
    print(f"You have {lives} lives, try again")
