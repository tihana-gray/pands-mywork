# demonstrate reading from TSV and excel
# Author: Tihana Gray

import pandas as pd
import re
import numpy as np
import dataManipulation

import os
print("📁 Current working directory:", os.getcwd())
print("📄 File exists:", os.path.isfile("originalData.tsv"))


filename = 'originalData.tsv'
workbookFileName = 'timetableData.xlsx'

df = pd.read_table(filename)
print("TSV data preview:\n", df.head())

df.to_excel(workbookFileName, sheet_name='activities', index=False)
print(f"Wrote 'activities' to {workbookFileName}")

ds_staff = dataManipulation.getSeriesOfUnique(df, 'Staff (delimited)')
print("Unique staff series preview:\n", ds_staff.head())

#print (ds_staff) # debug I should use logging
# we have to use a different engin (openpyxl) to append to the book
with pd.ExcelWriter(workbookFileName, engine='openpyxl', mode='a') as writer:
    ds_staff.to_excel(writer, sheet_name="staff", index=False)