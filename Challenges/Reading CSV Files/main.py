import csv
import pandas

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
    #print(temperatures)

data = pandas.read_csv("weather_data.csv")
# print(data["temp"].max())
#
# #get data in columns
# print(data["condition"])
# print(data.condition)

# get data in rows
# monday = data[data.day == "Monday"]
# temp_c = data[data.day == "Monday"].temp
# temp_f = temp_c*(9/5)+32
# print(temp_f)

# create dataframe from scratch
data_dict = {
    "students":["Any", "James", "Angela"],
    "scores": [76, 56, 65]
}
data= pandas.Dataframe(data_dict)
data.to_csv("new_data.csv")