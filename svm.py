# THIS IS THE MAIN FILE FOR THE SVM MODEL.

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from pathlib import Path
from sklearn.svm import SVC

##############################################################
## READING IN TRAINING DATA THAT HAS BEEN PREVIOSLY CLEANED ##
##############################################################

# Creating two empty lists that are used to store the data that is read in.
x_train_list = []
y_train_list = []
# Iterating through the data for all the years.
for i in range(2000, 2021):
    # We ignore the year of 2004, as there seems to me something wrong with the formatting of the data in out dataset.
    if i != 2004:
        # Assembling in the name of the file that contains the x data that needs to be trained.
        file_name = "season_stats/east" + str(i) + ".csv"
         # Reading the x data from the filename created above.
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

print("Support Vector Machine Model for the 2021 NBA season in the Eastern Conference")

east_logreg = LogisticRegression()
east_logreg.fit(x_train, y_train)

east_svm = SVC(kernel="linear", probability=True)
east_svm.fit(x_train, y_train)

east_svm_train_score = east_svm.score(x_train, y_train)
print("Score for training data: " + str(east_svm_train_score))
east_svm_test_score = east_svm.score(x_test, y_test)
print("Score for testing data: " + str(east_svm_test_score))
print()

train_feature_names = x_train.columns

print("Most important features for 2021 in the Eastern Conference")
print()
coefficient_svm = east_svm.coef_
importance_svm = coefficient_svm[0]
abs_importance_svm = abs(importance_svm)
importance_list_svm = list(zip(train_feature_names, importance_svm, abs_importance_svm))
importance_list_svm.sort(key=lambda x: x[2], reverse=True)
for i in range(5):
    print(importance_list_svm[i])
print()

print("Predictions for which teams makes the playoffs for 2021 in the Eastern Conference")
print()
east_predictions_2021 = y_test_prediction[["TEAM", "PLAYOFF"]]
svm_probability = east_svm.predict_proba(x_test)[:, 1].tolist()
svm_prediction = east_svm.predict(x_test).tolist()
east_predictions_2021["PREDICTION"] = svm_prediction
east_predictions_2021["PROBABILITY"] = svm_probability
east_predictions_2021 = east_predictions_2021.sort_values("PROBABILITY", ascending=False)

print(east_predictions_2021)
