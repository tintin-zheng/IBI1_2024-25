#import the matplotlib library
import matplotlib.pyplot as plt

#creat two lists to store the data from UK and China
uk_countries = [57.11, 3.13, 1.91, 5.45]
china_provinces = [65.77, 41.88, 45.28, 61.27, 85.15]
#sort the data in the lists
sorted_uk_countries = sorted(uk_countries)
sorted_china_provinces = sorted(china_provinces)
#print the sorted lists
print(f"The sorted list of uk_countries is {sorted_uk_countries}.")
print(f"The sorted list of china_provinces is {sorted_china_provinces}.")

#creat two pie charts displaying the distribution of population sizes separately in	UK countries	
#and Zhejiang-neighbouring provinces

#creat the pie chart for the UK countries
#assign the figure number
plt.figure(1)
#set the labels for the pie chart
labels_uk = ["England", "Wales", "Northern Ireland", "Scotland"]
#set the colors I LOVE for the pie chart
colors_uk = ["#4DA4BA", "#85BBDA", "#1C60AC", "#5C7FAD"]
#creat the pie chart
plt.pie(uk_countries, labels = labels_uk, colors = colors_uk, autopct = "%1.2f%%" )
#add the title to the pie chart
plt.title("Population size distribution in UK countries")

#creat the pie chart for the Zhejiang-neighbouring provinces
#assign the figure number
plt.figure(2)
#set the labels for the pie chart
labels_china = ["Zhengjiang", "Fujian", "Jiangxi", "Anhui", "Jiangsu"]
#set the colors I LOVE for the pie chart
colors_china = ["#AD1414", "#FFA12C", "#FFFE93", "#D3632C", "#683024"]
#creat the pie chart
plt.pie(china_provinces, labels = labels_china, colors = colors_china, autopct = "%1.2f%%" )
#add the title to the pie chart
plt.title("Population size distribution in Zhejiang-neighbouring provinces")
#show the pie chart
plt.show()

#try another plot to display the data
#use bar plot 
#creat the bar plot fro the UK countries
#assign the figure number
plt.figure(3)
#set the colors I LOVE for the bar plot
colors = ["#4DA4BA", "#85BBDA", "#1C60AC", "#5C7FAD"]
#creat the bar plot
plt.bar(labels_uk, uk_countries, color = colors)
#add the title and labels to the bar plot
plt.xlabel("UK countries")
plt.ylabel("Population size (millions)")
plt.title("Population size in UK countries")
#add the data on the top of the bars
for labels_uk, uk_countries in dict(zip(labels_uk, uk_countries)).items():
    plt.text(labels_uk, uk_countries, str(uk_countries))


#creat the bar plot for the Zhejiang-neighbouring provinces
#assign the figure number
plt.figure(4)
#set the colors I LOVE for the bar plot
colors = ["#AD1414", "#FFA12C", "#FFFE93", "#D3632C", "#683024"]
#creat the bar plot
plt.bar(labels_china, china_provinces, color = colors)
#add the title and labels to the bar plot
plt.xlabel("Zhejiang-neighbouring provinces")
plt.ylabel("Population size (millions)")
plt.title("Population size in Zhejiang-neighbouring provinces")
#add the data on the top of the bars
for labels_china, china_provinces in dict(zip(labels_china, china_provinces)).items():
    plt.text(labels_china, china_provinces, str(china_provinces))
#show the bar plot
plt.show()
