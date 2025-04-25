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

# use the Boolean to show DALYs for all countries in 1990
# create a boolean array to filter the data for the year 1990
bool_array = dalys_data["Year"] == 1990
# print the DALYs for all countries in 1990
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
plt.title("Difference of DALYs between UK and China")
plt.xlabel("Year")
plt.ylabel("Difference of DALYs")
plt.show()

# answer to the question 2
# find all countries in the dataset
countries = list(set([i for i in dalys_data.Entity if "World" not in i and "OECD" not in i and "WHO" not in i and "WB" not in i and "G20" not in i]))

# divide the countries by continent
# create a dictionary to store the countries by continent
# countries were divided by continent by Claude, and I checked the correctness of the data myself.
world_by_continent = {
   "Asia": [
       "Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", 
       "Bhutan", "Brunei", "Cambodia", "China", "Cyprus", "Georgia", 
       "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", 
       "Kazakhstan", "Kuwait", "Kyrgyzstan", "Laos", "Lebanon", "Malaysia", 
       "Maldives", "Mongolia", "Myanmar", "Nepal", "North Korea", "Oman", 
       "Pakistan", "Palestine", "Philippines", "Qatar", "Russia", "Saudi Arabia", 
       "Singapore", "South Korea", "Sri Lanka", "Syria", "Taiwan", "Tajikistan", 
       "Thailand", "Turkey", "Turkmenistan", "United Arab Emirates", "Uzbekistan", 
       "Vietnam", "Yemen", "East Timor"
   ],

   
   "Africa": [
       "Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", 
       "Cameroon", "Cape Verde", "Central African Republic", "Chad", "Comoros", 
       "Congo", "Cote d'Ivoire", "Democratic Republic of Congo", "Djibouti", 
       "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", 
       "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", 
       "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", 
       "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", "Sao Tome and Principe", 
       "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", 
       "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"
   ],
   
   "Europe": [
       "Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina", 
       "Bulgaria", "Croatia", "Czechia", "Denmark", "England", "Estonia", "Finland", 
       "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Latvia", 
       "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", 
       "North Macedonia", "Northern Ireland", "Norway", "Poland", "Portugal", "Romania", 
       "Russia", "San Marino", "Scotland", "Serbia", "Slovakia", "Slovenia", "Spain", 
       "Sweden", "Switzerland", "Turkey", "Ukraine", "United Kingdom", "Wales"
   ],
   
   "North America": [
       "Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Bermuda", "Canada", 
       "Costa Rica", "Cuba", "Dominica", "Dominican Republic", "El Salvador", "Grenada", 
       "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", 
       "Puerto Rico", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", 
       "Trinidad and Tobago", "United States", "United States Virgin Islands"
   ],
   
   "South America": [
       "Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", 
       "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"
   ],
   
   "Oceania": [
       "American Samoa", "Australia", "Cook Islands", "Fiji", "Guam", "Kiribati", 
       "Marshall Islands", "Micronesia (country)", "Nauru", "New Zealand", "Niue", 
       "Northern Mariana Islands", "Palau", "Papua New Guinea", "Samoa", "Solomon Islands", 
       "Tokelau", "Tonga", "Tuvalu", "Vanuatu"
   ]
}
#calculate the mean of DALYs for each continent
continent_means = {}
for continent, countries in world_by_continent.items():
    # create a boolean array to filter the data for the countries in the continent
    bool_array = dalys_data.Entity.isin(countries)
    # calculate the mean of DALYs for the countries in the continent
    continent_means[continent] = dalys_data.loc[bool_array, "DALYs"].mean()
# draw a bar chart to show the mean of DALYs for each continent
plt.bar(continent_means.keys(), continent_means.values(), color = "blue")
#add the title and labels
plt.title("Mean of DALYs for each continent")
plt.xlabel("Continent")
plt.ylabel("Mean of DALYs")
# add data on the top of the bars
for i, value in continent_means.items():
    plt.text(i, value + 0.05, f"{value:.2f}", ha = "center", va = "bottom")
plt.show()