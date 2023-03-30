# THIS IS THE MAIN FILE USED TO CREATE ALL THE MODELS THAT WE ARE THINKING TO USE.
# We have so far implemented two models: Logistic Regression and SVM.

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from pathlib import Path
from sklearn.svm import SVC

#####################################################
## TRAINED MODELS FOR PREDICTING THE 2022 PLAYOFFS ##
#####################################################


#####################################################
## PREDICTING THE 2022 EASTERN CONFERENCE PLAYOFFS ##
######################################################


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
        # Sorting the data according to the values in the TEAM column.
        df_x = df_x.sort_values("TEAM")
        # Resetting the index of the data.
        df_x = df_x.reset_index()
        # Dropping the TEAM column in the data.
        df_x = df_x.drop("TEAM", axis=1)
        # Dropping the extra index column in the data.
        df_x = df_x.drop("index", axis=1)
        # Appending the current round of data to the overall list holding all the x data.
        x_train_list.append(df_x)
        # Assembling in the name of the file that contains the y data that needs to be trained.
        file_name = "playoff_labels/east" + str(i) + "playoff.csv"
        # Reading the y data from the filename created above.
        df_y = pd.read_csv(file_name, index_col=0)
        # Sorting the data according to the values in the TEAM column.
        df_y = df_y.sort_values("TEAM")
        # Resetting the index of the data.
        df_y = df_y.reset_index()
        # Dropping the TEAM column in the data.
        df_y = df_y.drop("TEAM", axis=1)
        # Dropping the extra index column in the data.
        df_y = df_y.drop("index", axis=1)
        # Appending the current round of data to the overall list holding all the y data.
        y_train_list.append(df_y)

# Concatentating the list of x data to a dataframe to hold all the x data.
x_train = pd.concat(x_train_list)
# Concatentating the list of y data to a dataframe to hold all the y data.
y_train = pd.concat(y_train_list)

##############################
## READING IN THE TEST DATA ##
##############################

# Assembling in the name of the file that contains the x data that needs to be tested against.
x_test = pd.read_csv("season_stats/east2022.csv", index_col=0)
# Sorting the data according to the values in the TEAM column.
x_test = x_test.sort_values("TEAM")
# Resetting the index of the data.
x_test = x_test.reset_index()
# Dropping the extra index column in the data.
x_test = x_test.drop("index", axis=1)
# Assigning the test data to a variable that tells us that this is the prediction that should be made.
x_test_prediction = x_test
# Dropping the TEAM column in the data.
x_test = x_test.drop("TEAM", axis=1)
# Assembling in the name of the file that contains the y data that needs to be tested against.
y_test = pd.read_csv("playoff_labels/east2022playoff.csv", index_col=0)
# Sorting the data according to the values in the TEAM column.
y_test = y_test.sort_values("TEAM")
# Resetting the index of the data.
y_test = y_test.reset_index()
# Dropping the extra index column in the data.
y_test = y_test.drop("index", axis=1)
# Assigning the test data to a variable that tells us that this is the prediction that should be made.
y_test_prediction = y_test
# Dropping the TEAM column in the data.
y_test = y_test.drop("TEAM", axis=1)

##############################
## STANDARDIZING THE X DATA ##
##############################
# Creating a scaler object.
sc = StandardScaler()
# Scaling the x training data.
x_train_scaled = sc.fit_transform(x_train)
# Scaling the x test data.
x_test_scaled = sc.transform(x_test)

############################
## NORMALIZING THE X DATA ##
############################
# Normalizing the x scaled training data.
a = preprocessing.normalize(x_train_scaled, axis = 0)
# Creating a new dataframe to hold the saled, normalized x training data.
x_train_normalized = pd.DataFrame(a, columns = x_train.columns)
# Normalizing the x scaled testing data.
b = preprocessing.normalize(x_test_scaled, axis = 0)
# Creating a new dataframe to hold the saled, normalized x testing data.
x_test_normalized = pd. DataFrame (b, columns = x_test.columns)

#######################################
## USING TRAIN_TEST_SPLIT IN SKLEARN ##
#######################################

# We used this to check if the training and testing data that would be given us may lead to different results using out algorithm.
# xTrain, yTrain, xTest, yTest = train_test_split(y_train, x_train, test_size = 0.40, random_state = 30)

###############################
## LOGISTIC REGRESSION MODEL ##
###############################

