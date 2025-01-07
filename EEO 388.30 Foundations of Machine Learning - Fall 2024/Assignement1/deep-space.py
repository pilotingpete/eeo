import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df_deepspace = pd.read_csv('../data-sets/DeepSpaceData.csv')

# Scatter plot matrix without class labels
sns.pairplot(df_deepspace)
plt.show()


# Histograms
df_deepspace.hist(bins=30, figsize=(10, 7))
plt.tight_layout()
plt.show()