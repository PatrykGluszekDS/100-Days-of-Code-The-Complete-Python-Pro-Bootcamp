import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = len(data[data["Primary Fur Color"] == 'Gray'])
cinnamon = len(data[data["Primary Fur Color"] == 'Cinnamon'])
black = len(data[data["Primary Fur Color"] == 'Black'])

color_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [gray, cinnamon, black]
}
color_data = pandas.DataFrame(color_dict)
color_data.to_csv("squirrel_count.csv")
