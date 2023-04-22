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
eastStats = pd.read_csv('season_stats_2000to2022/eastTrainingData.csv', index_col=None)
# Getting the name of all the columns in the dataframe. 
eastColumnNames = eastStats.columns
# Dropping the first column of the dataframe as it is not useful to us. 
eastStats = eastStats.drop('Unnamed: 0.1', axis = 1)
# Dropping the first column of the dataframe as  again it is not useful to us. 
eastStats = eastStats.drop('Unnamed: 0', axis = 1)
# Dropping the team name column as well, as this will not be used in the matrix. 
eastStats = eastStats.drop('TEAM', axis = 1) 

#########################################
## WEST CONFERENCE TRAINING DATA STATS ##
#########################################

# Loading the eastTrainingData.csv into a pandas dataframe
westStats = pd.read_csv('season_stats_2000to2022/westTrainingData.csv', index_col=None)
# Getting the name of all the columns in the dataframe. 
westColumnNames = westStats.columns
# Dropping the first column of the dataframe as it is not useful to us. 
westStats = westStats.drop('Unnamed: 0.1', axis = 1)
# Dropping the first column of the dataframe as  again it is not useful to us. 
westStats = westStats.drop('Unnamed: 0', axis = 1)
# Dropping the team name column as well, as this will not be used in the matrix. 
westStats = westStats.drop('TEAM', axis = 1) 

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


