#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 08:05:02 2025

@author: anneyece isabel castro ramos and yolina bakhos
"""

# Part 3 – Understanding and preparing the data

#2.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

World_Demographic_Indicators = pd.read_csv("wdi_wide.csv")

#3. For instance, use the function info() to list the size of the dataset and its data types.
#how many empty values for the column “Physicians” and “Population”?

print(" ")
print("Information about the data:")
print(" ")
World_Demographic_Indicators.info()

# “Physicians” = 10 null
# “Population” = 0 null

#4. Use the nunique() function to print the number of unique values for each column.

print(" ")
print(" ")
print("Unique values for each column:")
print(" ")
print(World_Demographic_Indicators.nunique())

# 5. Use the describe() function to print further information about your data. What exactly does the output of this function provide?

print(" ")
print(" ")
print("Description of data:")
print(" ")
print(World_Demographic_Indicators.describe())

#5. Gross National Income (GNI) is an absolute value. It's more appropriate to
# use GNI per capita to answer some questions. Add a new column called “GNI per
# capita” to your dataset with data containing GNI by population. Then use the
# function round() to round it to the nearest cent.

World_Demographic_Indicators['GNI per capita'] = round(World_Demographic_Indicators["GNI"] / World_Demographic_Indicators["Population"], 2)

#7. Using the value_counts() function, print the answer for the following questions:
# a) How many countries are there in each region?
print(World_Demographic_Indicators.value_counts("Region"))
  
# b) How many hight income economies are there?

print(World_Demographic_Indicators.value_counts("High Income Economy"))

# 8. Using the pd.crosstab() function, print the answer for the question “Where are the high income economies?”. Per region, and including Yes and No.

print(pd.crosstab(World_Demographic_Indicators["High Income Economy"],World_Demographic_Indicators["Region"]))

# 9. You might need to filter some data from your dataset. Often it can be made without using a loop. For example, the syntax to get only rows with values > 10 in a given column would be:

    # filtered_data = data[data[“Your Column”] > 10]
    
#Can you tell me how many countries there are where women can expect to live for more than 80 years? And which countries those are?

life_expectancy_more_80_female = World_Demographic_Indicators[World_Demographic_Indicators["Life expectancy, female"] > 80]

print(" ")
print(" ")
print("Countries where women can expect to live for more than 80 years:")
print(" ")

for i in life_expectancy_more_80_female["Country Name"]:
    print(i)

# =============================================================================
# 
# =============================================================================

# Part 4 - Visualizing statistical relationships

#1. Is there any association between GNI per capita and life expectancy?” (one plot for each gender)

#female
sns.relplot(World_Demographic_Indicators, x="Life expectancy, female", y="GNI per capita")
#male
sns.relplot(World_Demographic_Indicators, x="Life expectancy, male", y="GNI per capita")

plt.show()

#2. By adding a third “feature” to your plot using colors to represent it in
# order to answer the following question: “Does the association between GNI per
# capita and life expectancy vary by region?” (one plot for each gender)

#female
sns.relplot(World_Demographic_Indicators, x="Life expectancy, female", y="GNI per capita", hue="Region")
#male
sns.relplot(World_Demographic_Indicators, x="Life expectancy, male", y="GNI per capita", hue="Region")

plt.show()

#3. Generate a the plot from item 2, now using lines along with standard deviation.

#female
sns.lineplot(World_Demographic_Indicators, x="Life expectancy, female", y="GNI per capita", errorbar="sd")
plt.show()
#male
sns.lineplot(World_Demographic_Indicators, x="Life expectancy, male", y="GNI per capita", errorbar="sd")
plt.show()

#4.

#5.

#6.
#a) Is there any association between Internet use and emissions per capita?

#b) Which are the countries with high emissions? (> 0.03)

#c) Is there much variation by region (with respect to high emissions vs Internet use)?

#d) Do all high income economies have high emissions?




























