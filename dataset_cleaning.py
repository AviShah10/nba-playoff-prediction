# This file is used to clean the Kaggle dataset. The dataset can be found here: https://www.kaggle.com/datasets/wyattowalsh/basketball/discussion.
# The format of the code is that of scripting, rather than having function calls.
# I datset has been downlaoded, and is in the file game2000.csv
# The plan is to do the following:
#   1. Load the dataset into a pandas dataset.
#   2. 

import pandas as pd
import os
import numpy as np

# recurant neural networks -- Look into this, we might have to implement this

#####################################
# LOADING THE DATA INTO A DATAFRAME #
#####################################

# This reads in the file called 'game.csv'
gamesDataframe = pd.read_csv('./game2000.csv')
# We then print the column names in the gamesDataFrame
gamesColumns = gamesDataframe.columns.values.tolist()
# print("The following columns are available in the dataset")
# print(columns)
# print("There are %d columns in the dataset. Each column represents a different statistic that we can use." % len(columns))
# print()

############################################################
# CHECKING FOR WHETHER THE COLUMNS HAVE NULL/EMPTY VALUES. #
############################################################

# We iterating through the columns in the dataset, and check if they contain data. If they do not, we print out the number of columsn that are empty.
emptyColumnsCount = 0
emptyColumnsList = []
for column in gamesColumns:
    if (gamesDataframe[column].isnull().values.any()):
        emptyColumnsCount += 1
        emptyColumnsList.append(column)
# print("Out of the %d columns in the dataset, %d have null/empty values that we may need to fill." % (len(columns), emptyColumnsCount))
# print("This is a list of all the column names that have null/empty values: ")
# print(emptyColumnsList)
# print()

#######################################################################################
# SPLITTTING THE DATASET BY YEAR. MAKING SEPARATE DATESET FOR ALL TEAMS FOR EACH YEAR #
#######################################################################################

# THIS IS THE FIRST WAY THAT WE COULD SPLIT THE DATASET. THIS WOULD CONTAIN DATA FOR ALL TEAMS BY YEARS.

