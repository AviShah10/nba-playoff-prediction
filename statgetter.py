import pandas as pd
import os
import numpy as np


# function takes in dataframe of season's games,
# First divides by each team
# Next splits by first half of the season
# Then averages all stats during first half of said season
# Finally recombines into East/West dataframes for team avg stats for that season
def getTeamAverages(seasonDataframe: pd.DataFrame):
    teamList = ['ATL', 'BOS', 'BKN', 'CHA', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU',
            'IND', 'LAC', 'LAL', 'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 'OKC', 'ORL', 
            'PHI', 'PHX', 'POR', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS']
    
    #Creates dict of all the teams' games for that season
    teamStats = {}

    #IMPORTANT: THESE ARE THE STATS WE WILL BE GETTING!!!
    statsColumns = ['WLPCT', 'MATCHUP', 'FGM', 'FGA', 'FGPCT', 'FG3M', 'FG3A', 'FG3PCT', 'FTM', 'FTA', 'FTPCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'PM']

    #Loop through each team and create entry in teamStats dictionary
    for team in teamList:
        teamStats[team] = seasonDataframe[(seasonDataframe['team_abbreviation_home'] == team) | (seasonDataframe['team_abbreviation_away'] == team)]
        #temporary variable to store team's dataframe
        df = teamStats[team]

        #empty dataframe to fill with first half of season's games
        temp = pd.DataFrame(columns = statsColumns)

        #Loop through team's first half of games, take stats from home or away columns
        i = 0 #counter for num games
        for homeid in df['team_id_home']:
            if homeid == team:
                temp.append(getHomeStats(df.iloc[[i]]))
            else:
                temp.append(getAwayStats(df.iloc[[i]]))

            i += 1
            #only takes first half of the season's games (88 game season)
            if i >= 44:
                break
            #Also thinking about doing home and away win percentage as separate columns?

        teamStats[team] = temp

    #Average the columns into new dataframe
    
    #Separate quick calculation for win percentage

    eastAverages = 0
    westAverages = 0

    return eastAverages, westAverages

# Helper function to get stats from csv if team is at home. Win is 1, loss is 0
def getHomeStats(homegame: pd.DataFrame):
    gamedf = homegame[['wl_home', 'matchup_home', 'fgm_home', 'fga_home', 'fg_pct_home', 
                       'fg3m_home', 'fg3a_home', 'fg3_pct_home', 'ftm_home', 'fta_home', 'ft_pct_home', 'oreb_home', 'dreb_home',
                       'reb_home', 'ast_home', 'stl_home', 'blk_home', 'tov_home', 'pf_home', 'pts_home',
                       'plus_minus_home']]
    statsColumns = ['WLPCT', 'MATCHUP', 'FGM', 'FGA', 'FGPCT', 'FG3M', 'FG3A', 'FG3PCT', 'FTM', 'FTA', 'FTPCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'PM']
    gamedf.columns = statsColumns

    if gamedf['WLPCT'].iloc[0] == 'L':
        gamedf['WLPCT'].iloc[0] = 0
    else:
        gamedf['WLPCT'].iloc[0] = 1

    #0 is defined as home
    gamedf['MATCHUP'].iloc[0] = 0

    return gamedf

# Helper function to get stats from csv if team is at home. Win is 1, loss is 0
def getAwayStats(awaygame: pd.DataFrame):
    gamedf = awaygame[['wl_away', 'matchup_away', 'fgm_away', 'fga_away', 'fg_pct_away', 
                       'fg3m_away', 'fg3a_away', 'fg3_pct_away', 'ftm_away', 'fta_away', 'ft_pct_away', 'oreb_away', 'dreb_away',
                       'reb_away', 'ast_away', 'stl_away', 'blk_away', 'tov_away', 'pf_away', 'pts_away',
                       'plus_minus_away']]
    statsColumns = ['WLPCT', 'MATCHUP', 'FGM', 'FGA', 'FGPCT', 'FG3M', 'FG3A', 'FG3PCT', 'FTM', 'FTA', 'FTPCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'PM']
    gamedf.columns = statsColumns

    if gamedf['WLPCT'].iloc[0] == 'L':
        gamedf['WLPCT'].iloc[0] = 0
    else:
        gamedf['WLPCT'].iloc[0] = 1

    #1 is defined as away
    gamedf['MATCHUP'].iloc[0] = 1
    return gamedf