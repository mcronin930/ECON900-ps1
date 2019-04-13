from sklearn import linear_model
import pandas as pd
import re

### Read in parsed data and clean the price type strings
dataset = pd.read_csv("parsed_files/boardgame_dataset.csv")
dataset['key'] = 1
print(dataset.head())
price = dataset['price'].str.replace("Shop",""). \
    str.replace("[","").str.replace("]",""). \
    str.replace("Lowest Amazon", "L_Amazon"). \
    str.replace("New Amazon", "N_Amazon"). \
    str.replace("iOS App", "App"). \
    str.replace("Too low to display", "Too_low"). \
    str.split(": ")

e = len(price) - 1
for i in range(0, e):
    price[i] = "__".join(price[i]).strip()

### Get Unique List of Game Prices By Game and Price Type
df = pd.DataFrame(data=price)
price_list = df['price'].str.split(" ", expand = True)
price_list = pd.DataFrame(data=price_list).stack().str.split("__", expand = True)
price_list.columns = ['Price_type', 'Price']
price_list.index = price_list.index.droplevel(1)
price_list['game_idex'] = price_list.index

### Get Unique List of Price Types
price_type = pd.DataFrame(data = price_list['Price_type']). \
    drop_duplicates(subset='Price_type').dropna(axis=0).drop([15])
price_type['key'] = 1
print(price_type)

### Merge Price Type List With Dataset of Games
# This forms a Cartesian Product of all games and price types
merged_data = dataset.merge(price_type, on = 'key').set_index('Unnamed: 0')
merged_data['game_idex'] = merged_data.index

### Merge ame Prices By Game and Price Type with Game Data
training_data = pd.merge(merged_data, price_list, how='left', on=['game_idex', 'Price_type'])

print(merged_data)
print(price_list)
print(training_data)
# merged_data.to_csv("training_data/boardgame_price_dataset.csv")