# # Looking at the game date colum for this process
# dateColumn = gamesDataframe['game_date']
# # Creating the dataframes that would hold the data for each respective year.
# dataset2000 = pd.DataFrame(columns=gamesColumns)
# dataset2001 = pd.DataFrame(columns=gamesColumns)
# dataset2002 = pd.DataFrame(columns=gamesColumns)
# dataset2003 = pd.DataFrame(columns=gamesColumns)
# dataset2004 = pd.DataFrame(columns=gamesColumns)
# dataset2005 = pd.DataFrame(columns=gamesColumns)
# dataset2006 = pd.DataFrame(columns=gamesColumns)
# dataset2007 = pd.DataFrame(columns=gamesColumns)
# dataset2008 = pd.DataFrame(columns=gamesColumns)
# dataset2009 = pd.DataFrame(columns=gamesColumns)
# dataset2010 = pd.DataFrame(columns=gamesColumns)
# dataset2011 = pd.DataFrame(columns=gamesColumns)
# dataset2012 = pd.DataFrame(columns=gamesColumns)
# dataset2013 = pd.DataFrame(columns=gamesColumns)
# dataset2014 = pd.DataFrame(columns=gamesColumns)
# dataset2015 = pd.DataFrame(columns=gamesColumns)
# dataset2016 = pd.DataFrame(columns=gamesColumns)
# dataset2017 = pd.DataFrame(columns=gamesColumns)
# dataset2018 = pd.DataFrame(columns=gamesColumns)
# dataset2019 = pd.DataFrame(columns=gamesColumns)
# # Declaring a dictionary to count the number of games in each year.
# countDictionary = {}
# # Iterating through the dataframe and adding each game to the respective year dataset.
# for i, date in enumerate(dateColumn):
#     # You check if the date for a particular game is equal to a sepcific year.
#     # You then move the row to the dataframe for that specific year.
#     # You increment the count in the dictionary, or you create a new key in the dictionary with a value of 1.
#     if (date[5:9] == '2000' or date[6:10] == '2000'):
#         dataset2000.loc[i] = gamesDataframe.loc[i]
#         if '2000' in countDictionary:
#             countDictionary['2000'] += 1
#         else:
#             countDictionary['2000'] = 1
#     elif (date[5:9] == '2001' or date[6:10] == '2001'):
#         dataset2001.loc[i] = gamesDataframe.loc[i]
#         if '2001' in countDictionary:
#             countDictionary['2001'] += 1
#         else:
#             countDictionary['2001'] = 1
#     elif (date[5:9] == '2002' or date[6:10] == '2002'):
#         dataset2002.loc[i] = gamesDataframe.loc[i]
#         if '2002' in countDictionary:
#             countDictionary['2002'] += 1
#         else:
#             countDictionary['2002'] = 1
#     elif (date[5:9] == '2003' or date[6:10] == '2003'):
#         dataset2003.loc[i] = gamesDataframe.loc[i]
#         if '2003' in countDictionary:
#             countDictionary['2003'] += 1
#         else:
#             countDictionary['2003'] = 1
#     elif (date[5:9] == '2004' or date[6:10] == '2004'):
#         dataset2004.loc[i] = gamesDataframe.loc[i]
#         if '2004' in countDictionary:
#             countDictionary['2004'] += 1
#         else:
#             countDictionary['2004'] = 1
#     elif (date[5:9] == '2005' or date[6:10] == '2005'):
#         dataset2005.loc[i] = gamesDataframe.loc[i]
#         if '2005' in countDictionary:
#             countDictionary['2005'] += 1
#         else:
#             countDictionary['2005'] = 1
#     elif (date[5:9] == '2006' or date[6:10] == '2006'):
#         dataset2006.loc[i] = gamesDataframe.loc[i]
#         if '2006' in countDictionary:
#             countDictionary['2006'] += 1
#         else:
#             countDictionary['2006'] = 1
#     elif (date[5:9] == '2007' or date[6:10] == '2007'):
#         dataset2007.loc[i] = gamesDataframe.loc[i]
#         if '2007' in countDictionary:
#             countDictionary['2007'] += 1
#         else:
#             countDictionary['2007'] = 1
#     elif (date[5:9] == '2008' or date[6:10] == '2008'):
#         dataset2008.loc[i] = gamesDataframe.loc[i]
#         if '2008' in countDictionary:
#             countDictionary['2008'] += 1
#         else:
#             countDictionary['2008'] = 1
#     elif (date[5:9] == '2009' or date[6:10] == '2009'):
#         dataset2009.loc[i] = gamesDataframe.loc[i]
#         if '2009' in countDictionary:
#             countDictionary['2009'] += 1
#         else:
#             countDictionary['2009'] = 1
#     elif (date[5:9] == '2010' or date[6:10] == '2010'):
#         dataset2010.loc[i] = gamesDataframe.loc[i]
#         if '2010' in countDictionary:
#             countDictionary['2010'] += 1
#         else:
#             countDictionary['2010'] = 1
#     elif (date[5:9] == '2011' or date[6:10] == '2011'):
#         dataset2011.loc[i] = gamesDataframe.loc[i]
#         if '2011' in countDictionary:
#             countDictionary['2011'] += 1
#         else:
#             countDictionary['2011'] = 1
#     elif (date[5:9] == '2012' or date[6:10] == '2012'):
#         dataset2012.loc[i] = gamesDataframe.loc[i]
#         if '2012' in countDictionary:
#             countDictionary['2012'] += 1
#         else:
#             countDictionary['2012'] = 1
#     elif (date[5:9] == '2013' or date[6:10] == '2013'):
#         dataset2013.loc[i] = gamesDataframe.loc[i]
#         if '2013' in countDictionary:
#             countDictionary['2013'] += 1
#         else:
#             countDictionary['2013'] = 1
#     elif (date[5:9] == '2014' or date[6:10] == '2014'):
#         dataset2014.loc[i] = gamesDataframe.loc[i]
#         if '2014' in countDictionary:
#             countDictionary['2014'] += 1
#         else:
#             countDictionary['2014'] = 1
#     elif (date[5:9] == '2015' or date[6:10] == '2015'):
#         dataset2015.loc[i] = gamesDataframe.loc[i]
#         if '2015' in countDictionary:
#             countDictionary['2015'] += 1
#         else:
#             countDictionary['2015'] = 1
#     elif (date[5:9] == '2016' or date[6:10] == '2016'):
#         dataset2016.loc[i] = gamesDataframe.loc[i]
#         if '2016' in countDictionary:
#             countDictionary['2016'] += 1
#         else:
#             countDictionary['2016'] = 1
#     elif (date[5:9] == '2017' or date[6:10] == '2017'):
#         dataset2017.loc[i] = gamesDataframe.loc[i]
#         if '2017' in countDictionary:
#             countDictionary['2017'] += 1
#         else:
#             countDictionary['2017'] = 1
#     elif (date[5:9] == '2018' or date[6:10] == '2018'):
#         dataset2018.loc[i] = gamesDataframe.loc[i]
#         if '2018' in countDictionary:
#             countDictionary['2018'] += 1
#         else:
#             countDictionary['2018'] = 1
#     elif (date[5:9] == '2019' or date[6:10] == '2019'):
#         dataset2019.loc[i] = gamesDataframe.loc[i]
#         if '2019' in countDictionary:
#             countDictionary['2019'] += 1
#         else:
#             countDictionary['2019'] = 1
# Saving all the dataframes in csv files. DON'T UNCOMMENT THE LINES BELOW RIGHT NOW. TESTING
# dataset2000.to_csv('./yearly_dataset/dataset2000.csv')
# dataset2001.to_csv('./yearly_dataset/dataset2001.csv')
# dataset2002.to_csv('./yearly_dataset/dataset2002.csv')
# dataset2003.to_csv('./yearly_dataset/dataset2003.csv')
# dataset2004.to_csv('./yearly_dataset/dataset2004.csv')
# dataset2005.to_csv('./yearly_dataset/dataset2005.csv')
# dataset2006.to_csv('./yearly_dataset/dataset2006.csv')
# dataset2007.to_csv('./yearly_dataset/dataset2007.csv')
# dataset2008.to_csv('./yearly_dataset/dataset2008.csv')
# dataset2009.to_csv('./yearly_dataset/dataset2009.csv')
# dataset2010.to_csv('./yearly_dataset/dataset2010.csv')
# dataset2011.to_csv('./yearly_dataset/dataset2011.csv')
# dataset2012.to_csv('./yearly_dataset/dataset2012.csv')
# dataset2013.to_csv('./yearly_dataset/dataset2013.csv')
# dataset2014.to_csv('./yearly_dataset/dataset2014.csv')
# dataset2015.to_csv('./yearly_dataset/dataset2015.csv')
# dataset2016.to_csv('./yearly_dataset/dataset2016.csv')
# dataset2017.to_csv('./yearly_dataset/dataset2017.csv')
# dataset2018.to_csv('./yearly_dataset/dataset2018.csv')
# dataset2019.to_csv('./yearly_dataset/dataset2019.csv')
# Printing the dictionary to confirm the number of games in each file. TESTING
# print(countDictionary)

