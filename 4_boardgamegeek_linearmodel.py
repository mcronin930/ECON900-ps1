from sklearn import linear_model
import pandas as pd

dataset = pd.read_csv("training_data/boardgame_price_dataset.csv")


print(dataset.head())
Training = dataset.dropna(subset=['avg_rating', 'geek_rating', 'rank', 'votes'])


List_Training = Training.loc[(Training['price_type'] == 'List')].dropna(subset=['price'])
List_Missing = Training.loc[(Training['price_type'] == 'List')][pd.isnull(Training['price'])]

print(List_Training)
print(List_Missing)

List_Data = List_Training.iloc[:,[1,3,7,8]].values
print(List_Data)
List_Target = List_Training.iloc[:,-1]
print(List_Target)
#
# ## construct a linear regression machine (as we did witht he KNN machine)
regression = linear_model.LinearRegression()
#
regression.fit(List_Data, List_Target)

List_predict = List_Missing.iloc[:,[1,3,7,8]]
print(List_predict)

results = regression.predict(List_predict)
print(results)
print(regression.score(List_Data, List_Target))
