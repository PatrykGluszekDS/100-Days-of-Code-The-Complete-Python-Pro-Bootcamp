import pandas

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
# for key, value in student_dict.items():
#     print(value)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame
# for k, v in student_data_frame.items():
#     # print(k)
#     # print(v)

# Loop through rows of a data frame
for index, row in student_data_frame.iterrows():
    # print(index)
    # print(row.student)
    # print(row.score)
    if row.student == "Angela":
        print(row.score)
