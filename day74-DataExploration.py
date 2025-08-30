#Data Exploration
#Ashlynn Ward, August 28, 2025
#This program was copied from my Google Colab notebook. It shows the practice I did to learn how to explore data using Pandas.

import pandas as pd

df = pd.read_csv('/salaries_by_college_major.csv')

df.head()

df.shape

df.columns

df.isna()

df.tail()

clean_df=df.dropna()

clean_df.tail()

clean_df['Starting Median Salary']

clean_df['Starting Median Salary'].max()

clean_df['Starting Median Salary'].idxmax()

clean_df['Undergraduate Major'].loc[43]

clean_df['Mid-Career Median Salary'].idxmax()

clean_df['Undergraduate Major'].loc[8]

clean_df["Mid-Career Median Salary"].max()

clean_df["Starting Median Salary"].idxmin()

clean_df["Undergraduate Major"].loc[49]

clean_df["Starting Median Salary"].min()

clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']

spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
clean_df.head()

clean_df.sort_values("Mid-Career 90th Percentile Salary", ascending=False)

clean_df.groupby('Group').count()

clean_df.groupby("Group").mean()

