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
    str.split(": ")

e = len(price) - 1
for i in range(0, e):
    price[i] = "_".join(price[i])

df = pd.DataFrame(data=price)

df['N_Amazon'] = df.price.str.slice(str.find("N_Amazon"),str.find(" ", str.find("N_Amazon")))

# df = pd.DataFrame()
#
# for i in range(0, e):
#     N_Amazon = price[i][price[i].find("N_Amazon"):price[i].find(" ", price[i].find("N_Amazon"))]
#
#     df = df.append({
#         'N_Amazon': N_Amazon.strip() }, ignore_index=True)

print(df)