#######################################################################################
# SPLITTTING THE DATASET BY TEAM. MAKING SEPARATE DATESET FOR ALL TEAMS FOR ALL YEARS #
#######################################################################################

# THIS IS THE SECOND WAY THAT WE COULD SPLIT THE DATA. 

# Making a list of the names of the datasets over the years
# smallList = [dataset2000]
# datasetList = [dataset2000,dataset2001,dataset2002,dataset2003,dataset2004,dataset2005,dataset2006,dataset2007,dataset2008,dataset2009,
#                dataset2010,dataset2011,dataset2012,dataset2013,dataset2014,dataset2015,dataset2016,dataset2017,dataset2018,dataset2019]
# Making a list of all the teams in the NBA
teamList = ['Atlanta Hawks','Boston Celtics','Brooklyn Nets','Charlotte Hornets',
            'Chicago Bulls','Cleveland Cavaliers','Dallas Mavericks',
            'Denver Nuggets','Detroit Pistons','Golden State Warriors','Houston Rockets',
            'Indiana Pacers','Los Angeles Clippers','Los Angeles Lakers','Memphis Grizzlies',
            'Miami Heat','Milwaukee Bucks','Minnesota Timberwolves','New Orleans Pelicans',
            'New York Knicks','Oklahoma City Thunder','Orlando Magic','Philadelphia 76ers',
            'Phoenix Suns','Portland Trail Blazers','Sacramento Kings','San Antonio Spurs',
            'Toronto Raptors','Utah Jazz','Washington Wizards']

