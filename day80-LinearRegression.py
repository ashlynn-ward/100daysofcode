#Linear Regression Practice
#Ashlynn Ward, September 4, 2025
#This program was copied from a Google Colab Notebook. It is the practice I completed when learning about linear regressions.

# Import Statements

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Notebook Presentation

pd.options.display.float_format = '{:,.2f}'.format

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Read the Data

data = pd.read_csv('cost_revenue_dirty.csv')

# Explore and Clean the Data

data.shape
data.isna()
data.duplicated()
data.dtypes

data.head()

### Data Type Conversions

data["USD_Production_Budget"] = data["USD_Production_Budget"].str.replace(",","")
data["USD_Production_Budget"] = pd.to_numeric(data["USD_Production_Budget"])
data["USD_Worldwide_Gross"] = data["USD_Worldwide_Gross"].str.replace("$","")
data["USD_Worldwide_Gross"] = data["USD_Worldwide_Gross"].str.replace(",","")
data["USD_Worldwide_Gross"] = pd.to_numeric(data["USD_Worldwide_Gross"])
data["USD_Domestic_Gross"] = data["USD_Domestic_Gross"].str.replace("$","")
data["USD_Domestic_Gross"] = data["USD_Domestic_Gross"].str.replace(",","")
data["USD_Domestic_Gross"] = pd.to_numeric(data["USD_Domestic_Gross"])
data.head()

data.dtypes

data["Release_Date"] = pd.to_datetime(data["Release_Date"])

### Descriptive Statistics
data.describe()

# Investigating the Zero Revenue Films

zero_domestic = data[data["USD_Domestic_Gross"] == 0]
zero_domestic.shape
zero_domestic.sort_values(by="USD_Production_Budget", ascending=False)

zero_worldwide = data[data.USD_Worldwide_Gross == 0]
print(f'Number of films that grossed $0 worldwide {len(zero_worldwide)}')
zero_worldwide.sort_values('USD_Production_Budget', ascending=False)

### Filtering on Multiple Conditions

international_releases = data.loc[(data.USD_Domestic_Gross == 0) & 
                                  (data.USD_Worldwide_Gross != 0)]

international_releases=data.query("USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0")
international_releases.head()

### Unreleased Films

# Date of Data Collection
scrape_date = pd.Timestamp('2018-5-1')

unreleased_films = data[data.Release_Date >= scrape_date]
data_clean = data.drop(unreleased_films.index)

### Films that Lost Money

lost_money = data[data.USD_Production_Budget > data.USD_Worldwide_Gross]
lost_percent = (len(lost_money)/len(data))*100
print(lost_percent)

# Seaborn for Data Viz: Bubble Charts

sns.scatterplot(data=data_clean,
                x='USD_Production_Budget', 
                y='USD_Worldwide_Gross')

plt.figure(figsize=(8,4), dpi=200)
 
ax = sns.scatterplot(data=data_clean,
                     x='USD_Production_Budget', 
                     y='USD_Worldwide_Gross')
 
ax.set(ylim=(0, 3000000000),
       xlim=(0, 450000000),
       ylabel='Revenue in $ billions',
       xlabel='Budget in $100 millions')
 
plt.show()

### Plotting Movie Releases over Time

plt.figure(figsize=(8,4), dpi=200)
ax = sns.scatterplot(data=data_clean,
                     x='USD_Production_Budget', 
                     y='USD_Worldwide_Gross',
                     hue='USD_Worldwide_Gross', # colour
                     size='USD_Worldwide_Gross',) # dot size
 
ax.set(ylim=(0, 3000000000),
       xlim=(0, 450000000),
       ylabel='Revenue in $ billions',
       xlabel='Budget in $100 millions',)
 
plt.show()

plt.figure(figsize=(8,4), dpi=200)
 
with sns.axes_style("darkgrid"):
    ax = sns.scatterplot(data=data_clean, 
                    x='Release_Date', 
                    y='USD_Production_Budget',
                    hue='USD_Worldwide_Gross',
                    size='USD_Worldwide_Gross',)
 
    ax.set(ylim=(0, 450000000),
           xlim=(data_clean.Release_Date.min(), data_clean.Release_Date.max()),
           xlabel='Year',
           ylabel='Budget in $100 millions')

# Converting Years to Decades Trick

dt_index = pd.DatetimeIndex(data_clean.Release_Date)
years = dt_index.year
decades = years//10*10
data_clean['Decade'] = decades

### Separate the "old" (before 1969) and "New" (1970s onwards) Films

old_films = data_clean[data_clean.Decade <= 1960]
new_films = data_clean[data_clean.Decade > 1960]

# Seaborn Regression Plots

sns.regplot(data=old_films, 
            x='USD_Production_Budget',
            y='USD_Worldwide_Gross')

plt.figure(figsize=(8,4), dpi=200)
with sns.axes_style('darkgrid'):
  ax = sns.regplot(data=new_films,
                   x='USD_Production_Budget',
                   y='USD_Worldwide_Gross',
                   color='#2f4b7c',
                   scatter_kws = {'alpha': 0.3},
                   line_kws = {'color': '#ff7c43'})
  
  ax.set(ylim=(0, 3000000000),
         xlim=(0, 450000000),
         ylabel='Revenue in $ billions',
         xlabel='Budget in $100 millions') 

# Run Your Own Regression with scikit-learn
regression = LinearRegression()

# Explanatory Variable(s) or Feature(s)
X = pd.DataFrame(new_films, columns=['USD_Production_Budget'])
 
# Response Variable or Target
y = pd.DataFrame(new_films, columns=['USD_Worldwide_Gross']) 

regression.fit(X, y)