print("LOGISTIC REGRESSION MODEL FOR THE 2022 NBA SEASON IN THE EASTERN CONFERENCE")
print()
# Creating a logistic regression object.
east_logreg = LogisticRegression()
# Fitting the model with the normalized x training and y training data.
east_logreg.fit(x_train_normalized, np.ravel(y_train))
# Getting the score from the normalized x training and y trianing data.
east_logreg_train_score = east_logreg.score(x_train_normalized, y_train)
# Printing out this score.
print("Score for training data: " + str(east_logreg_train_score))
# Getting the score from the normalized x testing and y testing data.
east_logreg_test_score = east_logreg.score(x_test_normalized, y_test)
# Printing out this score.
print("Score for testing data: " + str(east_logreg_test_score))
print()
# Getting the names of the columns in the x training dataset.
train_feature_names = x_train.columns
print("Most important features for 2022 in the Eastern Conference")
# Calculating the coeffeicnt for the logistic regression model.
coefficient_logreg = east_logreg.coef_
# Getting the most important coefficient value which would be the first one in the list.
importance_logreg = coefficient_logreg[0]
# Taking the absolute value of this coeffficient.
abs_importance_logreg = abs(importance_logreg)
# Making a list of the feature names, the importance coeffeicient and the absolute value of this coefficient.
importance_list_log = list(zip(train_feature_names, importance_logreg, abs_importance_logreg))
# Sorting this list according to the absolute values of the coefficient.
importance_list_log.sort(key=lambda x: x[2], reverse=True)
for i in range(5):
    print(importance_list_log[i])
print()
print("Predictions for which teams makes the playoffs for 2022 in the Eastern Conference")
# Getting the teams and whether they made it to the playoffs in our testing data. This will be the prediction that we would like to match.
east_predictions_2022_LR = y_test_prediction[["TEAM", "PLAYOFF"]]
# Getting the probability of this predction, using the x data.
logreg_probability = east_logreg.predict_proba(x_test_normalized)[:, 1].tolist()
# Making a new predcition.
logreg_prediction = east_logreg.predict(x_test_normalized).tolist()
# Assigning the prediction value to the prediciotn column in the list.
east_predictions_2022_LR["PREDICTION"] = logreg_prediction
# Assigning the probabilities to the column in the list.
east_predictions_2022_LR["PROBABILITY"] = logreg_probability
# Sorting the list according to the porbability values.
east_predictions_2022_LR = east_predictions_2022_LR.sort_values("PROBABILITY", ascending=False)
print(east_predictions_2022_LR)
print()
print()

###############
## SVM MODEL ##
###############

print("SVM MODEL FOR THE 2022 NBA SEASON IN THE EASTERN CONFERENCE")
print()
# Making SVM model.
east_svm = SVC(kernel="linear", probability=True)
# Fitting the data to the model.
east_svm.fit(x_train_normalized, np.ravel(y_train))
# Calculating the score from the x and y training data.
east_svm_train_score = east_svm.score(x_train_normalized, y_train)
# Printing the score for the training data.
print("Score for training data: " + str(east_svm_train_score))
# Printing the score for the test data.
east_svm_test_score = east_svm.score(x_test, y_test)
# Printing the score for the training data.
print("Score for testing data: " + str(east_svm_test_score))
print()
# Getting the names of the columns in the x training dataset.
train_feature_names_SVM = x_train.columns
print("Most important features for 2022 in the Eastern Conference")
# Calculating the coefficient for the SVM.
coefficient_svm = east_svm.coef_
# Getting the most important coefficient value which would be the first one in the list.
importance_svm = coefficient_svm[0]
# Taking the absolute value of this coeffficient.
abs_importance_svm = abs(importance_svm)
# Making a list of the feature names, the importance coeffeicient and the absolute value of this coefficient.
importance_list_svm = list(zip(train_feature_names_SVM, importance_svm, abs_importance_svm))
# Sorting this list according to the absolute values of the coefficient.
importance_list_svm.sort(key=lambda x: x[2], reverse=True)
for i in range(5):
    print(importance_list_svm[i])
print()
print("Predictions for which teams makes the playoffs for 2022 in the Eastern Conference")
# Getting the teams and whether they made it to the playoffs in our testing data. This will be the prediction that we would like to match.
east_predictions_2022_SVM = y_test_prediction[["TEAM", "PLAYOFF"]]
# Getting the probability of this predction, using the x data.
svm_probability = east_svm.predict_proba(x_test_normalized)[:, 1].tolist()
# Making a new predcition.
svm_prediction = east_svm.predict(x_test_normalized).tolist()
# Assigning the prediction value to the prediciotn colum in the list.
east_predictions_2022_SVM["PREDICTION"] = svm_prediction
# Assigning the probabilities to the column in the list.
east_predictions_2022_SVM["PROBABILITY"] = svm_probability
# Sorting the list according to the porbability values.
east_predictions_2022_SVM = east_predictions_2022_SVM.sort_values("PROBABILITY", ascending=False)
print(east_predictions_2022_SVM)




