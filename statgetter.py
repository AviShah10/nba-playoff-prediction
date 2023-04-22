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
    
    #Using team id instead due to moved/defunct nba teams i.e. vancouver, seattle, new jersey, etc
    teamCodes = [1610612737, 1610612738, 1610612751, 1610612766, 1610612741, 1610612739, 1610612742, 1610612743, 1610612765, 1610612744, 1610612745,
                 1610612754, 1610612746, 1610612747, 1610612763, 1610612748, 1610612749, 1610612750, 1610612740, 1610612752, 1610612760, 1610612753, 
                 1610612755, 1610612756, 1610612757, 1610612758, 1610612759, 1610612761, 1610612762, 1610612764]

    teamNames = ['Atlanta Hawks','Boston Celtics','Brooklyn Nets','Charlotte Hornets',
            'Chicago Bulls','Cleveland Cavaliers','Dallas Mavericks',
            'Denver Nuggets','Detroit Pistons','Golden State Warriors','Houston Rockets',
            'Indiana Pacers','Los Angeles Clippers','Los Angeles Lakers','Memphis Grizzlies',
            'Miami Heat','Milwaukee Bucks','Minnesota Timberwolves','New Orleans Pelicans',
            'New York Knicks','Oklahoma City Thunder','Orlando Magic','Philadelphia 76ers',
            'Phoenix Suns','Portland Trail Blazers','Sacramento Kings','San Antonio Spurs',
            'Toronto Raptors','Utah Jazz','Washington Wizards']
    
    teamNameDict = dict(zip(teamList, teamNames))

    #Creaets dict of all the teams' id and abbreviation
    teamDict = dict(zip(teamCodes, teamList))

    #Creates dict of all the teams' games for that season
    teamStats = {}

    #IMPORTANT: THESE ARE THE STATS WE WILL BE GETTING!!!
    statsColumns = ['WLPCT', 'MATCHUP', 'FGM', 'FGA', 'FGPCT', 'FG3M', 'FG3A', 'FG3PCT', 'FTM', 'FTA', 'FTPCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'PM']

    #Loop through each team and create entry in teamStats dictionary
    for team in teamCodes:
        teamStats[team] = seasonDataframe[(seasonDataframe['team_id_home'] == team) | (seasonDataframe['team_id_away'] == team)]
        #temporary variable to store team's dataframe
        df = teamStats[team]

        #empty dataframe to fill with first half of season's games
        temp = pd.DataFrame(columns = statsColumns)

        #Loop through team's first half of games, take stats from home or away columns
        i = 0 #counter for num games
        for homeid in df['team_id_home']:
            if homeid == team:
                temp = pd.concat([temp, getHomeStats(df.iloc[[i]])])
            else:
                temp = pd.concat([temp, getAwayStats(df.iloc[[i]])])

            i += 1

            # CRITICAL: edit this for how many games to include
            #only takes first half of the season's games (88 game season)
            if i >= 41:
                break
            #Also thinking about doing home and away win percentage as separate columns?

        #Average the columns into new dataframe
        temp = temp.mean(axis=0).to_frame().T

        teamStats[team] = temp

    #List with eastern conference, western conference teams ids
    eastTeams = [1610612737, 1610612738, 1610612751, 1610612766, 1610612741, 1610612739, 1610612765,
                 1610612754, 1610612748, 1610612749, 1610612752, 1610612753,
                 1610612755, 1610612761, 1610612764]
    
    # westTeams = list(set(teamCodes) - set(eastTeams))
    
    #Loop through and split into east team averages dataframe and west team averages dataframe
    eastAverages = pd.DataFrame(columns = statsColumns)
    eastAverages.insert(0, 'TEAM', [])
    westAverages = pd.DataFrame(columns = statsColumns)
    westAverages.insert(0, 'TEAM', [])


    for n in range (len(teamList)):
        teamid = teamCodes[n]
        teamdf = teamStats[teamid]
        teamdf.insert(0, 'TEAM', teamDict[teamid])
        if teamid in eastTeams:
            eastAverages = pd.concat([eastAverages, teamdf])
        else:
            westAverages = pd.concat([westAverages, teamdf])

    return eastAverages, westAverages

# Helper function to get stats from csv if team is at home. Win is 1, loss is 0
def getHomeStats(homegame: pd.DataFrame):
    gamedf = homegame[['wl_home', 'matchup_home', 'fgm_home', 'fga_home', 'fg_pct_home', 
                       'fg3m_home', 'fg3a_home', 'fg3_pct_home', 'ftm_home', 'fta_home', 'ft_pct_home', 'oreb_home', 'dreb_home',
                       'reb_home', 'ast_home', 'stl_home', 'blk_home', 'tov_home', 'pf_home', 'pts_home',
                       'plus_minus_home']]
    statsColumns = ['WLPCT', 'MATCHUP', 'FGM', 'FGA', 'FGPCT', 'FG3M', 'FG3A', 'FG3PCT', 'FTM', 'FTA', 'FTPCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'PM']
    gamedf.columns = statsColumns

    if gamedf.at[gamedf.index[0],'WLPCT'] == 'L':
        gamedf.at[gamedf.index[0],'WLPCT'] = 0
    else:
        gamedf.at[gamedf.index[0],'WLPCT'] = 1

    #0 is defined as home
    gamedf.at[gamedf.index[0],'MATCHUP'] = 0

    return gamedf

# Helper function to get stats from csv if team is away. Win is 1, loss is 0
def getAwayStats(awaygame: pd.DataFrame):
    gamedf = awaygame[['wl_away', 'matchup_away', 'fgm_away', 'fga_away', 'fg_pct_away', 
                       'fg3m_away', 'fg3a_away', 'fg3_pct_away', 'ftm_away', 'fta_away', 'ft_pct_away', 'oreb_away', 'dreb_away',
                       'reb_away', 'ast_away', 'stl_away', 'blk_away', 'tov_away', 'pf_away', 'pts_away',
                       'plus_minus_away']]
    statsColumns = ['WLPCT', 'MATCHUP', 'FGM', 'FGA', 'FGPCT', 'FG3M', 'FG3A', 'FG3PCT', 'FTM', 'FTA', 'FTPCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'PM']
    gamedf.columns = statsColumns

    if gamedf.at[gamedf.index[0],'WLPCT'] == 'L':
        gamedf.at[gamedf.index[0],'WLPCT'] = 0
    else:
        gamedf.at[gamedf.index[0],'WLPCT'] = 1

    #1 is defined as away
    gamedf.at[gamedf.index[0],'MATCHUP'] = 1
    return gamedf


# Helper function to get the playoff results dataframe for east, west for given season
def getPlayoffs(year, playoffdf: pd.DataFrame):
    teamNames = ['Atlanta Hawks','Boston Celtics','Brooklyn Nets','Charlotte Hornets',
                'Chicago Bulls','Cleveland Cavaliers','Dallas Mavericks',
                'Denver Nuggets','Detroit Pistons','Golden State Warriors','Houston Rockets',
                'Indiana Pacers','Los Angeles Clippers','Los Angeles Lakers','Memphis Grizzlies',
                'Miami Heat','Milwaukee Bucks','Minnesota Timberwolves','New Orleans Pelicans',
                'New York Knicks','Oklahoma City Thunder','Orlando Magic','Philadelphia 76ers',
                'Phoenix Suns','Portland Trail Blazers','Sacramento Kings','San Antonio Spurs',
                'Toronto Raptors','Utah Jazz','Washington Wizards', 'Seattle SuperSonics', 'New Jersey Nets', 'Vancouver Grizzlies', 'Charlotte Bobcats', 'New Orleans Hornets', 'New Orleans/Oklahoma City Hornets']

    teamAbbrev = ['ATL', 'BOS', 'BKN', 'CHA', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 
            'HOU', 'IND', 'LAC', 'LAL', 'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 
            'OKC', 'ORL', 'PHI', 'PHX', 'POR', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS', 'OKC', 'BKN', 'MEM', 'CHA', 'NOP', 'NOP']

    east = ['ATL', 'BOS', 'BKN', 'CHA', 'CHI', 'CLE', 'DET', 'IND', 'MIA', 'MIL', 'NYK', 'ORL', 'PHI', 'TOR', 'WAS']

    west = ['DAL', 'DEN', 'GSW', 'HOU', 'LAC', 'LAL', 'MEM', 'MIN', 'NOP', 'OKC', 'PHX', 'POR', 'SAC', 'SAS', 'UTA']

    #Section gets playoff data for every team into dataframes:
    #Returns season's east and west playoff teams and a boolean
    teamNameDict = dict(zip(teamNames, teamAbbrev))

    seasondf = playoffdf[playoffdf['year'] == year]

    eastplayoff = pd.DataFrame(columns = ['TEAM', 'PLAYOFF'])
    westplayoff = pd.DataFrame(columns = ['TEAM', 'PLAYOFF'])

    for teamname in seasondf['team']:
        team = teamNameDict[teamname]
        playoff_status = seasondf[seasondf['team'] == teamname]['is_playoffs_team'].values[0]
        row = pd.DataFrame({'TEAM': [team], 'PLAYOFF': [playoff_status]})
        if team in east:
            eastplayoff = pd.concat([eastplayoff, row], ignore_index=True)
        else:
            westplayoff = pd.concat([westplayoff, row], ignore_index=True)

    return eastplayoff, westplayoff
