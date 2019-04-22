from sklearn import linear_model
import pandas as pd

dataset = pd.read_csv("training_data/boardgame_price_dataset.csv")

d = {}
df = pd.DataFrame()
print(dataset.head())
Training = dataset.dropna(subset=['avg_rating', 'geek_rating', 'rank', 'votes', 'year'])
Training['game_age'] = 2019 - Training['year']

types = ['List', 'L_Amazon', 'N_Amazon', 'App', 'Amazon']

for i in types:
    OLS_Training = Training.loc[(Training['price_type'] == i)].dropna(subset=['price'])
    Pred_Missing = Training.loc[(Training['price_type'] == i)][pd.isnull(Training['price'])]
    print(OLS_Training)
    print(Pred_Missing)

    Data = OLS_Training.iloc[:,[1,3,7,8,-1]].values
    Target = OLS_Training.iloc[:,13]

    regression = linear_model.LinearRegression()

    regression.fit(Data, Target)

    OLS_predict = Pred_Missing.iloc[:,[1,3,7,8,-1]]
    print(OLS_predict)

    results = regression.predict(OLS_predict)
    print(results)


    d["R_2_{0}".format(i)] = regression.score(Data, Target)

    print(i)
    print(d["R_2_{0}".format(i)])

    df = df.append({
        'Price Type Estimated': i,
        'R-Squared Score': d["R_2_{0}".format(i)],
        }, ignore_index=True)

print(df)
