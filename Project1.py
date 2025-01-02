import pandas as pd

data = pd.read_csv(r'C:\Users\Fenky\Downloads\file.csv')
print(data)
print(data.head())   #Shows the first N rows in data (by default, N=5)
print(data.shape)    #Shows total no. of rows and columns in dataframe
print(data.index)    #Shows index
print(data.columns)         #Shows columns
print(data.dtypes)         #Shows datatypes of the dataframe
print(data['Weather'].unique())  #Shows all unique values in a column
print(data.nunique())         #Shows unique values of each column and be applied to single column or whole dataframe
print(data.count())     #Shows total num of non-null values in each column
print(data['Weather'].value_counts())  #Show all unique values with their count/ only be applied of single column
print(data.info)   #Provides basic information about dataframe

#1. Find all the unique 'Wind Speed' values in the data.
print(data.head(2))
print(data.nunique())
print(data['Wind Speed_km/h'].nunique())
print(data['Wind Speed_km/h'].unique())   #Answer

#2. Find the number of times when the 'Weather is exactly clear'.
print(data.head(2))
print(data.Weather.value_counts())  # Using value_counts

print(data.head(2))
print(data[data.Weather == 'Clear']) # Using filtering

print(data.head(2))
print(data.groupby('Weather').get_group('Clear'))  #Using groupby

#3. Find the number of times when the 'Wind Speed was exactly 4 km/h'
print(data.head(2))
print(data[data['Wind Speed_km/h'] == 4])   #Answer

#4. Find all the Nul values in the data
print(data.isnull().sum())
print(data.notnull().sum())

#5. Rename the column 'Weather' in the dataframe to 'Weather Condition'
print(data.rename(columns={'Weather': 'Weather Condition'}))  # Only changes for this line
data.rename(columns={'Weather': 'Weather Condition'}, inplace=True)  #Changes the column in dataframe
print(data.head())

#6. What is the mean of 'Visibility'?
print(data.head())
print(data.Visibility_km.mean())    #Gives the mean

#7. What is the Standard Deviation of 'Pressure' in this data?
print(data.head())
print(data.Press_kPa.std())      #Gives standard deviation

#8. What is the variance of 'Relative Humidity' in this data?
print(data.head())
print(data['Rel Hum_%'].var()) #Gives variance

#9. Find all instances when 'Snow' was recorded
print(data.columns)
print(data['Weather Condition'].value_counts())
print(data[data['Weather Condition'] == 'Snow'])
print(data[data['Weather Condition'].str.contains('Snow')])  #Using str.contains

#10. Find all instances when 'Wind Speed' is above 24 and 'Visibility' is 25.
print(data.columns)
print(data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)])

#11 What is the mean value of each column against each 'Weather Condition'
# data.groupby('Weather Condition').mean()
print(data.groupby('Weather Condition').mean())

#12 What is the minimum and maximum of each colum against each other in 'Weather Condition'?
print(data.head(2))
print(data.groupby('Weather Condition').min())
print(data.groupby('Weather Condition').max())

#13 Show all records where the weather condition is fog
print(data[data['Weather Condition'] == 'Fog'])

#14 Find all instances when 'Weather is clear' or 'Visibility is above 40'
print(data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km'] > 40)])  # | is or operator

#15 Find instances when 'Weather is clear' and 'Relative Humidity' is greater than 50 or 'Visibility' is above 40
print(data[(data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50) | (data['Visibility_km'] > 40)])
