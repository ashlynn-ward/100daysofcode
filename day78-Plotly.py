#Plotly Practice
#Ashlynn Ward, September 2, 2025
#This program was copied from Google Colab Notebooks. It shows my practice using Plotly instead of matplotlib to create graphs.

# Import Statements

import pandas as pd
import plotly.express as px

# Notebook Presentation

# Show numeric output in decimal format e.g., 2.15
pd.options.display.float_format = '{:,.2f}'.format

# Read the Dataset

df_apps = pd.read_csv('apps.csv')

# Data Cleaning


df_apps.shape

df_apps.columns

df_apps.sample(5)

### Drop Unused Columns


df_apps.drop(columns=['Last_Updated', 'Android_Ver'], inplace=True)

### Find and Remove NaN values in Ratings


nan_rows = df_apps[df_apps['Rating'].isna()]

df_apps_clean = df_apps.dropna()

### Find and Remove Duplicates



df_apps_clean.duplicated().sum()

df_apps_clean.drop_duplicates(inplace=True)

df_apps_clean.shape

# Find Highest Rated Apps


df_apps_clean.sort_values(by='Rating', ascending=False).head(10)

# Find 5 Largest Apps in terms of Size (MBs)


df_apps_clean.sort_values(by='Size_MBs', ascending=False).head(10)

# Find the 5 App with Most Reviews


df_apps_clean.sort_values(by='Reviews', ascending=False).head(50)

# Plotly Pie and Donut Charts - Visualise Categorical Data: Content Ratings

ratings = df_apps_clean.Content_Rating.value_counts()
ratings

fig = px.pie(labels=ratings.index, values=ratings.values, names=ratings.index)
fig.show()

fig = px.pie(labels=ratings.index,
values=ratings.values,
title="Content Rating",
names=ratings.index,
)
fig.update_traces(textposition='outside', textinfo='percent+label', hole = 0.5)
 
fig.show()

# Numeric Type Conversion: Examine the Number of Installs

df_apps_clean.Installs.describe()

df_apps_clean.Installs = df_apps_clean.Installs.astype(str).str.replace(',', "")
df_apps_clean.Installs = pd.to_numeric(df_apps_clean.Installs)
df_apps_clean[['App', 'Installs']].groupby('Installs').count()


df_apps_clean.Price = df_apps_clean.Price.astype(str).str.replace('$', "")
df_apps_clean.Price = pd.to_numeric(df_apps_clean.Price)
 
df_apps_clean.sort_values('Price', ascending=False).head(20)

df_apps_clean = df_apps_clean[df_apps_clean['Price'] < 250]
df_apps_clean.sort_values('Price', ascending=False).head(5)

# Find the Most Expensive Apps, Filter out the Junk, and Calculate a (ballpark) Sales Revenue Estimate


df_apps_clean['Revenue_Estimate'] = df_apps_clean.Installs.mul(df_apps_clean.Price)
df_apps_clean.sort_values('Revenue_Estimate', ascending=False)[:10]

### The most expensive apps sub $250



### Highest Grossing Paid Apps (ballpark estimate)



# Plotly Bar Charts & Scatter Plots: Analysing App Categories

df_apps_clean.Category.nunique()

top10_category = df_apps_clean.Category.value_counts()[:10]

bar = px.bar(x = top10_category.index, # index = category name
             y = top10_category.values)
 
bar.show()


### Vertical Bar Chart - Highest Competition (Number of Apps)

category_installs = df_apps_clean.groupby('Category').agg({'Installs': pd.Series.sum})
category_installs.sort_values('Installs', ascending=True, inplace=True)

### Horizontal Bar Chart - Most Popular Categories (Highest Downloads)

h_bar = px.bar(x = category_installs.Installs,
               y = category_installs.index,
               orientation='h',
               title='Category Popularity')
 
h_bar.update_layout(xaxis_title='Number of Downloads', yaxis_title='Category')
h_bar.show()



### Category Concentration - Downloads vs. Competition

cat_number = df_apps_clean.groupby('Category').agg({'App': pd.Series.count})

cat_merged_df = pd.merge(cat_number, category_installs, on='Category', how="inner")
print(f'The dimensions of the DataFrame are: {cat_merged_df.shape}')
cat_merged_df.sort_values('Installs', ascending=False)

scatter = px.scatter(cat_merged_df, # data
                    x='App', # column name
                    y='Installs',
                    title='Category Concentration',
                    size='App',
                    hover_name=cat_merged_df.index,
                    color='Installs')
 
scatter.update_layout(xaxis_title="Number of Apps (Lower=More Concentrated)",
                      yaxis_title="Installs",
                      yaxis=dict(type='log'))
 
scatter.show()

# Extracting Nested Data from a Column


# Split the strings on the semi-colon and then .stack them.
stack = df_apps_clean.Genres.str.split(';', expand=True).stack()
print(f'We now have a single column with shape: {stack.shape}')
num_genres = stack.value_counts()
print(f'Number of genres: {len(num_genres)}')

bar = px.bar(x = num_genres.index[:15], # index = category name
             y = num_genres.values[:15], # count
             title='Top Genres',
             hover_name=num_genres.index[:15],
             color=num_genres.values[:15],
             color_continuous_scale='Agsunset')
 
bar.update_layout(xaxis_title='Genre',
yaxis_title='Number of Apps',
coloraxis_showscale=False)
 
bar.show()


# Grouped Bar Charts: Free vs. Paid Apps per Category

df_apps_clean.Type.value_counts()


df_free_vs_paid = df_apps_clean.groupby(["Category", "Type"], as_index=False).agg({'App': pd.Series.count})
df_free_vs_paid.head()

g_bar = px.bar(df_free_vs_paid,
               x='Category',
               y='App',
               title='Free vs Paid Apps by Category',
               color='Type',
               barmode='group')
 
g_bar.update_layout(xaxis_title='Category',
                    yaxis_title='Number of Apps',
                    xaxis={'categoryorder':'total descending'},
                    yaxis=dict(type='log'))
 
g_bar.show()


# Plotly Box Plots: Revenue by App Category

df_paid_apps = df_apps_clean[df_apps_clean['Type'] == 'Paid']
box = px.box(df_paid_apps, 
             x='Category', 
             y='Revenue_Estimate',
             title='How Much Can Paid Apps Earn?')
 
box.update_layout(xaxis_title='Category',
                  yaxis_title='Paid App Ballpark Revenue',
                  xaxis={'categoryorder':'min ascending'},
                  yaxis=dict(type='log'))
 
 
box.show()

# How Much Can You Charge? Examine Paid App Pricing Strategies by Category

df_paid_apps.Price.median()


box = px.box(df_paid_apps,
             x='Category',
             y="Price",
             title='Price per Category')
 
box.update_layout(xaxis_title='Category',
                  yaxis_title='Paid App Price',
                  xaxis={'categoryorder':'max descending'},
                  yaxis=dict(type='log'))
 
box.show()


