import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df_raisin = pd.read_csv('../data-sets/Raisin_Dataset.csv')

# Scatter plot matrix
sns.pairplot(df_raisin, hue='Class', markers=["o", "s"])
plt.show()

# Histograms
df_raisin.hist(bins=30, figsize=(10, 7))
plt.tight_layout()
plt.show()

# Check for class distribution
print(df_raisin['Class'].value_counts())
