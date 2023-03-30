import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from pathlib import Path

x_train_list = []
y_train_list = []

for i in range(2000, 2021):
    if i != 2004:
        file_name = "season_stats/east" + str(i) + ".csv"
        df_x = pd.read_csv(file_name, index_col=0)
        df_x = df_x.sort_values("TEAM")
        df_x = df_x.reset_index()
        df_x = df_x.drop("TEAM", axis=1)
        df_x = df_x.drop("index", axis=1)
        x_train_list.append(df_x)

        file_name = "playoff_labels/east" + str(i) + "playoff.csv"
        df_y = pd.read_csv(file_name, index_col=0)
        df_y = df_y.sort_values("TEAM")
        # if i == 2002 or i == 2003:
        #     df_y = df_y.loc[df_y["TEAM"] != "CHA"]
        df_y = df_y.reset_index()
        df_y = df_y.drop("TEAM", axis=1)
        df_y = df_y.drop("index", axis=1)
        y_train_list.append(df_y)

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

##############################
## STANDARDIZING THE X DATA ##
##############################
sc = StandardScaler()
x_train_scaled = sc.fit_transform(x_train)
x_test_scaled = sc.transform(x_test)

############################
## NORMALIZING THE X DATA ##
############################
a = preprocessing.normalize(x_train_scaled, axis = 0)
x_train_normalized = pd.DataFrame(a, columns = x_train.columns)

b = preprocessing.normalize(x_test_scaled, axis = 0)
x_test_normalized = pd. DataFrame (b, columns = x_test.columns)

#######################################
## USING TRAIN_TEST_SPLIT IN SKLEARN ##
#######################################

xTrain, yTrain, xTest, yTest = train_test_split(y_train, x_train, test_size = 0.40, random_state = 30)
print("This is xTrain")
print(xTrain)
print()
print("This is xTest")
print(xTest)
print()
print("This is yTrain")
print(yTrain)
print()
print("This is yTest")
print(yTest)
print()

###############################
## LOGISTIC REGRESSION MODEL ##
###############################

print("Logistic Regression Model for the 2021 NBA season in the Eastern Conference")

east_logreg = LogisticRegression()
east_logreg.fit(xTrain, yTrain)

east_logreg_train_score = east_logreg.score(xTrain, yTrain)
print("Score for training data: " + str(east_logreg_train_score))
east_logreg_test_score = east_logreg.score(xTest, yTest)
print("Score for testing data: " + str(east_logreg_test_score))
print()

train_feature_names = x_train.columns

print("Most important features for 2021 in the Eastern Conference")
print()
coefficient_logreg = east_logreg.coef_
importance_logreg = coefficient_logreg[0]
abs_importance_logreg = abs(importance_logreg)
importance_list_log = list(zip(train_feature_names, importance_logreg, abs_importance_logreg))
importance_list_log.sort(key=lambda x: x[2], reverse=True)
for i in range(5):
    print(importance_list_log[i])
print()

print("Predictions for which teams makes the playoffs for 2021 in the Eastern Conference")
print()
east_predictions_2021 = y_test_prediction[["TEAM", "PLAYOFF"]]
logreg_probability = east_logreg.predict_proba(xTest)[:, 1].tolist()
logreg_prediction = east_logreg.predict(xTest).tolist()
east_predictions_2021["PREDICTION"] = logreg_prediction
east_predictions_2021["PROBABILITY"] = logreg_probability
east_predictions_2021 = east_predictions_2021.sort_values("PROBABILITY", ascending=False)

print(east_predictions_2021)
