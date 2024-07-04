from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    final_word = ""
    for letter in text:
        if letter not in alphabet:
            final_word += letter
        else:
            old_index = alphabet.index(letter)
            if direction == "encode":
                new_index = (old_index + shift) % (len(alphabet))
            elif direction == "decode":
                new_index = old_index - shift
            final_word += alphabet[new_index]
    print(final_word)


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    next_word = input("Do you want to continue? ")
    if next_word == 'no':
        break
