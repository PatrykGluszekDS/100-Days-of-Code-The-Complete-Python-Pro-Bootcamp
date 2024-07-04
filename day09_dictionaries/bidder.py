from art import logo

print(logo)

bid_dictionary = {}

while True:
    name = input("What is your name? ")
    bid_price = int(input("What is your bid price? $"))
    bid_dictionary[name] = bid_price

    other = input("Are there other users who want to bid? ")
    print('\n\n')
    if other == 'no':
        break

winner_price = 0
winner = ""

for k, v in bid_dictionary.items():
    if v > winner_price:
        winner_price = v
        winner = k

print(f"The winner is {winner}")
