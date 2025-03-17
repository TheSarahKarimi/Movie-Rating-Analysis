import numpy as np
import csv

# Load the dataset
with open('movies.csv','r',encoding='utf-8') as File: # Used Python (not NumPy) due to quoted string support
    RawData=csv.reader(File)
    DataList=list(RawData) # Convert to list
DataArray=np.array(DataList,dtype=str) # Convert to NumPy Array

# Explore the dataset
print('\n','_'*100,'\n')
print(f'Given dataset\'s header: \n\n{DataArray[0]}')
print('_'*100)
print(f'The dataset has {DataArray.shape[1]} columns and {DataArray.shape[0]} rows')
print('_'*100)
print('A preview of dataset (first 5 rows, header exculded):\n')
for Rows in DataArray[1:6]:
    print(Rows,'\n')
print('_'*100,'\n')

# Calculate basic statistics
RatingColumn=DataArray[1:,6].astype('O') # Extract the Rating column (Converted to object to allow mixed types)
Rating=np.where(RatingColumn=='',np.nan,RatingColumn).astype(float) # Replace empty strings with 'nan'
print('*'*10,'Rating\'s overview:','*'*10)
print(f'\nMean of rating: {np.nanmean(Rating):.1f}')
print(f'Median of rating: {np.nanmedian(Rating):.2f}')
print(f'Standard deviation of rating: {np.nanstd(Rating):.2f}')
print('_'*100,'\n')

