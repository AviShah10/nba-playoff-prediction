# THIS FILE IS USED TO PRODUCE THE CORRELATION MATRIX. 
# The correlation matrix is used to find the most important features in a project.
# This helps us better understand which features to focus on while creating our models. 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#########################################
## EAST CONFERENCE TRAINING DATA STATS ##
#########################################

# Loading the eastTrainingData.csv into a pandas dataframe
eastStats1 = pd.read_csv('./results/stats_east.csv', index_col=None)
eastPlayoff = pd.read_csv("./results/playoff_east.csv", index_col=None)
eastStats = pd.concat([eastStats1, eastPlayoff], axis=1)
# Getting the name of all the columns in the dataframe. 
eastColumnNames = eastStats.columns

#########################################
## WEST CONFERENCE TRAINING DATA STATS ##
#########################################

# Loading the eastTrainingData.csv into a pandas dataframe
westStats1 = pd.read_csv('./results/stats_west.csv', index_col=None)
westPlayoff = pd.read_csv("./results/playoff_west.csv", index_col=None)
westStats = pd.concat([westStats1, westPlayoff], axis=1)
# Getting the name of all the columns in the dataframe. 
westColumnNames = westStats.columns

#################################
## OVERALL TRAINING DATA STATS ##
#################################

# Combining the east and west training data stats into one dataframe.
overallStats = pd.concat([eastStats, westStats])

####################################################
## CALCULATING THE VISUALIZING CORRELATION MATRIX ##
####################################################

# Calculating the correlation coefficient. 
corr = overallStats.corr()
# Setting the plot size. 
plt.figure(figsize=(30,8.75))
# Plotting the correlation matrix with the values.
sns.heatmap(corr, annot=True, cmap = 'coolwarm')
# Saving the plot to a jpeg image. 
plt.savefig('correlation_matrix.jpeg')