#####################################################
## PREDICTING THE 2022 WESTERN CONFERENCE PLAYOFFS ##
######################################################


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
        file_name = "season_stats/west" + str(i) + ".csv"
        # Reading the x data from the filename created above.
        df_x = pd.read_csv(file_name, index_col=0)
        # Sorting the data according to the values in the TEAM column.
        df_x = df_x.sort_values("TEAM")
        # Resetting the index of the data.
        df_x = df_x.reset_index()
        # Dropping the TEAM column in the data.
        df_x = df_x.drop("TEAM", axis=1)
        # Dropping the extra index column in the data.
        df_x = df_x.drop("index", axis=1)
        # Appending the current round of data to the overall list holding all the x data.
        x_train_list.append(df_x)
        # Assembling in the name of the file that contains the y data that needs to be trained.
        file_name = "playoff_labels/west" + str(i) + "playoff.csv"
        # Reading the y data from the filename created above.
        df_y = pd.read_csv(file_name, index_col=0)
        # Sorting the data according to the values in the TEAM column.
        df_y = df_y.sort_values("TEAM")
        # Resetting the index of the data.
        df_y = df_y.reset_index()
        # Dropping the TEAM column in the data.
        df_y = df_y.drop("TEAM", axis=1)
        # Dropping the extra index column in the data.
        df_y = df_y.drop("index", axis=1)
        # Appending the current round of data to the overall list holding all the y data.
        y_train_list.append(df_y)

# Concatentating the list of x data to a dataframe to hold all the x data.
x_train = pd.concat(x_train_list)
# Concatentating the list of y data to a dataframe to hold all the y data.
y_train = pd.concat(y_train_list)

##############################
## READING IN THE TEST DATA ##
##############################

# Assembling in the name of the file that contains the x data that needs to be tested against.
x_test = pd.read_csv("season_stats/west2022.csv", index_col=0)
# Sorting the data according to the values in the TEAM column.
x_test = x_test.sort_values("TEAM")
# Resetting the index of the data.
x_test = x_test.reset_index()
# Dropping the extra index column in the data.
x_test = x_test.drop("index", axis=1)
# Assigning the test data to a variable that tells us that this is the prediction that should be made.
x_test_prediction = x_test
# Dropping the TEAM column in the data.
x_test = x_test.drop("TEAM", axis=1)
# Assembling in the name of the file that contains the y data that needs to be tested against.
y_test = pd.read_csv("playoff_labels/west2022playoff.csv", index_col=0)
# Sorting the data according to the values in the TEAM column.
y_test = y_test.sort_values("TEAM")
# Resetting the index of the data.
y_test = y_test.reset_index()
# Dropping the extra index column in the data.
y_test = y_test.drop("index", axis=1)
# Assigning the test data to a variable that tells us that this is the prediction that should be made.
y_test_prediction = y_test
# Dropping the TEAM column in the data.
y_test = y_test.drop("TEAM", axis=1)

##############################
## STANDARDIZING THE X DATA ##
##############################
# Creating a scaler object.
sc = StandardScaler()
# Scaling the x training data.
x_train_scaled = sc.fit_transform(x_train)
# Scaling the x test data.
x_test_scaled = sc.transform(x_test)

############################
## NORMALIZING THE X DATA ##
############################
# Normalizing the x scaled training data.
a = preprocessing.normalize(x_train_scaled, axis = 0)
# Creating a new dataframe to hold the saled, normalized x training data.
x_train_normalized = pd.DataFrame(a, columns = x_train.columns)
# Normalizing the x scaled testing data.
b = preprocessing.normalize(x_test_scaled, axis = 0)
# Creating a new dataframe to hold the saled, normalized x testing data.
x_test_normalized = pd. DataFrame (b, columns = x_test.columns)

#######################################
## USING TRAIN_TEST_SPLIT IN SKLEARN ##
#######################################

# We used this to check if the training and testing data that would be given us may lead to different results using out algorithm.
# xTrain, yTrain, xTest, yTest = train_test_split(y_train, x_train, test_size = 0.40, random_state = 30)

###############################
## LOGISTIC REGRESSION MODEL ##
###############################

