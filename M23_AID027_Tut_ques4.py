import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from scipy.optimize import curve_fit

# Read the weather data from the CSV file

temprature_data = pd.read_csv(r"C:\Users\DELL\Downloads\oneyearTempData.csv")

data = temprature_data[['tmin', 'tmax']]

# Define Gaussian function
def gaussian(x, A, uu, sigma):
    return A * np.exp(-(x - uu)*2 / (2 * sigma*2))

# Fit Gaussian curve to tmin
p_tmin, pcv_tmin = curve_fit(gaussian, np.arange(len(data)), data['tmin'], p0=[1, len(data)/2, 1])

# Fit Gaussian curve to tmax
p_tmax, pcv_tmax = curve_fit(gaussian, np.arange(len(data)), data['tmax'], p0=[1, len(data)/2, 1])

# Generate x values for plotting
x = np.linspace(0, len(data), 100)

# Plotting with Matplotlib
plt.figure(figsize=(10, 6))

# Scatter plot for tmin
plt.scatter(np.arange(len(data)), data['tmin'], color='red', label='tmin')

# Scatter plot for tmax
plt.scatter(np.arange(len(data)), data['tmax'], color='yellow', label='tmax')

# Gaussian fit for tmin
plt.plot(x, gaussian(x, *p_tmin), color='red', linestyle='--', label='tmin fit')

# Gaussian fit for tmax
plt.plot(x, gaussian(x, *p_tmax), color='yellow', linestyle='--', label='tmax fit')

plt.title('Curve Fitting for Min and Max Temperature for Mathura,UP India (2014)')
plt.xlabel('Day')
plt.ylabel('Temperature')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()