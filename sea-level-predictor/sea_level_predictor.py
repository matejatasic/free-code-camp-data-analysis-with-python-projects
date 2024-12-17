import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(16, 6))
    plt.scatter(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    linear_regression = linregress(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])
    years_up_to_2050 = pd.Series(range(1880, 2051))
    sea_level_rise_from_1880 = (linear_regression.slope * years_up_to_2050) + linear_regression.intercept

    plt.plot(years_up_to_2050, sea_level_rise_from_1880)

    # Create second line of best fit
    data_from_2000_onwards = df[df["Year"] >= 2000]
    linear_regression = linregress(x=data_from_2000_onwards["Year"], y=data_from_2000_onwards["CSIRO Adjusted Sea Level"])

    years_from_2000_to_2050 = pd.Series(range(2000, 2051))
    sea_level_rise_from_2000 = (linear_regression.slope * years_from_2000_to_2050) + linear_regression.intercept

    plt.plot(years_from_2000_to_2050, sea_level_rise_from_2000)

    # Add labels and title
    plt.title(label="Rise in Sea Level")
    plt.xlabel(xlabel="Year")
    plt.ylabel(ylabel="Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()