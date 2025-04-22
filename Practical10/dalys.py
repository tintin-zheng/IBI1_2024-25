# import necessory libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# change the working directory to the Practical10 folder
os.chdir("Practical10")
# read the dalys-rate-from-all-causes.csv file
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

#  showing the third column for the first 10 rows
print(dalys_data.iloc[0:10, 2]) # the 10th year is 1999

# use the Boolean to show DALYs for all countries in 1999
# create a boolean array to filter the data for the year 1999
bool_array = dalys_data["Year"] == 1999
# print the DALYs for all countries in 1999
print(dalys_data.loc[bool_array, "DALYs"])

# create a new dataframe to store the data of UK
uk = dalys_data.loc[dalys_data.Entity == "United Kingdom", ["DALYs", "Year"]]
# create a new dataframe to store the data of France
france = dalys_data.loc[dalys_data.Entity == "France", ["DALYs", "Year"]]
# cauculate the mean of DALYs for UK and France
uk_mean = uk.DALYs.mean()
france_mean = france.DALYs.mean()
# compare the mean of DALYs for UK and France
if uk_mean > france_mean:
    print("UK has a higher mean of DALYs than France")
elif uk_mean < france_mean:
    print("France has a higher mean of DALYs than UK")
else:
    print("UK and France have the same mean of DALYs")
# Result: UK has a higher mean of DALYs than France

# create a plot showing the DALYs over time in UK
plt.plot(uk.Year, uk.DALYs, 'r+')
plt.xticks(uk.Year, rotation=-45)
plt.show()


# answer to the question 1
china = dalys_data.loc[dalys_data.Entity == "China", ["DALYs", "Year"]]
# merge the data of UK and China
merged_data = pd.merge(uk, china, on="Year", suffixes=("_UK", "_China"))
# calulate the difference value of DALYs between UK and China
merged_data["Difference"] = merged_data.DALYs_UK - merged_data.DALYs_China
# plot the difference value of DALYs between UK and China
plt.plot(merged_data.Year, merged_data.Difference, 'r+')
plt.xticks(merged_data.Year, rotation=-45)
plt.show()