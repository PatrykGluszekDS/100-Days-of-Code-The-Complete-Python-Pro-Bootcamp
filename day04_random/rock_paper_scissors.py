import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

random_choice = random.randint(1, 3)
your_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors: "))

if your_choice == 0:
    print(rock)
elif your_choice == 1:
    print(paper)
else:
    print(scissors)

print("Computer chose:")
if random_choice == 0:
    print(rock)
if random_choice == 1:
    print(paper)
else:
    print(scissors)

if random_choice == your_choice:
    print("Draw")
elif (your_choice == 0 and random_choice == 2) or (your_choice == 1 and random_choice == 0) or (your_choice == 2 and random_choice == 1):
    print("You won")
else:
    print("You lose")