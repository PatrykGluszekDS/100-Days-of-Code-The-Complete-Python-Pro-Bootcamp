# with open("weather_data.csv") as file:
#     data = file.read().splitlines()
#
# print(data)


# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")

print(data)
# print(data["temp"])
# print(type(data))

data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
# print(temp_list)

# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)
# print(data["temp"].mean())
# print(data["temp"].max())

# Get data in columns
# print(data["condition"])
# print(data.condition)

# Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp = monday.temp
print(monday_temp)

f_temp = (monday_temp * 1.8) + 32
print(f_temp)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data2 = pandas.DataFrame(data_dict)
print(data2)
data2.to_csv("new_data.csv")
