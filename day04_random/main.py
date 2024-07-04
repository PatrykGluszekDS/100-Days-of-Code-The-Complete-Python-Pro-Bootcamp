import random
import my_module

# random_integer = random.randint(1, 10)
# print(random_integer)
#
# print(my_module.pi)
#
# random_float = 5 * random.random()
# print(random_float)

states_of_america = ["Delaware", "Pennsylvania", "Ohio"]
print(states_of_america[0])
print(states_of_america[-1])

states_of_america.append("Texas")
print(states_of_america)

states_of_america.extend(["Washington", "Alaska"])
print(states_of_america)

print(len(states_of_america))
# print(states_of_america[6])

fruits = ["apple", "pineapple"]
vegetables = ["carrot", "potato"]
food = [fruits, vegetables]
print(food)
