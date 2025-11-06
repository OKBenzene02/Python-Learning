# Calculation of trimmed mean...
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['figure.figsize'] = 10, 5

# Importing the data and specifying the percentage of data to be trimmed.....
data = pd.read_csv('Book1.csv', sep=',', header=None)
print(len(data))

val_num = int(len(data) * .1)
print(val_num) # Trimmed to 10%

# Converting the 2d data into a 1d array.
list_data = sorted(data.values.reshape(1, -1).tolist()[0])
print(list_data)

list_data = list_data[val_num::]
print(list_data)
list_data = list_data[:len(list_data) - val_num]
print(list_data)
print(np.mean(list_data))
print(stats.trim_mean(data, .1))

estimates = [5] * len(list_data)

plt.plot(list_data, estimates, color='red', ls='--')
plt.plot([np.mean(list_data)], [5], color='black', marker='^', markersize=10)
plt.plot([np.median(list_data)], [5], color='blue', marker='o', markersize=10)
plt.plot([372.35], [5], color='grey', marker='*', markersize=10)
plt.xlabel('Estimates')
plt.ylabel('Centered Estimates')
plt.title('Mean Median Plot of Estimates')
plt.show()

