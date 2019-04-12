from sklearn import linear_model
import pandas as pd
import re

dataset = pd.read_csv("parsed_files/boardgame_dataset.csv")
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

df = pd.DataFrame(data=price)
price_list = df['price'].str.split(" ", expand = True)
price_list = pd.DataFrame(data=price_list).stack().str.split("__", expand = True)
price_list.columns = ['Price_type', 'Price']
price_list.index = price_list.index.droplevel(1)
merged_data = price_list.join(dataset, how='outer')

print(merged_data)
merged_data.to_csv("training_data/boardgame_price_dataset.csv")
