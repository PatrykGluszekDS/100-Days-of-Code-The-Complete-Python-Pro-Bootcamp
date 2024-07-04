print("Welcome to Treasure Island.\nYour mission is to find the treasure")
choice1 = input("left or right?: ").lower()
if choice1 == 'left':
    choice2 = input("swim or wait? ").lower()
    if choice2 == 'wait':
        choice3 = input("Which door? ").lower()
        if choice3 == 'red':
            print("Burned by fire/\nGame Over")
        elif choice3 == 'yellow':
            print("You win!")
        elif choice3 == "blue":
            print("Eaten by beasts.\nGame Over.")
        else:
            print("Game Over")
    else:
        print("Attacked by trout.\nGame Over")
else:
    print("Fall into a hole.\nGame Over.")