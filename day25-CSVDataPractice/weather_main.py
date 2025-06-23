#Import csv, pandas, and os libraries
import csv
import pandas
import os

#Change working directory so program can access files
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

#Open and read the weather data
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    #Print each item
    for row in data:
        print(row)
    #Store temperatures without the heading
    temperatures = []
    for row in data:
        if row[1]!="temp":
            temperatures.append(int(row[1]))
    print(temperatures)

#Read weather data using pandas and print it
data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])

#Turn data into a dictionary
data_dict = data.to_dict()

#Turn temps into a list
temp_list = data["temp"].to_list()

#Calculate average temp
average = sum(temp_list)/len(temp_list)
average_temp = data["temp"].mean()

#Find max temp
max_temp = data["temp"].max()
#You can also use data.temp 
max_temp = data.temp.max()

#Get data in a row
data[data.day == "Monday"]

#Find the row of data with the highest temp
print(data[data.temp == data.temp.max()])

#Convert Monday's temp into F
monday = data[data.day == "Monday"]
monday_temp = monday.temp*9/5+32

#Create a data frame from scratch