# Importing libs
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skewnorm

# Create the data
speed = skewnorm.rvs(4, size=50)
size = skewnorm.rvs(4, size=50)

# Create and shor the 2D Density plot
ax = sns.kdeplot(speed, size, cmap="Reds", shade=False, bw=.15, cbar=True)
ax.set(xlabel='speed', ylabel='size')
plt.show()