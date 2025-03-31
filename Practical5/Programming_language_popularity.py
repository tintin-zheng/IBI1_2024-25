"""
pseudocode:
    import the library for a bar plot plotting
    creat a dictionary to store the data
    print the dictionary
    creat the bar plot
    import the data from the dictionary and choose a color for the bars
    add the title and labels to the plot
    add the data on the top of the bars
    show the plot
    choose a language to check. 
    print the percentage of the users of the chosen language
"""
#import the matplotlib library for a bar plot plotting
import matplotlib.pyplot as plt

#creat a dictionary to store the data about the popularity of programming languages
popularity = { "JavaScript" : 62.3,
              "HTML": 52.9,
              "python": 51, 
              "SQL": 51,
              "TypeScript": 38.5,
              }

#print the dictionary
print(popularity)

#creat the bar plot
#import the data from the dictionary and choose a color for the bars
plt.bar(popularity.keys(), popularity.values(), color = "#81D8CF")
#add the title and labels to the plot
plt.xlabel("Programming Languages")
plt.ylabel("Popularity (%)")
plt.title("Programming Language Popularity")
#add the data on the top of the bars
for key, value in popularity.items():
    plt.text(key, value, str(value))
#show the plot
plt.show()

#choose a language to check. I choose python, the third language in the dictionary,
#and you can change it to any other langusges you like.
language = "python"
#print the percentage of the users of the chosen language
print(f"The percentage of the users of {language} is {popularity[language]}.")