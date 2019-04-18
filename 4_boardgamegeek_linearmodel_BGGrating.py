from sklearn import linear_model
import pandas as pd

dataset = pd.read_csv("training_data/boardgame_price_dataset.csv")

df = pd.DataFrame()

dataset['game_age'] = 2019 - dataset['year']
dataset = dataset.dropna(subset=['avg_rating', 'geek_rating', 'rank', 'votes', 'game_age']) \
    [['avg_rating', 'name', 'geek_rating', 'rank', 'votes', 'game_age']].drop_duplicates()
print(dataset.head())

Data = dataset.iloc[:,[0,3,4,5]].values
Target = dataset.iloc[:,[2]].values
print(Data)
print(Target)

regression = linear_model.LinearRegression()
regression.fit(Data, Target)
print("R-Sqaured Score is " + str(regression.score(Data, Target)))
