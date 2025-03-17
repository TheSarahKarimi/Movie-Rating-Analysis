import numpy as np
import csv
import pandas as pd

# Load the dataset
with open('project-1/movies.csv','r',encoding='utf-8') as File: # Used Python (not NumPy) due to quoted string support
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
SelectedIMDB=float(input('Filter movies by IMDB rating: '))
while True:
    if 0<SelectedIMDB<10:
        IMDBIndex=np.where(Rating>=float(SelectedIMDB)) # Fetch the index of movies with rating above 7
        IMDB=DataArray[IMDBIndex[0]+1, 0]
        print(f'Movies with ratings 7 and above includes:\n{IMDB}')
        break
    else:
        SelectedIMDB=float(input('IMDB is in range 1-10! Enter again: '))
print('_'*100,'\n')
GenreColumn=DataArray[1:,2]
SelectedGenre=input('Filter movies by genre: ')
while True:
    if SelectedGenre in Genre:
        DramaIndex=np.where(GenreColumn==SelectedGenre)
        Dramas=DataArray[DramaIndex[0]+1,0]
        print(f'List of {SelectedGenre} movies:\n{Dramas}')
        break
    else:
        SelectedGenre=input('Genre not found! Enter again: ')
print('_'*100,'\n')

# Using Pandas
DataFrame=pd.read_csv('movies.csv') # Read the dataset
LimitedDataFrame=pd.concat([DataFrame.name,DataFrame.genre,DataFrame.year,DataFrame.rating],axis=1) # Create a dataframe with prefered columns
print(f'A prefered preview of the dataset:\n{LimitedDataFrame}')
print('_'*100,'\n')

print(f'Some column name changed:\n{LimitedDataFrame.rename(columns={'name':'movie_title','rating':'IMDB'},inplace=True)}') # Rename some column names
print('_'*100,'\n')

Empty=LimitedDataFrame.isnull().sum() # Disply missing data count grouped by header
print(f'The dataset empty cells count:\n {Empty}') 
print('_'*100,'\n')

LimitedDataFrame.dropna(axis=0,inplace=True) # Handle missing data
print(f'All none-value datas removed:\n{LimitedDataFrame}') # Dataframe without missing data
print('_'*100,'\n')

LimitedDataFrame.sort_values(by='IMDB',ascending=False,inplace=True) # Sort dataframe
print(f'Sorted by IMDB rating:\n{LimitedDataFrame}') 
print('_'*100,'\n')

# Group by year and calculate the average rating
GroupByYear = LimitedDataFrame.groupby('year')
AvgRatingByYear = GroupByYear['IMDB'].mean()
print(f'Average IMDB rating for each year:\n{AvgRatingByYear}')
print('_'*100,'\n')
