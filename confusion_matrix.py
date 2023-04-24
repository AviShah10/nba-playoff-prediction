# THIS FILE IS GOING TO CREATE THE CONFUSION MATRIX FOR VARIOUS MODELS.
import pandas as pd
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# We are going to create the confusion matrices for each model. Thus we are going to have 4 overall confusion matrices. 
# The way we are going to do this is we are going to make the confusion matrix for each model, for each year, for ewach conference, and then add them all together up. 
# This will give us the overall confusion matrix for that model. 

#########################
## LOGISTIC REGRESSION ##
#########################
# Reading in all the data
east_2021_LR = pd.read_pickle("./results/east_predictions_2021_LR")
west_2021_LR = pd.read_pickle("./results/west_predictions_2021_LR")
east_2022_LR = pd.read_pickle("./results/east_predictions_2022_LR")
west_2022_LR = pd.read_pickle("./results/west_predictions_2022_LR")
# Getting the known thruth values from the dataframes loaded above. 
east_2021_LR_KT = east_2021_LR['PLAYOFF']
west_2021_LR_KT = west_2021_LR['PLAYOFF']
east_2022_LR_KT = east_2022_LR['PLAYOFF']
west_2022_LR_KT = west_2022_LR['PLAYOFF']
# Getting the prediction from the dataframes above. 
east_2021_LR_Pred = east_2021_LR['PREDICTION']
west_2021_LR_Pred = west_2021_LR['PREDICTION']
east_2022_LR_Pred = east_2022_LR['PREDICTION']
west_2022_LR_Pred = east_2022_LR['PREDICTION']
# Creating the confusion matrices for each year
east_2021_LR_cm = confusion_matrix(east_2021_LR_KT, east_2021_LR_Pred)
west_2021_LR_cm = confusion_matrix(west_2021_LR_KT, west_2021_LR_Pred)
east_2022_LR_cm = confusion_matrix(east_2022_LR_KT, east_2022_LR_Pred)
west_2022_LR_cm = confusion_matrix(west_2022_LR_KT, west_2022_LR_Pred)
# Creating the final confusion matrix for the logistic regression model. 
LR_cm = east_2021_LR_cm + west_2021_LR_cm + east_2022_LR_cm + west_2022_LR_cm
# Creating a visualisation for the confusion matrix for the model. 
sns.heatmap(LR_cm, annot=True, cmap="Blues")
plt.title("Confusion Matrix for Logistic Rgression Model (2021 & 2022)")
plt.savefig("./confusion_matrix/LR_cm.jpeg")
plt.show()

#########
## SVM ##
#########
# Reading in all the data
east_2021_SVM = pd.read_pickle("./results/east_predictions_2021_SVM")
west_2021_SVM = pd.read_pickle("./results/west_predictions_2021_SVM")
east_2022_SVM = pd.read_pickle("./results/east_predictions_2022_SVM")
west_2022_SVM = pd.read_pickle("./results/west_predictions_2022_SVM")
# Getting the known thruth values from the dataframes loaded above. 
east_2021_SVM_KT = east_2021_SVM['PLAYOFF']
west_2021_SVM_KT = west_2021_SVM['PLAYOFF']
east_2022_SVM_KT = east_2022_SVM['PLAYOFF']
west_2022_SVM_KT = west_2022_SVM['PLAYOFF']
# Getting the prediction from the dataframes above. 
east_2021_SVM_Pred = east_2021_SVM['PREDICTION']
west_2021_SVM_Pred = west_2021_SVM['PREDICTION']
east_2022_SVM_Pred = east_2022_SVM['PREDICTION']
west_2022_SVM_Pred = east_2022_SVM['PREDICTION']
# Creating the confusion matrices for each year
east_2021_SVM_cm = confusion_matrix(east_2021_SVM_KT, east_2021_SVM_Pred)
west_2021_SVM_cm = confusion_matrix(west_2021_SVM_KT, west_2021_SVM_Pred)
east_2022_SVM_cm = confusion_matrix(east_2022_SVM_KT, east_2022_SVM_Pred)
west_2022_SVM_cm = confusion_matrix(west_2022_SVM_KT, west_2022_SVM_Pred)
# Creating the final confusion matrix for the logistic regression model. 
SVM_cm = east_2021_SVM_cm + west_2021_SVM_cm + east_2022_SVM_cm + west_2022_SVM_cm
# Creating a visualisation for the confusion matrix for the model. 
sns.heatmap(SVM_cm, annot=True, cmap="Reds")
plt.title("Confusion Matrix for SVM Model (2021 & 2022)")
plt.savefig("./confusion_matrix/SVM_cm.jpeg")
plt.show()

