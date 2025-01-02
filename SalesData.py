import pandas as pd
import os
import matplotlib.pyplot as plt

# df = pd.read_csv('./Sales_Data/Sales_April_2019.csv')
# files = [file for file in os.listdir('./Sales_Data')]
#
#
# all_months_data = pd.DataFrame()
#
#
# for file in files:
#     df = pd.read_csv('./Sales_Data/' + file)
#     all_months_data = pd.concat([all_months_data, df])
#
# all_months_data.to_csv('all_data.csv', index=False)

all_data = pd.read_csv('all_data.csv')
all_data.head()

#Clean up data!
#Drop rows of NaN
nan_df = all_data[all_data.isna().any(axis=1)]

all_data = all_data.dropna(how='all')
# print(all_data.head())

all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']

#Add month Column
all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month'].astype('int32')
# print(all_data.head())

#Covert columns to correct type
all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])

#Add sales column
all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']
# print(all_data.head())

#1. What was the best month for sales? How much was earned that month
all_data.groupby('Month').sum()

results = all_data.groupby('Month').sum()


#
# months = range(1,13)
# plt.bar(months, results['Sales'])
# plt.xticks(months)
# plt.ylabel('Sales in USD ($)')
# plt.xlabel('Months number')
# plt.show()

#Add city column
def get_city(address):
    return address.split(',')[1]


def get_state(address):
    return address.split(',')[2].split(' ')[1]


# all_data['City'] = all_data['Purchase Address'].apply(lambda x: get_city(x) + ' ' + get_state(x))
all_data['City'] = all_data['Purchase Address'].apply(lambda x: f"{get_city(x)} ({get_state(x)})")


#What city had the highest number of sales
# resultsCity = all_data.groupby('City').sum()
#
#
# cities = [city for city, df in all_data.groupby('City')]
#
# plt.bar(cities, results['Sales'])
# plt.xticks(cities, rotation='vertical', size=8)
# plt.ylabel('Sales in USD ($)')
# plt.xlabel('City Name')
# plt.show()

#3. What time should we display advertisement to maximize likelihood of customer's buying product?
all_data['Order Date'] = pd.to_datetime(all_data['Order Date'], format='%m/%d/%Y %H:%M', errors='coerce')

