# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("../../my_file.txt", mode="r") as file:  # modes: a, r, w
    content = file.read()
    print(content)
