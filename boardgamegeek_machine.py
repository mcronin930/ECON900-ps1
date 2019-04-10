from sklearn import linear_model
import pandas as pd
import re

dataset = pd.read_csv("parsed_files/boardgame_dataset.csv")
print(dataset.head())

price = list(dataset['price'].astype(str))
print(price)

# print(price.dtypes)
#
# for i in price:
#     prices.append(i.split('$')[0])
#
# print(prices.head())


# a = ['apple,orange,cherry', 'tomato,potato,cucumber', 'pear,grape, kiwi']
# b = [s.split(',') for s in a]
#
# b = pd.DataFrame(b)
# print(b)
