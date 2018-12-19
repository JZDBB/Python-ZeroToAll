# Import libs
import pandas as pd
from matplotlib import pyplot as plt
from scipy.cluster import hierarchy
import numpy as np

# Read in the dataset
# Drop any fields that are strings
# Only get the first 40 because this dataset is big
df = pd.read_csv('Pokemon.csv')
df = df.set_index('Name')
del df.index.name
df = df.drop(["Type 1", "Type 2", "Legendary"], axis=1)
df = df.head(n=40)

# Calculate the distance between each sample
Z = hierarchy.linkage(df, 'ward')

# Orientation our tree
hierarchy.dendrogram(Z, orientation="left", labels=df.index)

plt.show()