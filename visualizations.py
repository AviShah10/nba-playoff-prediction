import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn as sk
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import seaborn as sns

# sudo pip install csvkit
# sudo apt-get install python-dev python-pip python-setuptools build-essential

# read in csv
east_data = pd.read_csv("https://raw.githubusercontent.com/AviShah10/nba-playoff-prediction/main/season_stats_2000to2022/eastTrainingData.csv?token=GHSAT0AAAAAACAWOTD5XKWSHIIY3MVQCZQMZBHIT6A")
east_playoff_data = pd.read_csv("https://raw.githubusercontent.com/AviShah10/nba-playoff-prediction/main/playoff_labels_2000to2022/eastTrainingPlayoffs.csv?token=GHSAT0AAAAAACAWOTD5DPF7X4AK6DJUORXMZBHHHNA")

west_data = pd.read_csv("https://raw.githubusercontent.com/AviShah10/nba-playoff-prediction/main/season_stats_2000to2022/westTrainingData.csv?token=GHSAT0AAAAAACAWOTD5ZWKBMM5ULKPCV77GZBHIIIQ")
west_playoff_data = pd.read_csv("https://raw.githubusercontent.com/AviShah10/nba-playoff-prediction/main/playoff_labels_2000to2022/westTrainingPlayoffs.csv?token=GHSAT0AAAAAACAWOTD5N3UZ5DFECN46CMDYZBHIJ2Q")



