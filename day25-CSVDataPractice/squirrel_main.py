#Import pandas and os library
import pandas
import os

#Change working directory so program can access files
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

#Isolate fur colour to determine the number of each colour squirrel
data = pandas.read_csv("2018_squirrel_data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
cinammon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinammon"])

#Create dictionary to store fur colour data
data_dict={
    "Fur Colour":["Gray", "Black", "Cinammon"],
    "Count": [grey_squirrels_count, black_squirrels_count, cinammon_squirrels_count]
}

#Turn dictionary into a dataframe
df = pandas.DataFrame(data_dict)
#Convert Data Frame to a csv
df.to_csv("squirrel_count.csv")