print("LOGISTIC REGRESSION MODEL FOR THE 2022 NBA SEASON IN THE WESTERN CONFERENCE")
print()
# Creating a logistic regression object.
west_logreg = LogisticRegression()
# Fitting the model with the normalized x training and y training data.
west_logreg.fit(x_train_normalized, np.ravel(y_train))
# Getting the score from the normalized x training and y trianing data.
west_logreg_train_score = west_logreg.score(x_train_normalized, y_train)
# Printing out this score.
print("Score for training data: " + str(west_logreg_train_score))
# Getting the score from the normalized x testing and y testing data.
west_logreg_test_score = west_logreg.score(x_test_normalized, y_test)
# Printing out this score.
print("Score for testing data: " + str(west_logreg_test_score))
print()
# Getting the names of the columns in the x training dataset.
train_feature_names = x_train.columns
print("Most important features for 2022 in the Western Conference")
# Calculating the coeffeicnt for the logistic regression model.
coefficient_logreg = west_logreg.coef_
# Getting the most important coefficient value which would be the first one in the list.
importance_logreg = coefficient_logreg[0]
# Taking the absolute value of this coeffficient.
abs_importance_logreg = abs(importance_logreg)
# Making a list of the feature names, the importance coeffeicient and the absolute value of this coefficient.
importance_list_log = list(zip(train_feature_names, importance_logreg, abs_importance_logreg))
# Sorting this list according to the absolute values of the coefficient.
importance_list_log.sort(key=lambda x: x[2], reverse=True)
for i in range(5):
    print(importance_list_log[i])
print()
print("Predictions for which teams makes the playoffs for 2022 in the Western Conference")
# Getting the teams and whether they made it to the playoffs in our testing data. This will be the prediction that we would like to match.
west_predictions_2022_LR = y_test_prediction[["TEAM", "PLAYOFF"]]
# Getting the probability of this predction, using the x data.
logreg_probability = west_logreg.predict_proba(x_test_normalized)[:, 1].tolist()
# Making a new predcition.
logreg_prediction = west_logreg.predict(x_test_normalized).tolist()
# Assigning the prediction value to the prediciotn column in the list.
west_predictions_2022_LR["PREDICTION"] = logreg_prediction
# Assigning the probabilities to the column in the list.
west_predictions_2022_LR["PROBABILITY"] = logreg_probability
# Sorting the list according to the porbability values.
west_predictions_2022_LR = west_predictions_2022_LR.sort_values("PROBABILITY", ascending=False)
print(west_predictions_2022_LR)
print()
print()

###############
## SVM MODEL ##
###############

print("SVM MODEL FOR THE 2022 NBA SEASON IN THE WESTERN CONFERENCE")
print()
# Making SVM model.
west_svm = SVC(kernel="linear", probability=True)
# Fitting the data to the model.
west_svm.fit(x_train_normalized, np.ravel(y_train))
# Calculating the score from the x and y training data.
west_svm_train_score = west_svm.score(x_train_normalized, y_train)
# Printing the score for the training data.
print("Score for training data: " + str(west_svm_train_score))
# Printing the score for the test data.
west_svm_test_score = west_svm.score(x_test, y_test)
# Printing the score for the training data.
print("Score for testing data: " + str(west_svm_test_score))
print()
# Getting the names of the columns in the x training dataset.
train_feature_names_SVM = x_train.columns
print("Most important features for 2022 in the Western Conference")
# Calculating the coefficient for the SVM.
coefficient_svm = west_svm.coef_
# Getting the most important coefficient value which would be the first one in the list.
importance_svm = coefficient_svm[0]
# Taking the absolute value of this coeffficient.
abs_importance_svm = abs(importance_svm)
# Making a list of the feature names, the importance coeffeicient and the absolute value of this coefficient.
importance_list_svm = list(zip(train_feature_names_SVM, importance_svm, abs_importance_svm))
# Sorting this list according to the absolute values of the coefficient.
importance_list_svm.sort(key=lambda x: x[2], reverse=True)
for i in range(5):
    print(importance_list_svm[i])
print()
print("Predictions for which teams makes the playoffs for 2022 in the Western Conference")
# Getting the teams and whether they made it to the playoffs in our testing data. This will be the prediction that we would like to match.
west_predictions_2022_SVM = y_test_prediction[["TEAM", "PLAYOFF"]]
# Getting the probability of this predction, using the x data.
svm_probability = west_svm.predict_proba(x_test_normalized)[:, 1].tolist()
# Making a new predcition.
svm_prediction = west_svm.predict(x_test_normalized).tolist()
# Assigning the prediction value to the prediction column in the list.
west_predictions_2022_SVM["PREDICTION"] = svm_prediction
# Assigning the probabilities to the column in the list.
west_predictions_2022_SVM["PROBABILITY"] = svm_probability
# Sorting the list according to the probability values.
west_predictions_2022_SVM = west_predictions_2022_SVM.sort_values("PROBABILITY", ascending=False)
print(west_predictions_2022_SVM)