colors = {1.0:'red', 0.0:'blue'}
plt.scatter(east_data['SEASON'], east_data['FGA'], c=east_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('Year')
plt.ylabel('FGA')
plt.title("EAST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

plt.scatter(west_data['SEASON'], west_data['FGA'], c=west_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('Year')
plt.ylabel('FGA')
plt.title("WEST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

plt.scatter(west_data['SEASON'], west_data['FGA'], c=west_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.scatter(east_data['SEASON'], east_data['FGA'], c=east_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('Year')
plt.ylabel('FGA')
plt.title("EAST AND WEST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

colors = {1.0:'red', 0.0:'blue'}
plt.scatter(east_data['SEASON'], east_data['FGPCT'], c=east_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('Year')
plt.ylabel('FGPCT')
plt.title("EAST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

plt.scatter(west_data['SEASON'], west_data['FGPCT'], c=west_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('Year')
plt.ylabel('FGPCT')
plt.title("WEST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

plt.scatter(west_data['SEASON'], west_data['FGPCT'], c=west_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.scatter(east_data['SEASON'], east_data['FGPCT'], c=east_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('Year')
plt.ylabel('FGPCT')
plt.title("EAST AND WEST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

colors = {1.0:'red', 0.0:'blue'}
plt.scatter(east_data['SEASON'], east_data['REB'], c=east_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('Year')
plt.ylabel('REB')
plt.title("EAST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

plt.scatter(west_data['SEASON'], west_data['REB'], c=west_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('Year')
plt.ylabel('REB')
plt.title("WEST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

plt.scatter(west_data['SEASON'], west_data['REB'], c=west_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.scatter(east_data['SEASON'], east_data['REB'], c=east_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('Year')
plt.ylabel('REB')
plt.title("EAST AND WEST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

colors = {1.0:'red', 0.0:'blue'}
plt.scatter(east_data['SEASON'], east_data['BLK'], c=east_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('Year')
plt.ylabel('BLK')
plt.title("EAST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

plt.scatter(west_data['SEASON'], west_data['BLK'], c=west_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('Year')
plt.ylabel('BLK')
plt.title("WEST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

plt.scatter(west_data['SEASON'], west_data['BLK'], c=west_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.scatter(east_data['SEASON'], east_data['BLK'], c=east_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('Year')
plt.ylabel('BLK')
plt.title("EAST AND WEST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

colors = {1.0:'red', 0.0:'blue'}
plt.scatter(east_data['SEASON'], east_data['STL'], c=east_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('Year')
plt.ylabel('STL')
plt.title("EAST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

plt.scatter(west_data['SEASON'], west_data['STL'], c=west_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('Year')
plt.ylabel('STL')
plt.title("WEST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

plt.scatter(west_data['SEASON'], west_data['STL'], c=west_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.scatter(east_data['SEASON'], east_data['STL'], c=east_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('Year')
plt.ylabel('STL')
plt.title("EAST AND WEST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

colors = {1.0:'red', 0.0:'blue'}
plt.scatter(east_data['SEASON'], east_data['PM'], c=east_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('Year')
plt.ylabel('PM')
plt.title("EAST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

plt.scatter(west_data['SEASON'], west_data['PM'], c=west_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('Year')
plt.ylabel('PM')
plt.title("WEST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

plt.scatter(west_data['SEASON'], west_data['PM'], c=west_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.scatter(east_data['SEASON'], east_data['PM'], c=east_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('Year')
plt.ylabel('PM')
plt.title("EAST AND WEST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

colors = {1.0:'red', 0.0:'blue'}
plt.scatter(east_data['FGPCT'], east_data['REB'], c=east_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('FGPCT')
plt.ylabel('REB')
plt.title("EAST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

plt.scatter(west_data['FGPCT'], west_data['REB'], c=west_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('FGPCT')
plt.ylabel('REB')
plt.title("WEST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

plt.scatter(west_data['FGPCT'], west_data['REB'], c=west_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.scatter(east_data['FGPCT'], east_data['REB'], c=east_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('FGPCT')
plt.ylabel('REB')
plt.title("EAST AND WEST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

print(np.corrcoef(east_data['FGPCT'], east_data['REB']))


colors = {1.0:'red', 0.0:'blue'}
plt.scatter(east_data['SEASON'], east_data['FG3A'], c=east_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('Year')
plt.ylabel('FG3A')
plt.title("EAST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

plt.scatter(west_data['SEASON'], west_data['FG3A'], c=west_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('Year')
plt.ylabel('FG3A')
plt.title("WEST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

plt.scatter(west_data['SEASON'], west_data['FG3A'], c=west_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.scatter(east_data['SEASON'], east_data['FG3A'], c=east_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('Year')
plt.ylabel('FG3A')
plt.title("EAST AND WEST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

colors = {1.0:'red', 0.0:'blue'}
plt.scatter(east_data['SEASON'], east_data['WLPCT'], c=east_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('Year')
plt.ylabel('WLPCT')
plt.title("EAST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

plt.scatter(west_data['SEASON'], west_data['WLPCT'], c=west_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('Year')
plt.ylabel('WLPCT')
plt.title("WEST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

plt.scatter(west_data['SEASON'], west_data['WLPCT'], c=west_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.scatter(east_data['SEASON'], east_data['WLPCT'], c=east_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('Year')
plt.ylabel('WLPCT')
plt.title("EAST AND WEST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

colors = {1.0:'red', 0.0:'blue'}
plt.scatter(east_data['SEASON'], east_data['FG3PCT'], c=east_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('Year')
plt.ylabel('FG3PCT')
plt.title("EAST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

plt.scatter(west_data['SEASON'], west_data['FG3PCT'], c=west_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('Year')
plt.ylabel('FG3PCT')
plt.title("WEST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

plt.scatter(west_data['SEASON'], west_data['FG3PCT'], c=west_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.scatter(east_data['SEASON'], east_data['FG3PCT'], c=east_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('Year')
plt.ylabel('FG3PCT')
plt.title("EAST AND WEST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()


ax = plt.axes(projection ="3d")

ax.scatter3D(east_data['SEASON'], east_data['WLPCT'], east_data['PM'], c=east_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
ax.scatter3D(west_data['SEASON'], west_data['WLPCT'], west_data['PM'], c=west_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))

print(np.corrcoef(east_data['PM'], east_data['WLPCT']))

 
# show plot
plt.show()

ax = plt.axes(projection ="3d")

ax.scatter3D(east_data['PM'], east_data['WLPCT'], east_data['FGPCT'], c=east_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
ax.scatter3D(west_data['PM'], west_data['WLPCT'], west_data['FGPCT'], c=west_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))


 
# show plot
plt.show()

colors = {1.0:'red', 0.0:'blue'}
plt.scatter(east_data['FGPCT'], east_data['FGA'], c=east_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('FGPCT')
plt.ylabel('FGA')
plt.title("EAST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

plt.scatter(west_data['FGPCT'], west_data['FGA'], c=west_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('FGPCT')
plt.ylabel('FGA')
plt.title("WEST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

plt.scatter(west_data['FGPCT'], west_data['FGA'], c=west_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.scatter(east_data['FGPCT'], east_data['FGA'], c=east_playoff_data['PLAYOFF'].apply(lambda x: colors[x]))
plt.xlabel('FGPCT')
plt.ylabel('FGA')
plt.title("EAST AND WEST")
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.8)
plt.show()

print(np.corrcoef(east_data['FGPCT'], east_data['FGA']))
