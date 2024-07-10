import pandas as pd
import numpy as np
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns

# Data provided
data = """
T2M,1981,9.74,10.32,14.04,16.94,19.79,23.71,25.37,26.67,25.0,21.54,15.31,13.35,18.53
T2M,1982,12.78,11.77,12.61,14.73,19.04,25.98,29.55,27.71,25.15,20.39,15.59,11.38,18.93
T2M,1983,10.9,10.33,12.81,16.75,20.12,23.53,28.76,27.2,24.55,19.8,16.52,12.3,18.68
T2M,1984,11.41,10.74,12.3,15.07,19.22,23.05,27.1,26.14,23.55,19.35,16.68,12.62,18.12
T2M,1985,9.96,13.01,12.07,15.71,18.78,23.83,27.89,26.84,24.3,20.33,16.63,13.42,18.59
T2M,1986,11.26,11.44,13.07,15.98,21.05,23.1,25.83,28.51,24.98,20.94,15.43,12.01,18.68
T2M,1987,10.74,11.57,11.75,15.78,17.66,23.39,28.27,28.68,26.67,22.66,16.17,14.19,19.01
T2M,1988,12.79,12.08,13.46,17.15,21.4,23.72,27.89,28.38,23.94,22.24,16.19,12.32,19.33
T2M,1989,11.34,11.89,14.76,16.37,19.28,23.26,27.32,27.77,24.36,19.49,16.52,14.73,18.97
T2M,1990,12.08,13.91,14.04,15.51,19.53,24.71,26.65,26.23,25.94,22.65,16.1,11.24,19.08
T2M,1991,11.24,10.66,14.24,13.9,16.62,22.67,26.51,27.39,25.21,20.56,15.4,11.56,18.05
T2M,1992,10.47,10.96,12.96,15.49,19.26,22.23,25.05,27.86,24.86,20.83,16.7,12.69,18.3
T2M,1993,11.19,10.9,12.46,16.3,20.12,23.78,26.52,28.01,24.87,21.65,15.94,12.82,18.76
T2M,1994,12.08,12.04,14.6,15.04,22.01,24.19,27.65,30.2,26.36,21.06,17.44,13.73,19.75
T2M,1995,10.87,13.3,12.9,15.28,20.49,23.49,26.76,27.38,23.92,20.57,15.82,14.06,18.77
T2M,1996,12.84,11.11,13.09,15.19,19.09,22.69,26.12,27.76,22.56,18.71,16.08,13.27,18.24
T2M,1997,12.38,12.74,13.34,15.11,21.13,26.15,26.94,26.88,23.65,20.98,16.0,13.13,19.08
T2M,1998,11.43,12.01,13.14,16.67,19.18,25.34,27.22,27.01,24.53,19.51,14.62,11.46,18.55
T2M,1999,11.4,10.03,13.37,15.83,21.92,25.18,26.49,29.69,25.9,22.19,15.97,11.86,19.21
T2M,2000,9.96,11.6,13.86,16.92,21.54,23.38,27.53,28.34,24.66,19.93,16.55,13.69,19.02
T2M,2001,11.94,11.73,16.35,15.9,19.91,24.81,27.25,27.7,23.78,22.9,16.28,11.83,19.25
T2M,2002,10.51,12.49,14.53,16.35,19.59,25.1,26.66,26.94,23.57,20.5,16.56,13.4,18.89
T2M,2003,11.62,9.81,12.3,15.9,19.72,25.8,29.17,29.82,24.21,21.41,16.32,11.66,19.04
T2M,2004,11.0,11.6,12.8,14.87,17.63,22.66,26.19,27.56,24.23,22.3,15.35,12.78,18.27
T2M,2005,10.05,9.24,12.69,15.08,20.35,24.65,27.56,26.41,23.91,21.01,15.96,11.32,18.24
T2M,2006,9.8,10.58,13.08,17.17,21.15,24.6,27.58,26.7,24.08,21.8,16.62,13.18,18.91
T2M,2007,12.55,12.75,12.9,16.03,19.99,24.41,26.99,27.5,24.17,20.13,14.88,11.92,18.72
T2M,2008,11.21,11.37,12.98,16.62,20.18,23.76,27.76,28.13,24.94,20.6,15.29,11.65,18.73
T2M,2009,11.15,10.07,12.55,14.87,19.75,23.93,27.69,28.42,24.34,19.65,15.98,13.48,18.55
T2M,2010,11.59,12.11,13.72,16.22,19.08,22.83,27.23,27.07,23.93,20.08,15.73,12.01,18.51
T2M,2011,11.13,10.49,12.4,16.26,19.15,23.12,27.02,27.35,25.44,19.92,16.26,12.73,18.48
T2M,2012,11.4,9.01,13.01,16.05,19.35,26.12,28.3,29.38,24.47,21.33,17.35,12.58,19.06
T2M,
"""

lines = data.strip().split("\n")
data_points = [line.split(",") for line in lines if line.strip()]

years = []
temperatures = []

for row in data_points:
    try:
        year = int(row[1])
        temp_data = [float(value) for value in row[2:]]
        years.append(year)
        temperatures.append(temp_data)  # Append the entire list of temperature data for each year
    except (ValueError, IndexError) as e:
        print(f"Error processing row: {row}. Error message: {str(e)}")

# Plotting
for year, temps in zip(years, temperatures):
    plt.plot([year] * len(temps), temps, marker='o', linestyle='-', color='b')

plt.xlabel('Year')
plt.ylabel('Temperature')
plt.title('Temperature Trends')
plt.grid(True)
plt.show()