# This file is used to clean the Kaggle dataset. The dataset can be found here: https://www.kaggle.com/datasets/wyattowalsh/basketball/discussion.
# The format of the code is that of scripting, rather than having function calls.
# I datset has been downlaoded, and is in the file game2000.csv

# The plan is to do the following:
#   1. Load the entire dataset into a pandas dataset.
#   2. 

import pandas as pd
import os
import numpy as np
import statgetter

# recurant neural networks -- Look into this, we might have to implement this

#####################################
# LOADING THE DATA INTO A DATAFRAME #
#####################################

# This reads in the file called 'game.csv'
gamesDataframe = pd.read_csv('./game2000.csv', index_col=None)
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

# Taking subdataframes by season_id
dataset2000 = gamesDataframe[gamesDataframe['season_id'] == 22000]
dataset2001 = gamesDataframe[gamesDataframe['season_id'] == 22001]
dataset2002 = gamesDataframe[gamesDataframe['season_id'] == 22002]
dataset2003 = gamesDataframe[gamesDataframe['season_id'] == 22003]
dataset2004 = gamesDataframe[gamesDataframe['season_id'] == 22004]
dataset2005 = gamesDataframe[gamesDataframe['season_id'] == 22005]
dataset2006 = gamesDataframe[gamesDataframe['season_id'] == 22006]
dataset2007 = gamesDataframe[gamesDataframe['season_id'] == 22007]
dataset2008 = gamesDataframe[gamesDataframe['season_id'] == 22008]
dataset2009 = gamesDataframe[gamesDataframe['season_id'] == 22009]
dataset2010 = gamesDataframe[gamesDataframe['season_id'] == 22010]
dataset2011 = gamesDataframe[gamesDataframe['season_id'] == 22011]
dataset2012 = gamesDataframe[gamesDataframe['season_id'] == 22012]
dataset2013 = gamesDataframe[gamesDataframe['season_id'] == 22013]
dataset2014 = gamesDataframe[gamesDataframe['season_id'] == 22014]
dataset2015 = gamesDataframe[gamesDataframe['season_id'] == 22015]
dataset2016 = gamesDataframe[gamesDataframe['season_id'] == 22016]
# dataset2017 = gamesDataframe[gamesDataframe['season_id'] == 22017] #2017 data doesn't exist
dataset2018 = gamesDataframe[gamesDataframe['season_id'] == 22018]
dataset2019 = gamesDataframe[gamesDataframe['season_id'] == 22019]
dataset2020 = gamesDataframe[gamesDataframe['season_id'] == 22020]
dataset2021 = gamesDataframe[gamesDataframe['season_id'] == 22021]
dataset2022 = gamesDataframe[gamesDataframe['season_id'] == 22022]

# Saving all the dataframes in csv files. DON'T UNCOMMENT THE LINES BELOW RIGHT NOW. TESTING
dataset2000.to_csv('./yearly_dataset/dataset2000.csv')
dataset2001.to_csv('./yearly_dataset/dataset2001.csv')
dataset2002.to_csv('./yearly_dataset/dataset2002.csv')
dataset2003.to_csv('./yearly_dataset/dataset2003.csv')
dataset2004.to_csv('./yearly_dataset/dataset2004.csv')
dataset2005.to_csv('./yearly_dataset/dataset2005.csv')
dataset2006.to_csv('./yearly_dataset/dataset2006.csv')
dataset2007.to_csv('./yearly_dataset/dataset2007.csv')
dataset2008.to_csv('./yearly_dataset/dataset2008.csv')
dataset2009.to_csv('./yearly_dataset/dataset2009.csv')
dataset2010.to_csv('./yearly_dataset/dataset2010.csv')
dataset2011.to_csv('./yearly_dataset/dataset2011.csv')
dataset2012.to_csv('./yearly_dataset/dataset2012.csv')
dataset2013.to_csv('./yearly_dataset/dataset2013.csv')
dataset2014.to_csv('./yearly_dataset/dataset2014.csv')
dataset2015.to_csv('./yearly_dataset/dataset2015.csv')
dataset2016.to_csv('./yearly_dataset/dataset2016.csv')
# dataset2017.to_csv('./yearly_dataset/dataset2017.csv') #2017 data doesn't exist
dataset2018.to_csv('./yearly_dataset/dataset2018.csv')
dataset2019.to_csv('./yearly_dataset/dataset2019.csv')
dataset2020.to_csv('./yearly_dataset/dataset2020.csv')
dataset2021.to_csv('./yearly_dataset/dataset2021.csv')
dataset2022.to_csv('./yearly_dataset/dataset2022.csv')
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

