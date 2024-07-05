# Please plot the data of this file https://pythonhow.com/media/data/sampledata.txt into a graph of x and y axis.


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://pythonhow.com/media/data/sampledata.txt")
df.plot.scatter(x='x', y='y')
plt.show()
