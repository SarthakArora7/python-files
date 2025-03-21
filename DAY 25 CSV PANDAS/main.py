# import csv
#
# with open("weather-data.csv") as weather:
#     data = csv.reader(weather)
#     temperatures = []
#     for row in data:
#         if row[1] == "temp":
#             pass
#         else:
#             temperatures.append(int(row[1]))
# print(temperatures)

import pandas

data = pandas.read_csv("weather-data.csv")
print(data["temp"])

# temp_list = data["temp"].tolist()
# print(temp_list)
#
# print(data["temp"].mean())
#
# print(data["temp"].max())

# Get the row from the weather-data file where temp is maximum
# print(data[data.temp == data.temp.max()])

# Get Monday's temperature in Fahrenheit
# monday = data[data.day == "Monday"]
# print(monday)
# monday_temp_fahr = monday.temp*9/5 + 32
# print(monday_temp_fahr)
#

# squirrel = pandas.read_csv("Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# gray_squirrel_count = len(squirrel[squirrel["Primary Fur Color"] == "Gray"])
# cinnamon_squirrel_count = len(squirrel[squirrel["Primary Fur Color"] == "Cinnamon"])
# black_squirrel_count = len(squirrel[squirrel["Primary Fur Color"] == "Black"])
#
# squirrel_dict = {"Color": ("Gray", "Cinnamon", "Black"),
#                  "Count": (gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count)}
#
# squirrel_table = pandas.DataFrame(squirrel_dict)
# squirrel_table.to_csv("Squirrel_table.csv")
