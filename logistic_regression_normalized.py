import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from pathlib import Path

from sklearn.preprocessing import QuantileTransformer, Normalizer

x_train_list = []
y_train_list = []

scaler = QuantileTransformer(output_distribution='normal')
normalizer = Normalizer()

for i in range(2000, 2001):
    if i != 2004:
        file_name = "season_stats/east" + str(i) + ".csv"
        df_x = pd.read_csv(file_name, index_col=0)
        df_x = df_x.sort_values("TEAM")
        df_x = df_x.reset_index()
        # print(df_x.head())
        df_x = df_x.drop("TEAM", axis=1)
        df_x = df_x.drop("index", axis=1)
        # print(df_x.head())
        df_x_scaled = pd.DataFrame(scaler.fit_transform(df_x), columns=df_x.columns)
        df_x_normalized = pd.DataFrame(normalizer.fit_transform(df_x_scaled), columns=df_x_scaled.columns)
        # print(df_x_normalized.head())

        x_train_list.append(df_x_normalized)

        file_name = "playoff_labels/east" + str(i) + "playoff.csv"
        df_y = pd.read_csv(file_name, index_col=0)
        df_y = df_y.sort_values("TEAM")
        # if i == 2002 or i == 2003:
        #     df_y = df_y.loc[df_y["TEAM"] != "CHA"]
        df_y = df_y.reset_index()
        df_y = df_y.drop("TEAM", axis=1)
        df_y = df_y.drop("index", axis=1)
        df_y_scaled = pd.DataFrame(scaler.fit_transform(df_y), columns=df_y.columns)
        df_y_normalized = pd.DataFrame(normalizer.fit_transform(df_y_scaled), columns=df_y_scaled.columns)
        y_train_list.append(df_y_normalized)

x_train = pd.concat(x_train_list)
y_train = pd.concat(y_train_list)

x_test = pd.read_csv("season_stats/east2021.csv", index_col=0)
x_test = x_test.sort_values("TEAM")
x_test = x_test.reset_index()
x_test = x_test.drop("index", axis=1)
x_test_prediction = x_test
x_test = x_test.drop("TEAM", axis=1)

y_test = pd.read_csv("playoff_labels/east2021playoff.csv", index_col=0)
y_test = y_test.sort_values("TEAM")
y_test = y_test.reset_index()
y_test = y_test.drop("index", axis=1)
y_test_prediction = y_test
y_test = y_test.drop("TEAM", axis=1)

# print(x_train.columns)
# print(x_test.columns)
#
# print(y_train.columns)
# print(y_test.columns)
#
# scaler = QuantileTransformer(output_distribution='normal')
# normalizer = Normalizer()

# scaled_df = pd.DataFrame(scaler.fit_transform(change_df), columns=change_df.columns)
# normalized_df = pd.DataFrame(normalizer.fit_transform(scaled_df), columns=scaled_df.columns)


east_logreg = LogisticRegression()
east_logreg.fit(x_train, y_train)

east_logreg_train_score = east_logreg.score(x_train, y_train)
east_logreg_test_score = east_logreg.score(x_test, y_test)
#
print("Score for training data: " + str(east_logreg_train_score))
print("Score for testing data: " + str(east_logreg_test_score))

train_feature_names = x_train.columns

print("Logistic Regression - East")
coefficient_logreg = east_logreg.coef_
importance_logreg = coefficient_logreg[0]
abs_importance_logreg = abs(importance_logreg)
importance_list_log = list(zip(train_feature_names, importance_logreg, abs_importance_logreg))
importance_list_log.sort(key=lambda x: x[2], reverse=True)
for i in range(5):
    print(importance_list_log[i])

east_predictions_2021 = y_test_prediction[["TEAM", "PLAYOFF"]]
logreg_probability = east_logreg.predict_proba(x_test)[:, 1].tolist()
logreg_prediction = east_logreg.predict(x_test).tolist()
east_predictions_2021["PREDICTION"] = logreg_prediction
east_predictions_2021["PROBABILITY"] = logreg_probability
east_predictions_2021 = east_predictions_2021.sort_values("PROBABILITY", ascending=False)
print(east_predictions_2021)
