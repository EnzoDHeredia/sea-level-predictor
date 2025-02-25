import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    y = df['CSIRO Adjusted Sea Level']
    x = df['Year']


    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x, y)

    # Create first line of best fit
    slope, intercept = linregress(x, y)[:2]
    x_pred = pd.Series([i for i in range(1880, 2051)])
    y_pred = slope * x_pred + intercept
    plt.plot(x_pred, y_pred, 'r')


    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    x_2000 = df_2000['Year']
    y_2000 = df_2000['CSIRO Adjusted Sea Level']
    slope_2000, intercept_2000 = linregress(x_2000, y_2000)[:2]
    x_pred_2000 = pd.Series([i for i in range(2000, 2051)])
    y_pred_2000 = slope_2000 * x_pred_2000 + intercept_2000
    plt.plot(x_pred_2000, y_pred_2000, 'g')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()