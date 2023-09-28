import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    #df.fillna(0)

    # Create scatter plot
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]
  
    fig, axis = plt.subplots()
    plt.scatter(x,y)
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
  
    # Create first line of best fit
    xprediction = pd.Series([i for i in range(1880, 2051)])
    yprediction = slope * xprediction + intercept
    plt.plot(xprediction, yprediction, "g")

    # Create second line of best fit
    df1 = df[df["Year"] >= 2000]
    x1 = df1["Year"]
    y1 = df1["CSIRO Adjusted Sea Level"]
    #plt.scatter(x1,y1)
    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(x1, y1)
  
    # Create first line of best fit
    x1prediction = pd.Series([i for i in range(2000, 2051)])
    y1prediction = slope1 * x1prediction + intercept1
    plt.plot(x1prediction, y1prediction, "r")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
