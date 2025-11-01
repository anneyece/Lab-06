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

World_Demographic_Indicators = pd.read_csv("wdi_wide.csv") #acessing data and giving it a variable name "World_Demographic_Indicators"


#3. For instance, use the function info() to list the size of the dataset and its data types.
#how many empty values for the column “Physicians” and “Population”?

print(" ")
print("Information about the data:")
print(" ")
World_Demographic_Indicators.info() # info(): provides the amount of not empty (non-null) cells within each column and total columns in data set

# ANSWER --> “Physicians” = 10 null and “Population” = 0 null


#4. Use the nunique() function to print the number of unique values for each column.

print(" ")
print(" ")
print("Unique values for each column:")
print(" ")
print(World_Demographic_Indicators.nunique()) # nunique(): provides amount of variation (types) within each column 


# 5. Use the describe() function to print further information about your data. What exactly does the output of this function provide?

print(" ")
print(" ")
print("Description of data:")
print(" ")
print(World_Demographic_Indicators.describe()) # describe(): does statistical test on the data that fits ("GNI" and "High Income Economy" for our data set)
print(" ")
print(" ")

#5. Gross National Income (GNI) is an absolute value. It's more appropriate to
# use GNI per capita to answer some questions. Add a new column called “GNI per
# capita” to your dataset with data containing GNI by population. Then use the
# function round() to round it to the nearest cent.

World_Demographic_Indicators['GNI per capita'] = round(World_Demographic_Indicators["GNI"] / World_Demographic_Indicators["Population"], 2) # creating new column "GNI per capita" which consist of the operation of (GNI / Population = GNI per capita) which is then rounded to have 2 decimal place

#7. Using the value_counts() function, print the answer for the following questions:
# a) How many countries are there in each region?

print(" ")
print(" ")
print("Amount of countries in each region:")
print(" ")
print(World_Demographic_Indicators.value_counts("Region")) # value_counts(): provides how many countries are in each region (counts how many times a region reappears looking at the countries)

  
# b) How many hight income economies are there?

print(" ")
print(" ")
print("Amount of high income economies:")
print(" ")
print(World_Demographic_Indicators.value_counts("High Income Economy")) # printing the High Income Economy column and using value_counts() to get the amount


# 8. Using the pd.crosstab() function, print the answer for the question “Where are the high income economies?”. Per region, and including Yes and No.

print(" ")
print(" ")
print("Region of high income economies:")
print(" ")
print(pd.crosstab(World_Demographic_Indicators["High Income Economy"],World_Demographic_Indicators["Region"])) # pd.crosstab(): accesses the specific colunms (region and high income economy) and indicates the amount of times that 0 or 1 (results fron the High Income column) appears which represent the amount of countries within in that region that are (1) or are not (0) a high income economy


# 9. You might need to filter some data from your dataset. Often it can be made without using a loop. For example, the syntax to get only rows with values > 10 in a given column would be:
   
    # filtered_data = data[data[“Your Column”] > 10]
    
#Can you tell me how many countries there are where women can expect to live for more than 80 years? And which countries those are?

life_expectancy_more_80_female = World_Demographic_Indicators[World_Demographic_Indicators["Life expectancy, female"] > 80] # new variable name "life_expectancy_more_80_female" that equals the results of the filtering of the life expectancy column to get life expectancy >80 for females

print(" ")
print(" ")
print("Countries where women can expect to live for more than 80 years:")
print(" ")

for i in life_expectancy_more_80_female["Country Name"]: # "for" loop that finds the corresponding country associated with the women that live for more then 80 years
    print(i) #prints the results


# =============================================================================
# 
# =============================================================================

# Part 4 - Visualizing statistical relationships

#1. Is there any association between GNI per capita and life expectancy?” (one plot for each gender)

#female
sns.relplot(World_Demographic_Indicators, x="Life expectancy, female", y="GNI per capita") # creating scatter plot, x = life expectancy female, y = GNI per capita
#male
sns.relplot(World_Demographic_Indicators, x="Life expectancy, male", y="GNI per capita") # creating scatter plot, x = life expectancy male, y = GNI per capita

plt.show() # Displays the plot


#2. By adding a third “feature” to your plot using colors to represent it in
# order to answer the following question: “Does the association between GNI per
# capita and life expectancy vary by region?” (one plot for each gender)

#female
sns.relplot(World_Demographic_Indicators, x="Life expectancy, female", y="GNI per capita", hue="Region") # creating scatter plot, x = life expectancy female, y = GNI per capita, colours = regions
#male
sns.relplot(World_Demographic_Indicators, x="Life expectancy, male", y="GNI per capita", hue="Region") # creating scatter plot, x = life expectancy male, y = GNI per capita, colours = regions

plt.show() # Displays the plot


#3. Generate a the plot from item 2, now using lines along with standard deviation.

#female
sns.lineplot(World_Demographic_Indicators, x="Life expectancy, female", y="GNI per capita", errorbar="sd", hue="Region") # creating line plot, x = life expectancy female, y = GNI per capita, addition of standard deviation error bars, colours = regions
plt.show() # Displays the plot
#male
sns.lineplot(World_Demographic_Indicators, x="Life expectancy, male", y="GNI per capita", errorbar="sd", hue="Region") # creating line plot, x = life expectancy male, y = GNI per capita, addition of standard deviation error bars, colours = regions
plt.show() # Displays the plot


