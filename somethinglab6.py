#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 16:38:21 2025

@author: isabel
"""

print(" ")
print(" ")
print("Countries with high GNI per capita (>13935):")
print(" ")

high_income_countries = []

for i in GNI_per_cap_more_than["Country Name"]:
    high_income_countries.append(i)
    print(i)

print(" ")
print(" ")
print("Countries with high GNI per capita(>13935) with their emissions per capita:")
print(" ")

for country in high_income_countries:
    print(country, ":")
    print(World_Demographic_Indicators.loc[World_Demographic_Indicators["Country Name"]== country, ["emissions per capita"]])
    print(" ")
    print(" ")