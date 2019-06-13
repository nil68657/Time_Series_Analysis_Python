# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 18:03:18 2019

@author: nchatter
"""

# Import pandas and plotting modules
import pandas as pd
import matplotlib.pyplot as plt

##############################   Import the Google Trend data for the word "diet" in a datframe   ###############################
diet = pd.read_csv("diet.csv",skiprows=2)
diet= diet.rename(index=str, columns={"Week": "Week", "diet: (United States)": "Score"})
#print(diet.head(5))
#################    Convert the date index to datetime. DateTime helps index the rows usnig 'Date' #############################
diet.datetime = pd.to_datetime(diet.Week)

diet.plot(grid=True)
plt.show()

# From previous step
diet.index = pd.to_datetime(diet.datetime)
#print(diet.index )

# Slice the dataset to keep only 2015
diet2015=diet['2015']

# Plot 2012 data
diet2015.plot(grid=True)
plt.show()

######################################################################################################################################

bonds= pd.read_csv("bonds.csv")
stocks= pd.read_csv("stocks.csv")
bonds.datetime = pd.to_datetime(bonds.DATE)
stocks.datetime = pd.to_datetime(stocks.DATE)

# Convert the stock index and bond index into sets
set_stock_dates = set(stocks.index)
set_bond_dates = set(bonds.index)

# Take the difference between the sets and print
#print(set_stock_dates - set_bond_dates)

# Merge stocks and bonds DataFrames using join()
#stocks_and_bonds = pd.merge(bonds,stocks,how='inner',on='DATE')
stocks_and_bonds = stocks.join(bonds,how='inner',lsuffix='_stocks', rsuffix='_bonds')
stocks_and_bonds = stocks_and_bonds.drop("DATE_bonds",axis=1)
#stocks_and_bonds = pd.merge(stocks,bonds,how='inner',on='DATE')
print(stocks_and_bonds)

# Compute percent change using pct_change()
returns = stocks_and_bonds.pct_change(fill_method='ffill',axis=1)
print(returns.head(5))
# Compute correlation using corr()
correlation = returns['SP500'].corr(returns['US10Y'])
print("Correlation of stocks and interest rates: ", correlation)

# Make scatter plot
plt.scatter(returns['SP500'],returns['US10Y'])
plt.show()