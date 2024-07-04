import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for index, row in data.iterrows()}
# print(data_dict)


def generate_phonetic():
    user_word = input("Enter some word: ").upper()

    try:
        output = [data_dict[let] for let in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output)


generate_phonetic()
