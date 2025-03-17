import numpy as np
import csv

# Load the dataset
with open('movies.csv','r',encoding='utf-8') as File: # Used Python (not NumPy) due to quoted string support
    RawData=csv.reader(File)
    DataList=list(RawData) # Convert to list
DataArray=np.array(DataList,dtype=str) # Convert to NumPy Array


