def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")


# greet()
# greet()


def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


# greet_with_name("Angela")
# greet_with_name("John")


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


greet_with("Jack", "Warsaw")
greet_with(location="London", name="Eddie")