###################
## RANDOM FOREST ##
###################
# Reading in all the data
east_2021_RF = pd.read_pickle("./results/east_predictions_2021_RF")
west_2021_RF = pd.read_pickle("./results/west_predictions_2021_RF")
east_2022_RF = pd.read_pickle("./results/east_predictions_2022_RF")
west_2022_RF = pd.read_pickle("./results/west_predictions_2022_RF")
# Getting the known thruth values from the dataframes loaded above. 
east_2021_RF_KT = east_2021_RF['PLAYOFF']
west_2021_RF_KT = west_2021_RF['PLAYOFF']
east_2022_RF_KT = east_2022_RF['PLAYOFF']
west_2022_RF_KT = west_2022_RF['PLAYOFF']
# Getting the prediction from the dataframes above. 
east_2021_RF_Pred = east_2021_RF['PREDICTION']
west_2021_RF_Pred = west_2021_RF['PREDICTION']
east_2022_RF_Pred = east_2022_RF['PREDICTION']
west_2022_RF_Pred = east_2022_RF['PREDICTION']
# Creating the confusion matrices for each year
east_2021_RF_cm = confusion_matrix(east_2021_RF_KT, east_2021_RF_Pred)
west_2021_RF_cm = confusion_matrix(west_2021_RF_KT, west_2021_RF_Pred)
east_2022_RF_cm = confusion_matrix(east_2022_RF_KT, east_2022_RF_Pred)
west_2022_RF_cm = confusion_matrix(west_2022_RF_KT, west_2022_RF_Pred)
# Creating the final confusion matrix for the logistic regression model. 
RF_cm = east_2021_RF_cm + west_2021_RF_cm + east_2022_RF_cm + west_2022_RF_cm
# Creating a visualisation for the confusion matrix for the model. 
sns.heatmap(RF_cm, annot=True, cmap="Greens")
plt.title("Confusion Matrix for Random Forest Model (2021 & 2022)")
plt.savefig("./confusion_matrix/RF_cm.jpeg")
plt.show()

###################
## DECISION TREE ##
###################
# Reading in all the data
east_2021_DT = pd.read_pickle("./results/east_predictions_2021_DT")
west_2021_DT = pd.read_pickle("./results/west_predictions_2021_DT")
east_2022_DT = pd.read_pickle("./results/east_predictions_2022_DT")
west_2022_DT = pd.read_pickle("./results/west_predictions_2022_DT")
# Getting the known thruth values from the dataframes loaded above. 
east_2021_DT_KT = east_2021_DT['PLAYOFF']
west_2021_DT_KT = west_2021_DT['PLAYOFF']
east_2022_DT_KT = east_2022_DT['PLAYOFF']
west_2022_DT_KT = west_2022_DT['PLAYOFF']
# Getting the prediction from the dataframes above. 
east_2021_DT_Pred = east_2021_DT['PREDICTION']
west_2021_DT_Pred = west_2021_DT['PREDICTION']
east_2022_DT_Pred = east_2022_DT['PREDICTION']
west_2022_DT_Pred = east_2022_DT['PREDICTION']
# Creating the confusion matrices for each year
east_2021_DT_cm = confusion_matrix(east_2021_DT_KT, east_2021_DT_Pred)
west_2021_DT_cm = confusion_matrix(west_2021_DT_KT, west_2021_DT_Pred)
east_2022_DT_cm = confusion_matrix(east_2022_DT_KT, east_2022_DT_Pred)
west_2022_DT_cm = confusion_matrix(west_2022_DT_KT, west_2022_DT_Pred)
# Creating the final confusion matrix for the logistic regression model. 
DT_cm = east_2021_DT_cm + west_2021_DT_cm + east_2022_DT_cm + west_2022_DT_cm
# Creating a visualisation for the confusion matrix for the model. 
sns.heatmap(DT_cm, annot=True, cmap="PuBu")
plt.title("Confusion Matrix for Decision Tree Model (2021 & 2022)")
plt.savefig("./confusion_matrix/DT_cm.jpeg")
plt.show()


