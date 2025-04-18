# extra tasks
# Author: Tihana Gray
# This script demonstrates how to read a log file into a pandas DataFrame, 
# clean the data, and perform some basic analysis.


# Task 7
import pandas as pd
import re
import matplotlib.pyplot as plt  # needed for the plot in Task 16

path = './data/'
logFilename = path + 'access.log.demo'
df = pd.read_csv(logFilename, sep=' ', header=None)
print(df)

# Task 8
print(df.iloc[0])

# Task 9
colNames = (
    'ip',
    'dash1',
    'userId',
    'time',
    'url',
    'status code',
    'size of response',
    'referer',
    'user agent',
    'dunno'
)
df = pd.read_csv(logFilename, sep=' ', header=None, names=colNames)

# Task 10
df.drop(columns=['dash1', 'userId'], inplace=True)

# Task 11 (clean timestamp string, with fixed regex warning)
df['time'] = df['time'].apply(lambda x: re.search(r'[\w:/]+', x).group())

# Task 12
print(df.dtypes)

# Task 13 (correct line for converting to datetime)
df['time'] = pd.to_datetime(df['time'], format='%d/%b/%Y:%H:%M:%S')

# Task 14
df = df.set_index(['time'])
df = df.sort_index() # added this to avoid error 
newdf = df['2021/02/15 23:00':'2021/02/15 23:59:59']
print(newdf)

# Task 15
downloadSamples = df['size of response'].resample(rule='30Min').mean()
print(downloadSamples)

# Task 16
downloadSamples.plot()
plt.show()
