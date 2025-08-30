#Creating Graphs
#Ashlynn Ward, August 29, 2025
#This program was copied from my Google Colab notebook. It shows my practice with pivoting tables and using matplotlib to create
#graphs.

## Import Statements

import matplotlib.pyplot as plt

import pandas as pd
df = pd.read_csv('/QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

## Data Exploration
df.head()
df.tail()

df.columns

df.shape

df.shape

df.count()

df.groupby("TAG").sum()

df.groupby("TAG").count()

## Data Cleaning

df['DATE'][1]

df.DATE[1]

df.DATE = pd.to_datetime(df.DATE)

df.head()

## Data Manipulation



pivoted_df = df.pivot(index="DATE", columns="TAG", values="POSTS")
pivoted_df.head()

pivoted_df.shape

pivoted_df.columns

pivoted_df.head()

pivoted_df.fillna(0, inplace=True)

## Data Visualisaton with with Matplotlib

plt.plot(pivoted_df.index, pivoted_df.java)

for column in pivoted_df.columns:
    plt.plot(pivoted_df.index, pivoted_df[column])

# Smoothing out Time Series Data

roll_df = pivoted_df.rolling(window=6).mean()

plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column],
             linewidth=3, label=roll_df[column].name)

plt.legend(fontsize=16)

