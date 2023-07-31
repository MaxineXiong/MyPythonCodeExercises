# Please concatenate this file https://pythonhow.com/media/data/sampledata.txt
# with this one https://pythonhow.com/media/data/sampledata_x_2.txt to a single text file.
import pandas as pd

df1 = pd.read_csv('https://pythonhow.com/media/data/sampledata.txt')
df2 = pd.read_csv('https://pythonhow.com/media/data/sampledata_x_2.txt')

df = pd.concat([df1, df2], axis = 0)
df.to_csv('concatenated.txt', index = False)
