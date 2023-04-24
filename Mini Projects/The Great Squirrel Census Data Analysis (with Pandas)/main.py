import csv
import pandas


# ,Fur Color,count
# 0,Black,103
# 1,Red,392
# 2,Gray,2473


data = pandas.read_csv("C:/Users/sesay/OneDrive/Desktop/Python-Projects/Mini Projects/The Great Squirrel Census Data Analysis (with Pandas)/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

black = data["Primary Fur Color"=="Black"]
red = data["Primary Fur Color"=="Red"]
gray = data["Primary Fur Color"=="Gray"]
black_count = black.count()
red_count = red.count()

print(red_count)