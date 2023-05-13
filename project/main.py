import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import os


df = pd.read_csv("test.csv")
df = df[(df['LONGITUDE'] >= -74.4) & (df['LONGITUDE'] <= -70) & (df['LATITUDE'] <= 41)]
# Define the x and y variables
x = df['LONGITUDE']
y = df['LATITUDE']

# Define the color for each borough
colors = {'QUEENS': 'red', 'BROOKLYN': 'blue', 'MANHATTAN': 'green', 'BRONX': 'purple', 'STATEN ISLAND': 'orange'}

# Define the color for each data point based on its predicted borough
color_list = [colors[borough] for borough in df['BOROUGH_RF']]

# Create the scatter plot
fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(x, y, color=color_list, alpha=0.5)

# Set the plot title and axis labels
ax.set_title('Predicted Boroughs', fontsize=20)
ax.set_xlabel('Longitude', fontsize=16)
ax.set_ylabel('Latitude', fontsize=16)

# Display the plot
plt.show()