# Import libs
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Get the data
df=pd.read_csv("avengers_csv.csv")
print(df)

"""
   #             Name  Attack  Defense  Speed  Range  Health
0  1         Iron Man      83       80     75     70      70
1  2  Captain America      60       62     63     80      80
2  3             Thor      80       82     83    100     100
3  3             Hulk      80      100     67     44      92
4  4      Black Widow      52       43     60     50      65
5  5          Hawkeye      58       64     58     80      65

"""

# Get the data for Iron Man
labels=np.array(["Attack","Defense","Speed","Range","Health"])
stats=df.loc[0,labels].values

# Make some calculations for the plot
angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
stats=np.concatenate((stats,[stats[0]]))
angles=np.concatenate((angles,[angles[0]]))

# Plot stuff
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, stats, 'o-', linewidth=2)
ax.fill(angles, stats, alpha=0.25)
ax.set_thetagrids(angles * 180/np.pi, labels)
ax.set_title([df.loc[0,"Name"]])
ax.grid(True)

plt.show()