#4.Use the lmplot() function to generate a linear regression for the previous plot.

#male
sns.lmplot(World_Demographic_Indicators, x="Life expectancy, male", y="GNI per capita", hue="Region") # creating scatter plot, x = life expectancy male, y = GNI per capita, colours = regions, best fit line (linear regression line) for each different region
plt.show() # Displays the plot
#female
sns.lmplot(World_Demographic_Indicators, x="Life expectancy, female", y="GNI per capita", hue="Region") # creating scatter plot, x = life expectancy female, y = GNI per capita, colours = regions, best fit line (linear regression line) for each different region
plt.show() # Displays the plot


#5.Use relplot() to explore relationships between female life expectancy and
#some of the other numerical features. Are these relationships similar for
#male life expectancy? Elaborate at least 5 more questions and generate one
#plot for each to help you answering them. Use “Faceting” feature from seaborn
#to visualize side by side results for female.

sns.relplot(World_Demographic_Indicators, x="Life expectancy, female", y="Tertiary education, female", size="Population", col="Region") 
plt.show() # Displays the plot

#Q1 - What is the linear regression of life expectancy for females vs tertiary education for females per region?

sns.lmplot(World_Demographic_Indicators, x="Life expectancy, female", y="Tertiary education, female", col="Region")
plt.show() # Displays the plot

#Q2 - What is the relationship between life expectancy for females and tertiary education overall (in all the regions)?

sns.lmplot(World_Demographic_Indicators, x="Life expectancy, female", y="Tertiary education, female")
plt.show() # Displays the plot

#Q3 - What is the variation of population in those regions?

sns.relplot(World_Demographic_Indicators, x="Life expectancy, female", y="Tertiary education, female", size="Population") 
plt.show() # Displays the plot

#Q4 - What is the trend that can be observed between life expectancy for females and tertiary education per region?

sns.lineplot(World_Demographic_Indicators, x="Life expectancy, female", y="Tertiary education, female", hue="Region") 
plt.show() # Displays the plot

#Q5 - What is the standard deviation between life expectancy for females and tertiary overall (in all the regions)?

sns.lineplot(World_Demographic_Indicators, x="Life expectancy, female", y="Tertiary education, female", errorbar="sd")


#6.Using your new programming skills, answer the following questions:
#a) Is there any association between Internet use and emissions per capita?

#finding emissions per capita
World_Demographic_Indicators['emissions per capita'] = World_Demographic_Indicators["Greenhouse gas emissions"] / World_Demographic_Indicators["Population"] # creating new column "emissions per capita" which consist of the operation of (greenhouse gas emissions / Population = emissions per capita)

sns.lmplot(World_Demographic_Indicators, x="Internet use", y="emissions per capita") # creating line plot, x = internet use, y = emissions per capita, best fit line (linear regression line)


#b) Which are the countries with high emissions? (> 0.03)

#finding countries with high emissions
emission_per_capita_more_than = World_Demographic_Indicators[World_Demographic_Indicators["emissions per capita"] > 0.03] # new variable name "lemission_per_capita_more_than" that equals the results of the filtering of the emissions per capita column to get emissions per capita >0.03

print(" ")
print(" ")
print("Countries with high emissions per capita:")
print(" ")

high_emissions_countries = [] # list that is currently empty

for i in emission_per_capita_more_than["Country Name"]: # "For" loop that accesses the countries associated with the emissions per capita > 0.03
    high_emissions_countries.append(i) # adding to the list "high_emissions_countries" the different countries that are being accessed
    print(i) #prints the results


#c1) Is there much variation by those region (with respect to high emissions vs Internet use)? Anneyece did this (sir i did not understand the question but heres the code for my understanding)
#-----> "those" regions being Brunei Darussalam and in Qatar (based off the previous questions)

print(" ")
print(" ")
print("Looking at High Emissions vs Internet use by those region:")
print(" ")

for country in high_emissions_countries: # "For" loop that accessing countries in the list "high_emissions_countries" and applying the 
    print(country, ":") # prints the country (from the list of the one by one because  loop cycles through all elements of the list)
    print(World_Demographic_Indicators.loc[World_Demographic_Indicators["Country Name"]== country, ["emissions per capita", "Internet use"]]) # .loc: row or column being accessed is displayed with its corresonding label, for each country in the list, print its emissions per capita and internet use
    print(" ")
    print(" ")

# ANSWER --> Looking at the emissions per capita and internet use in Brunei Darussalam and in Qatar, there is not much variation.

#c2) Is there much variation by all region (with respect to high emissions vs Internet use)?

sns.relplot(World_Demographic_Indicators, x="Internet use", y="emissions per capita", hue="Region")
plt.show() # Displays the plot


#d) Do all high income economies have high emissions?

sns.relplot(World_Demographic_Indicators, x="Population", y="Greenhouse gas emissions", hue="High Income Economy", style="High Income Economy") 

























