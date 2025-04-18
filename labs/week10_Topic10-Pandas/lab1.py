# creating a data from with data in it
# Author: Tihana Gray

import pandas as pd
listDAta= [
['John', 'math', 23],
['John', 'programming', 66],
['Mary', 'math', 45],
['Mary', 'programming', 33],
['Mark', 'SIEM', 57],
['Mark', 'programming', 70],
['Mark', 'math', 73],
['John', 'programming', 61]
]
df = pd.DataFrame(listDAta, columns=['name','subject','grade'])
print(df.head(3))


print(df.describe())
print(type(df.describe()))


path = "./data/"
csvFilename = path + 'grades.csv'
df.to_csv(csvFilename)


excelFilename = path +'grades.xlsx'
df.to_excel(excelFilename, index=False, sheet_name='data')


with pd.ExcelWriter(excelFilename, engine='openpyxl', mode='a') as writer:
    df.describe().to_excel(writer, sheet_name="summary")


mean = df.describe().loc['mean','grade']
print(mean)
# or
mean = df['grade'].mean()
print (mean)


# there is comma in the csv file beacause andas includes the DataFrame’s index by default when writing to CSV.
# because my index doesn’t have a name, it just appears as an empty header in the CSV file.