# Making a list of all the teams abbrevs in the NBA
teamList = ['ATL', 'BOS', 'BKN', 'CHA', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 
            'HOU', 'IND', 'LAC', 'LAL', 'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 
            'OKC', 'ORL', 'PHI', 'PHX', 'POR', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS']

teamCodes = [1610612737, 1610612738, 1610612751, 1610612766, 1610612741, 1610612739, 1610612742, 1610612743, 1610612765, 1610612744, 
             1610612745, 1610612754, 1610612746, 1610612747, 1610612763, 1610612748, 1610612749, 1610612750, 1610612740, 1610612752,
             1610612760, 1610612753, 1610612755, 1610612756, 1610612758, 1610612759, 1610612761, 1610612762, 1610612764]

# Making a dictionary to store the names of the teams, and number of rows in each dataset
countDictionary = {}

#Uses helper functions in statgetter to divide each season by team, average them, then split by conference
east2000, west2000 = statgetter.getTeamAverages(dataset2000)
east2001, west2001 = statgetter.getTeamAverages(dataset2001)
east2002, west2002 = statgetter.getTeamAverages(dataset2002)
east2003, west2003 = statgetter.getTeamAverages(dataset2003)
east2004, west2004 = statgetter.getTeamAverages(dataset2004)
east2005, west2005 = statgetter.getTeamAverages(dataset2005)
east2006, west2006 = statgetter.getTeamAverages(dataset2006)
east2007, west2007 = statgetter.getTeamAverages(dataset2007)
east2008, west2008 = statgetter.getTeamAverages(dataset2008)
east2009, west2009 = statgetter.getTeamAverages(dataset2009)
east2010, west2010 = statgetter.getTeamAverages(dataset2010)
east2011, west2011 = statgetter.getTeamAverages(dataset2011)
east2012, west2012 = statgetter.getTeamAverages(dataset2012)
east2013, west2013 = statgetter.getTeamAverages(dataset2013)
east2014, west2014 = statgetter.getTeamAverages(dataset2014)
east2015, west2015 = statgetter.getTeamAverages(dataset2015)
east2016, west2016 = statgetter.getTeamAverages(dataset2016)
# east2017, west2017 = statgetter.getTeamAverages(dataset2017) #2017 data doesn't exist in dataset
east2018, west2018 = statgetter.getTeamAverages(dataset2018)
east2019, west2019 = statgetter.getTeamAverages(dataset2019)
east2020, west2020 = statgetter.getTeamAverages(dataset2020)
east2021, west2021 = statgetter.getTeamAverages(dataset2021)
east2022, west2022 = statgetter.getTeamAverages(dataset2022)

# east2022.to_csv('./yearly_dataset/east2022.csv')
# west2022.to_csv('./yearly_dataset/west2022.csv')

##
## PLAYOFFS
##

# Making a list of all the teams in the NBA, including supersonics, NJN, vancouver
teamNames = ['Atlanta Hawks','Boston Celtics','Brooklyn Nets','Charlotte Hornets',
            'Chicago Bulls','Cleveland Cavaliers','Dallas Mavericks',
            'Denver Nuggets','Detroit Pistons','Golden State Warriors','Houston Rockets',
            'Indiana Pacers','Los Angeles Clippers','Los Angeles Lakers','Memphis Grizzlies',
            'Miami Heat','Milwaukee Bucks','Minnesota Timberwolves','New Orleans Pelicans',
            'New York Knicks','Oklahoma City Thunder','Orlando Magic','Philadelphia 76ers',
            'Phoenix Suns','Portland Trail Blazers','Sacramento Kings','San Antonio Spurs',
            'Toronto Raptors','Utah Jazz','Washington Wizards', 'Seattle SuperSonics', 'New Jersey Nets', 'Vancouver Grizzlies', 'Charlotte Bobcats', 'New Orleans Hornets']

teamAbbrev = ['ATL', 'BOS', 'BKN', 'CHA', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 
            'HOU', 'IND', 'LAC', 'LAL', 'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 
            'OKC', 'ORL', 'PHI', 'PHX', 'POR', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS', 'OKC', 'BKN', 'MEM', 'CHA', 'NOP']

#Section gets playoff data for every team into dataframes:
#Returns season's east and west playoff teams and a boolean
teamNameDict = dict(zip(teamAbbrev, teamNames))

playoffDataframe = pd.read_csv('./playoffs_data.csv', index_col=None)
east2000playoff, west2000playoff = statgetter.getPlayoffs(2000, playoffDataframe)
east2001playoff, west2001playoff = statgetter.getPlayoffs(2001, playoffDataframe)
east2002playoff, west2002playoff = statgetter.getPlayoffs(2002, playoffDataframe)
east2003playoff, west2003playoff = statgetter.getPlayoffs(2003, playoffDataframe)
east2004playoff, west2004playoff = statgetter.getPlayoffs(2004, playoffDataframe)
east2005playoff, west2005playoff = statgetter.getPlayoffs(2005, playoffDataframe)
east2006playoff, west2006playoff = statgetter.getPlayoffs(2006, playoffDataframe)
east2007playoff, west2007playoff = statgetter.getPlayoffs(2007, playoffDataframe)
east2008playoff, west2008playoff = statgetter.getPlayoffs(2008, playoffDataframe)
east2009playoff, west2009playoff = statgetter.getPlayoffs(2009, playoffDataframe)
east2010playoff, west2010playoff = statgetter.getPlayoffs(2010, playoffDataframe)
east2011playoff, west2011playoff = statgetter.getPlayoffs(2011, playoffDataframe)
east2012playoff, west2012playoff = statgetter.getPlayoffs(2012, playoffDataframe)
east2013playoff, west2013playoff = statgetter.getPlayoffs(2013, playoffDataframe)
east2014playoff, west2014playoff = statgetter.getPlayoffs(2014, playoffDataframe)
east2015playoff, west2015playoff = statgetter.getPlayoffs(2015, playoffDataframe)
east2016playoff, west2016playoff = statgetter.getPlayoffs(2016, playoffDataframe)
# east2017playoff, west2017playoff = statgetter.getPlayoffs(2017, playoffDataframe)
east2018playoff, west2018playoff = statgetter.getPlayoffs(2018, playoffDataframe)
east2019playoff, west2019playoff = statgetter.getPlayoffs(2019, playoffDataframe)
east2020playoff, west2020playoff = statgetter.getPlayoffs(2020, playoffDataframe)
east2021playoff, west2021playoff = statgetter.getPlayoffs(2021, playoffDataframe)
east2022playoff, west2022playoff = statgetter.getPlayoffs(2022, playoffDataframe)

east2022playoff.to_csv('./yearly_dataset/east2022playoff.csv')
west2022playoff.to_csv('./yearly_dataset/west2022playoff.csv')


print('All done with data processing! use the east and west dataframes and playoff dataframes to run supervised learning.')




