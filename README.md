# NBA Playoff Prediction Algorithm (not done, will need to edit for word count/clarity)


## Introduction:

The NBA is the world’s most competitive professional basketball league and each of its 30 teams try to win the NBA championship every season. Our project goal is to create a model to accurately predict which NBA teams have the best chance to make the NBA playoffs and win the NBA championship.

NBA teams all want to make the playoffs to get a chance to win an NBA championship, but teams would like to know where they stand in relation to the rest of the teams in their respective conferences at the half point of the season. Our team is looking to use machine learning to predict the ranking of all teams at the end of the season so towards the end of the season, teams know what they need to do to get into the playoffs, or what they need to do to stay in the playoffs.


## Dataset

Kaggle Dataset: https://www.kaggle.com/datasets/wyattowalsh/basketball/discussion
The game.csv file in this dataset has information on all basketball games from 1946 until January 2023. We will only use the last 23 years of data. This dataset includes nearly every statistical metric (W/L, MIN, PTS, FGM, REB, AST, TOV, PF, +/-, and more) all of which can be used for our algorithms.

NBA official Website: https://www.nba.com/stats/teams/boxscores?dir=A&sort=TEAM_NAME
This dataset has all games and stats as presented by the NBA. Any games that cannot be accessed on the Kaggle Dataset (i.e. more recent games in 2023) can be loaded from here.


## Methods:

We have currently looked at 4 possible supervised-learning models that could be used for this project. Out of the 4, we are looking at implementing 2 or 3 models. We are still doing more research to figure out which models would be the best for us. 

  Logistic Regression: This model  gives us concrete binary results for events, based on input variables.

  SVM: This model allows for high dimensional feature vectors to predict game results. 

  K-Nearest Neighbor: This model allows for easy clustering of features and thus allows for a regression model to be created allowing for prediction of certain variables that could be used to further predict the outcome of games. 

  Random Forest: This model allows for a combination of several decision trees into a single model, letting us look at multiple events affecting the final prediction of which teams would make the payoff.


## Predicted Outcomes:

There are a large number of factors that dictate whether an NBA team will make it to the playoffs or not. Some factors cannot be shown within the statistics that we will put into our algorithms, such as team chemistry, mid-season trades, and morale. Therefore, most of the analysis that we will do will be purely quantitative and will contain data from previous seasons to counteract qualitative factors that can cause outliers in team performances. Using this purely quantitative data we can have the following potential results:

Team overperforms: This result occurs when a team performs better during the second half of the season than what the algorithm predicts. This result could occur for any number of reasons ranging from an addition of a star player to a change in coaching staff to a change in team chemistry. This result is usually not predicted by ML algorithms, but does not often occur within basketball. For example, our algorithm can predict that a team will make it to the playoffs based on first half statistics, and a team may not make the playoffs due to a decreased performance during the second half.

Team underperforms: When this result occurs, a team performs worse during the second half of the season than what the algorithm predicts.

Team performs at par: Team performs similar to how the algorithm predicts. 
	
A couple metrics we will explore are, home team advantage, win percentage, rebounds, assists, turnovers, steals, blocks, plus/minus score, offensive rating, defensive rating, and true shooting percentage.


## Gannt Chart/Timeline:

(INSERT SCREENSHOT OF COMPLETED GANNT CHART HERE)


## Video:

(INSERT LINK HERE)


## Scholarly References:

Kohli, Ikjyot Singh. “Finding Common Characteristics among NBA Playoff Teams: A Machine Learning Approach.” SSRN Electronic Journal, 2016, https://doi.org/10.2139/ssrn.2764396.

Ma, Nigel. “NBA Playoff Prediction Using Several Machine Learning Methods.” 2021 3rd International Conference on Machine Learning, Big Data and Business Intelligence (MLBDBI), Dec. 2021, https://doi.org/10.1109/mlbdbi54094.2021.00030. 

Wang, Jingru, and Qishi Fan. “Application of Machine Learning on NBA Data Sets.” Journal of Physics: Conference Series, vol. 1802, no. 3, 1 Mar. 2021, p. 032036, https://doi.org/10.1088/1742-6596/1802/3/032036. 


## Contributions:

Samuel - Found 3 references of similar studies that we can leverage for use throughout the project proposal. Also found a couple datasets we can use for training data

Avi - Defined the problem definition and cummulated background knowledge to provide to foundation for our algorithm. Also created our github repository. 

Divyesh - Structured the algorithm and defined which methods are useful in relation to the libraries and data available

Param - Worked on finishing the Gantt chart and assisted in the ideation for the results and Discussion

Saahas - Lead the overall discussion and results for the project and figured out the quantitative metrics that we will use to predict how useful the algorithm will be

