from art import logo, vs
from game_data import data
import random

print(logo)
first_guy = random.choice(data)
score = 0

while True:
    second_choice = random.choice(data)
    if first_guy == second_choice:
        continue

    print(f"Compare {first_guy['name']}, {first_guy['description']} from {first_guy['country']} with "
          f"{first_guy['follower_count']} followers ")
    print(vs)
    print(f"{second_choice['name']}, {second_choice['description']} from {second_choice['country']}")
    answer = input("Choose A/B: ")

    first_followers = first_guy['follower_count']
    second_followers = second_choice['follower_count']

    if (answer == 'A' and first_followers > second_followers) or (answer == 'B' and second_followers > first_followers):
        score += 1
        print("You are right!")
        print(f"Current score: {score}\n")
        first_guy = second_choice
    else:
        print(f"You are wrong! Number of {second_choice['name']} followers - {second_followers}")
        print(f"Final score - {score}")
        break
