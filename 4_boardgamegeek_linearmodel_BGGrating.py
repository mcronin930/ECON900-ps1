
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.model_selection import KFold

dataset = pd.read_csv("training_data/boardgame_price_dataset.csv")

df = pd.DataFrame()

dataset['game_age'] = 2019 - dataset['year']
dataset = dataset.dropna(subset=['avg_rating', 'geek_rating', 'rank', 'votes', 'game_age']) \
    [['avg_rating', 'name', 'geek_rating', 'rank', 'votes', 'game_age']].drop_duplicates()
print(dataset.head())

data = dataset.iloc[:,[0,3,4,5]].values
target = dataset.iloc[:,[2]].values
print(data)
print(target)

kfold_machine = KFold(n_splits = 4, shuffle = True)
kfold_machine.get_n_splits(data)
print(kfold_machine)
print(data)
i = 1
for training_index, test_index in kfold_machine.split(data):
    print("Training: ", training_index)
    print("Test: ", test_index)
    data_training, data_test = data[training_index], data[test_index]
    target_training, target_test = target[training_index], target[test_index]
    regression = linear_model.LinearRegression()
    regression.fit(data_training,target_training)
    prediction = regression.predict(data_test)
    print(metrics.r2_score(target_test,prediction))

    df = df.append({
        'Split': i,
        'R-Squared Score': metrics.r2_score(target_test,prediction),
        }, ignore_index=True)

    i = i+1

print(df)
