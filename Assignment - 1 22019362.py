# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 2023
@author: Durga
"""


import pandas as pd
import matplotlib.pyplot as plt


def read_data_lineplot():
    """ "
    This function will read data from average yearly temperature of countries data set
    """
    Temperature_dataset = pd.read_csv("average yearly temperature of countries.csv")
    return Temperature_dataset


def read_data_barplot():
    """ "
    This function will read data from average yearly temperature of countries data set
    """
    Game_dataset = pd.read_csv("android-games.csv")
    return Game_dataset


def read_data_boxplot():
    """ "
    This function will read data from Cricketers data set
    """
    Cricket_dataset = pd.read_csv("Cricketers Data.csv")
    return Cricket_dataset


def addlabels(x, y):
    """
    This function is to add value lables to bar chart
    """
    for i in range(len(x)):
        plt.text(i, 40 / y[i], str(y[i]) + " M", ha="center")


def line_plot():
    """
    This function plots average yearly temperature of 5 countries for past 5 years
    """


# Calling the function to read data
Temperature_dataset = read_data_lineplot()
print(Temperature_dataset)
plt.figure(figsize=(15, 8))
Year = Temperature_dataset["Year"]
Argentina = Temperature_dataset["Argentina"]
Australia = Temperature_dataset["Australia"]
Germany = Temperature_dataset["Germany"]
India = Temperature_dataset["India"]
United_Kingdom = Temperature_dataset["United Kingdom"]
# Plot the data and its label
plt.plot(Year, Argentina, label="Argentina")
plt.plot(Year, Australia, label="Australia")
plt.plot(Year, Germany, label="Germany")
plt.plot(Year, India, label="India")
plt.plot(Year, United_Kingdom, label="United Kingdom")
# Setting X-axis limits and y-axis
plt.xlim(2017, 2023)
plt.ylim(0, 30)
# Assigining Title, X-axis label, Y-axis label
plt.title("Average yearly temperature of countries")
plt.xlabel("Years")
plt.ylabel("Temperature (°C)")
# Showing the legend
plt.legend()
# Saving the image
plt.savefig("line.png", bbox_inches="tight", dpi=1000)
plt.show()


def bar_plot():
    """
    This function plots top 10 andriod games in playstore
    """


# Calling the function to read data
Andriod_Games_dataset = read_data_barplot()
print(Andriod_Games_dataset)
Name = Andriod_Games_dataset["title"]
rating_count = Andriod_Games_dataset["total ratings"]
Rank = Andriod_Games_dataset["rank"]
plt.figure(figsize=(15, 8))
# Ploting the bar chart with Name and Rank data
bars = plt.bar(Name[:10], Rank[:10])
# Setting to make x-axis label alignment
plt.xticks(rotation=90, horizontalalignment="center")
plt.ylim(0, 15)
# calling the function to add value labels
addlabels(Name[:10], rating_count[:10])
# Assigining Title, X-axis label, Y-axis label
plt.xlabel("Andriod Games")
plt.ylabel("Rank")
plt.title("Top 10 andriod games in playstore")
# Saving the image
plt.savefig("bar.png", bbox_inches="tight", dpi=500)
plt.show()


def box_plot():
    """
    This function creates a box plot which shows us the comparision between two cricket players in the period (2019 - 2022)
    """


# Calling the function to read data
Cricket_dataset = read_data_boxplot()
print(Cricket_dataset)
Virat_Runs = Cricket_dataset["Virat Kohli"]
Smith_Runs = Cricket_dataset["Steve Smith"]
data = [Virat_Runs, Smith_Runs]
fig = plt.figure(figsize=(10, 7))
# Creating axes instance
ax = fig.add_axes([0, 0, 1, 1])
# Creating plot
bp = ax.boxplot(data)
plt.xticks([1, 2], ["Virat Kohli", "Steve Smith"])
plt.ylim(0, 1400)
# Assigining Title, X-axis label, Y-axis label
plt.xlabel("Player Name")
plt.ylabel("Runs")
plt.title("Comparision between two cricket players for period (2019 - 2022)")
# Saving the image
plt.savefig("box.png", bbox_inches="tight", dpi=500)
plt.show()


# Calling function to visualise line plot
line_plot()

# Calling function to visualise Bar plot
bar_plot()

# Calling function to visualise Bar plot
box_plot()
