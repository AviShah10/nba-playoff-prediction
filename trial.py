import pandas as pd
import numpy as np

# # Making a list of all the teams in the NBA
# teamList = ['Atlanta Hawks','Boston Celtics','Brooklyn Nets','Charlotte Hornets',
#             'Chicago Bulls','Cleveland Cavaliers','Dallas Mavericks',
#             'Denver Nuggets','Detroit Pistons','Golden State Warriors','Houston Rockets',
#             'Indiana Pacers','Los Angeles Clippers','Los Angeles Lakers','Memphis Grizzlies',
#             'Miami Heat','Milwaukee Bucks','Minnesota Timberwolves','New Orleans Pelicans',
#             'New York Knicks','Oklahoma City Thunder','Orlando Magic','Philadelphia 76ers',
#             'Phoenix Suns','Portland Trail Blazers','Sacramento Kings','San Antonio Spurs',
#             'Toronto Raptors','Utah Jazz','Washington Wizards']
# teamListH = []
# header = ['Name','Age']
# for team in teamList:
#     teamName = team.replace(" ","_")
#     print(teamName)
#     print()

# Atlanta_Hawks = pd.DataFrame(columns = gameColumns)
# Boston_Celtics = pd.DataFrame(columns = gameColumns)
# Brooklyn_Nets = pd.DataFrame(columns = gameColumns)
# Charlotte_Hornets = pd.DataFrame(columns = gameColumns)
# Chicago_Bulls = pd.DataFrame(columns = gameColumns)
# Cleveland_Cavaliers = pd.DataFrame(columns = gameColumns)
# Dallas_Mavericks = pd.DataFrame(columns = gameColumns)
# Denver_Nuggets = pd.DataFrame(columns = gameColumns)
# Detroit_Pistons = pd.DataFrame(columns = gameColumns)
# Golden_State_Warriors = pd.DataFrame(columns = gameColumns)
# Houston_Rockets = pd.DataFrame(columns = gameColumns)
# Indiana_Pacers = pd.DataFrame(columns = gameColumns)
# Los_Angeles_Clippers = pd.DataFrame(columns = gameColumns)
# Los_Angeles_Lakers = pd.DataFrame(columns = gameColumns)
# Memphis_Grizzlies = pd.DataFrame(columns = gameColumns)
# Miami_Heat = pd.DataFrame(columns = gameColumns)
# Milwaukee_Bucks = pd.DataFrame(columns = gameColumns)
# Minnesota_Timberwolves = pd.DataFrame(columns = gameColumns)
# New_Orleans_Pelicans = pd.DataFrame(columns = gameColumns)
# New_York_Knicks = pd.DataFrame(columns = gameColumns)
# Oklahoma_City_Thunder = pd.DataFrame(columns = gameColumns)
# Orlando_Magic = pd.DataFrame(columns = gameColumns)
# Philadelphia_76ers = pd.DataFrame(columns = gameColumns)
# Phoenix_Suns = pd.DataFrame(columns = gameColumns)
# Portland_Trail_Blazers = pd.DataFrame(columns = gameColumns)
# Sacramento_Kings = pd.DataFrame(columns = gameColumns)
# San_Antonio_Spurs = pd.DataFrame(columns = gameColumns)
# Toronto_Raptors = pd.DataFrame(columns = gameColumns)
# Utah_Jazz = pd.DataFrame(columns = gameColumns)
# Washington_Wizards = pd.DataFrame(columns = gameColumns)

columnHeader = ['Twos','Threes','Fours','Fives']
base = pd.DataFrame(columns = columnHeader)
array = np.array([2,3,4,5])
print(array)
for item in columnHeader:
    base.loc[item] = array

print(base)