# Making a dictionary to store the names of the teams, and number of rows in each dataset
countDictionary = {}

# Creating a datframe for every team that contains data from all the years
Atlanta_Hawks = pd.DataFrame(columns = gamesColumns)
Boston_Celtics = pd.DataFrame(columns = gamesColumns)
Brooklyn_Nets = pd.DataFrame(columns = gamesColumns)
Charlotte_Hornets = pd.DataFrame(columns = gamesColumns)
Chicago_Bulls = pd.DataFrame(columns = gamesColumns)
Cleveland_Cavaliers = pd.DataFrame(columns = gamesColumns)
Dallas_Mavericks = pd.DataFrame(columns = gamesColumns)
Denver_Nuggets = pd.DataFrame(columns = gamesColumns)
Detroit_Pistons = pd.DataFrame(columns = gamesColumns)
Golden_State_Warriors = pd.DataFrame(columns = gamesColumns)
Houston_Rockets = pd.DataFrame(columns = gamesColumns)
Indiana_Pacers = pd.DataFrame(columns = gamesColumns)
Los_Angeles_Clippers = pd.DataFrame(columns = gamesColumns)
Los_Angeles_Lakers = pd.DataFrame(columns = gamesColumns)
Memphis_Grizzlies = pd.DataFrame(columns = gamesColumns)
Miami_Heat = pd.DataFrame(columns = gamesColumns)
Milwaukee_Bucks = pd.DataFrame(columns = gamesColumns)
Minnesota_Timberwolves = pd.DataFrame(columns = gamesColumns)
New_Orleans_Pelicans = pd.DataFrame(columns = gamesColumns)
New_York_Knicks = pd.DataFrame(columns = gamesColumns)
Oklahoma_City_Thunder = pd.DataFrame(columns = gamesColumns)
Orlando_Magic = pd.DataFrame(columns = gamesColumns)
Philadelphia_76ers = pd.DataFrame(columns = gamesColumns)
Phoenix_Suns = pd.DataFrame(columns = gamesColumns)
Portland_Trail_Blazers = pd.DataFrame(columns = gamesColumns)
Sacramento_Kings = pd.DataFrame(columns = gamesColumns)
San_Antonio_Spurs = pd.DataFrame(columns = gamesColumns)
Toronto_Raptors = pd.DataFrame(columns = gamesColumns)
Utah_Jazz = pd.DataFrame(columns = gamesColumns)
Washington_Wizards = pd.DataFrame(columns = gamesColumns)

# Getting the column for the data the contains the name of the team that is playing home
teamNameColumn = gamesDataframe['team_name_home']
# Iterating through the entire gameDataset
for i, team in enumerate(teamNameColumn):
        if (team == 'Atlanta Hawks'):
            Atlanta_Hawks.loc[i] = gamesDataframe.loc[i]
            if 'Atlanta Hawks' in countDictionary:
                countDictionary['Atlanta Hawks'] += 1
            else:
                countDictionary['Atlanta Hawks'] = 1
        if (team == 'Boston Celtics'):
            Boston_Celtics.loc[i] = gamesDataframe.loc[i]
            if 'Boston Celtics' in countDictionary:
                countDictionary['Boston Celtics'] += 1
            else:
                countDictionary['Boston Celtics'] = 1
        if (team == 'Brooklyn Nets'):
            Brooklyn_Nets.loc[i] = gamesDataframe.loc[i]
            if 'Brooklyn Nets' in countDictionary:
                


            





    


    


