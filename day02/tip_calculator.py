print("Welcome to the tip calculator!")
total = float(input("What was the total bill?: "))
tip_amount = float(input("How much tip would you like to give? (%): "))
people = int(input("How many people there was?: "))

amount = (total/people)*(1.0+(tip_amount/100))

print(f"Each person should pay: {round(amount, 2)}$")
