# This file is used to clean the Kaggle dataset. The dataset can be found here: https://www.kaggle.com/datasets/wyattowalsh/basketball/discussion.
# The format of the code is that of scripting, rather than having function calls.
# I datset has been downlaoded, and is in the file game2000.csv
# The plan is to do the following:
#   1. Load the dataset into a pandas dataset.
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
# Making a list of all the teams in the NBA
teamList = ['Atlanta Hawks','Boston Celtics','Brooklyn Nets','Charlotte Hornets',
            'Chicago Bulls','Cleveland Cavaliers','Dallas Mavericks',
            'Denver Nuggets','Detroit Pistons','Golden State Warriors','Houston Rockets',
            'Indiana Pacers','Los Angeles Clippers','Los Angeles Lakers','Memphis Grizzlies',
            'Miami Heat','Milwaukee Bucks','Minnesota Timberwolves','New Orleans Pelicans',
            'New York Knicks','Oklahoma City Thunder','Orlando Magic','Philadelphia 76ers',
            'Phoenix Suns','Portland Trail Blazers','Sacramento Kings','San Antonio Spurs',
            'Toronto Raptors','Utah Jazz','Washington Wizards']

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
east2018, west2018 = statgetter.getTeamAverages(dataset2018)
east2019, west2019 = statgetter.getTeamAverages(dataset2019)
east2020, west2020 = statgetter.getTeamAverages(dataset2020)
east2021, west2021 = statgetter.getTeamAverages(dataset2021)
east2022, west2022 = statgetter.getTeamAverages(dataset2022)


#OLD CODE: may not be needed anymore
# # Creating a datframe for every team that contains data from all the years
# Atlanta_Hawks = pd.DataFrame(columns = gamesColumns)
# Boston_Celtics = pd.DataFrame(columns = gamesColumns)
# Brooklyn_Nets = pd.DataFrame(columns = gamesColumns)
# Charlotte_Hornets = pd.DataFrame(columns = gamesColumns)
# Chicago_Bulls = pd.DataFrame(columns = gamesColumns)
# Cleveland_Cavaliers = pd.DataFrame(columns = gamesColumns)
# Dallas_Mavericks = pd.DataFrame(columns = gamesColumns)
# Denver_Nuggets = pd.DataFrame(columns = gamesColumns)
# Detroit_Pistons = pd.DataFrame(columns = gamesColumns)
# Golden_State_Warriors = pd.DataFrame(columns = gamesColumns)
# Houston_Rockets = pd.DataFrame(columns = gamesColumns)
# Indiana_Pacers = pd.DataFrame(columns = gamesColumns)
# Los_Angeles_Clippers = pd.DataFrame(columns = gamesColumns)
# Los_Angeles_Lakers = pd.DataFrame(columns = gamesColumns)
# Memphis_Grizzlies = pd.DataFrame(columns = gamesColumns)
# Miami_Heat = pd.DataFrame(columns = gamesColumns)
# Milwaukee_Bucks = pd.DataFrame(columns = gamesColumns)
# Minnesota_Timberwolves = pd.DataFrame(columns = gamesColumns)
# New_Orleans_Pelicans = pd.DataFrame(columns = gamesColumns)
# New_York_Knicks = pd.DataFrame(columns = gamesColumns)
# Oklahoma_City_Thunder = pd.DataFrame(columns = gamesColumns)
# Orlando_Magic = pd.DataFrame(columns = gamesColumns)
# Philadelphia_76ers = pd.DataFrame(columns = gamesColumns)
# Phoenix_Suns = pd.DataFrame(columns = gamesColumns)
# Portland_Trail_Blazers = pd.DataFrame(columns = gamesColumns)
# Sacramento_Kings = pd.DataFrame(columns = gamesColumns)
# San_Antonio_Spurs = pd.DataFrame(columns = gamesColumns)
# Toronto_Raptors = pd.DataFrame(columns = gamesColumns)
# Utah_Jazz = pd.DataFrame(columns = gamesColumns)
# Washington_Wizards = pd.DataFrame(columns = gamesColumns)

# # Getting the column for the data the contains the name of the team that is playing home
# teamNameColumn = gamesDataframe['team_name_home']
# # Iterating through the entire gameDataset
# for i, team in enumerate(teamNameColumn):
#         if (team == 'Atlanta Hawks'):
#             Atlanta_Hawks.loc[i] = gamesDataframe.loc[i]
#             if 'Atlanta Hawks' in countDictionary:
#                 countDictionary['Atlanta Hawks'] += 1
#             else:
#                 countDictionary['Atlanta Hawks'] = 1
#         if (team == 'Boston Celtics'):
#             Boston_Celtics.loc[i] = gamesDataframe.loc[i]
#             if 'Boston Celtics' in countDictionary:
#                 countDictionary['Boston Celtics'] += 1
#             else:
#                 countDictionary['Boston Celtics'] = 1
#         if (team == 'Brooklyn Nets'):
#             Brooklyn_Nets.loc[i] = gamesDataframe.loc[i]
#             if 'Brooklyn Nets' in countDictionary:
#                 countDictionary['Brooklyn Nets'] += 1
#             else:
#                 countDictionary['Brooklyn Nets'] = 1

