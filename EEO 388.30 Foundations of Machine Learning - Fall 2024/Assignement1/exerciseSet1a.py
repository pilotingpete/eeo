import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

# Create a NumPy array with 1 column and 100 rows, filled with random numbers
array_1d = np.random.randn(100)


# Convert the 1D array into a pandas Series
series_1d = pd.Series(array_1d)
print(series_1d)


# Create a NumPy array with 3 columns and 100 rows, filled with random integers
array_3d = np.random.randn(100, 3)


# Convert the 3-column array into a DataFrame with column labels
df = pd.DataFrame(array_3d, columns=['X1', 'X2', 'X3'])
print(df)


# Use Seaborn to create a pairplot of the DataFrame
sns.pairplot(df)
#plt.show()

# Generate current timestamp in the format yyyy-mm-dd-hh-mm-ss
timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

# Create the file name with timestamp prepended
filename = f"{timestamp}_pairplot.png"
plt.savefig(filename)

