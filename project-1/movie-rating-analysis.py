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
Rating=np.where(RatingColumn=='',np.nan,RatingColumn).astype(float) # Replace empty strings with nan
print('*'*10,'Rating\'s overview:','*'*10)
print(f'\nMean of rating: {np.nanmean(Rating):.1f}')
print(f'Median of rating: {np.nanmedian(Rating):.2f}')
print(f'Standard deviation of rating: {np.nanstd(Rating):.2f}')
print('_'*100,'\n')

# Some numerical computation with NumPy
YearColumn=DataArray[1:,3].astype('O') # Extract the year column
Year=np.where(YearColumn=='',np.nan,YearColumn) # Replace empty strings with nan
print('*'*10,'Some facts about this dataset:','*'*10)
print(f'\n1.The oldest movie belong to {np.nanmin(Year)} and {np.max(Year)} is the latest release!')

FirstYearIndex=np.where(Year==np.nanmin(Year)) # Fetch oldest year's movies tuple
LastYearIndex=np.where(Year==np.nanmax(Year))# Fetch latest year's movies tuple
FirstYearReleaseds=DataArray[FirstYearIndex[0]] # Access oldest year's movies index
LastYearReleaseds=DataArray[LastYearIndex[0]] # Access latest year's movies index
FirstBudgetColumn=FirstYearReleaseds[:,12] # Extract the budget value of oldest year's movies
LastBudgetColumn=LastYearReleaseds[:,12] # Extract the budget value latest year's movies
def to_numeric(value): # Convert to numeric, replace non-numeric with nan
    try:
        return int(value)  # Try converting to int
    except ValueError:
        return np.nan  # Return nan if conversion fails
FirstBudget=[]
for BudgetIndex in FirstBudgetColumn: # Allocate total budget of oldest year's movies
    FirstNumericValue=to_numeric(BudgetIndex) 
    FirstBudget.append(FirstNumericValue) 
LastBudget=[]
for BudgetIndex in LastBudgetColumn: # Allocate total budget of latest year's movies
    LastNumericValue=to_numeric(BudgetIndex)
    LastBudget.append(LastNumericValue) 
print(f'\n2.On {np.nanmin(Year)}, {np.nansum(FirstBudget)} $ was spent on movies,while the budget allocated to {np.nanmin(Year)}\'s movies was {np.nansum(LastBudget)} $!')

Genre=np.unique(DataArray[1:,2])
print(f'\n3.This dataset has {np.shape(Genre)[0]} genres including:\n{Genre}')

print('_'*100,'\n')

# Dataset filtering
Above7Index=np.where(Rating>=7) # Fetch the index of movies with rating above 7
Rating = np.where(Rating == '', np.nan, Rating).astype(float)
Above7=DataArray[Above7Index[0]+1, 0]
print(f'Movies with ratings 7 and above includes:\n{Above7}')
print('_'*100,'\n')