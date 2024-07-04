import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card(user, number):
    for _ in range(number):
        card = random.choice(cards)
        user.append(card)


def replacing_ace(user):
    if sum(user) > 21:
        for card in user:
            index = 0
            if card == 11:
                del user[index]
                user.insert(index, 1)
            index += 1
        print(user)


def check_win(user1, user2):
    pass


print(logo)
while True:
    play = input("Do you want to play blackjack? (yes/no): ")
    if play == 'no':
        break

    user_cards = []
    dealer_cards = []
    deal_card(user_cards, 2)
    deal_card(dealer_cards, 2)

    print(user_cards)
    print(dealer_cards)

    if sum(dealer_cards) == 21:
        print("Dealer has blackjack! You lost")
        continue
    elif sum(user_cards) == 21:
        print("You have blackjack! You won")
        continue

    replacing_ace(user_cards)
    replacing_ace(dealer_cards)

    print(f"Computer first card: {dealer_cards[0]}")
    print(f"Your cards: {user_cards}")

    while True:
        another_card = input("Do you want another card? (Type yes/no): ")
        if another_card == 'no':
            check_win()
            break
        deal_card(user_cards, 1)
        if sum(user_cards) > 21:
            print("You lost! (Sum over 21)")
            break
