# NBA Playoff Prediction Algorithm


## Introduction:

The NBA is the world’s most competitive professional basketball league and each of its 30 teams try to win the NBA championship every season. Our project goal is to create a model to accurately predict which NBA teams have the best chance to make the NBA playoffs and win the championship. Our team is looking to use machine learning to predict the end ranking of teams by the halfway point, and find common traits in success so that teams can know what to improve to make the playoffs, or what they need to do to remain in the playoff picture.


## Dataset

Kaggle Dataset: https://www.kaggle.com/datasets/wyattowalsh/basketball/discussion
The game.csv file in this dataset has information on all basketball games from 1946 until January 2023. We will only use the last 23 years of data. This dataset includes nearly every statistical metric (W/L, MIN, PTS, REB, AST, PF, +/-, and more), all of which can be used for our algorithms.

NBA Website: https://www.nba.com/stats/teams/boxscores?dir=A&sort=TEAM_NAME
This dataset has all official games and stats by the NBA. Any games that cannot be accessed on the Kaggle Dataset (i.e. more recent games in 2023) can be loaded here.


## Methods:

We have looked at 4 possible supervised-learning models that could be used for this project. Out of the 4, we are looking at implementing 2 or 3 models. We are still researching which models would be the best for us. 

  Logistic Regression: Gives us concrete binary results for events, based on input variables.

  SVM: Allows for high dimensional feature vectors to predict game results. 

  K-Nearest Neighbor: Allows for easy clustering of features and thus allows for a regression model to be created allowing for prediction of certain variables that could be used to further predict the outcome of games. 

  Random Forest: Allows for a combination of several decision trees into a single model, letting us look at multiple events affecting the final prediction of which teams would make the payoff.

There are many factors that could dictate an NBA team making the playoffs or not. Some cannot be shown via quantitative statistics in our algorithm (such as chemistry, trades, and morale). Therefore, the data we feed our models will be purely quantitative and use a large sample size across many seasons to counteract qualitative factors that can cause outliers in performances.

## Predicted Outcomes:

Using this data in our models we can have the following potential results when comparing with our model's predictions:

Team overperforms (i.e. makes playoffs when algorithm predicts no playoffs).

Team underperforms (i.e. misses playoffs when algorithm predicts playoffs).

Team performs at par (Team performs similar to how the algorithm predicts). 
	
Some metrics we will explore in our analysis are home team advantage, win percentage, rebounds, assists, turnovers, offensive/defensive rating, etc. and based on teams' actual/predicted success we can advise on which metrics must be improved on to maximize playoff likelihood.


## Gannt Chart/Timeline:

![image](https://user-images.githubusercontent.com/55326680/221089383-a7bd3974-044a-426d-a906-6c627b50a20c.png)
![image](https://user-images.githubusercontent.com/55326680/221089528-541dc8e8-1ec9-4a62-9ddc-d2047b305006.png)


## Video:

[(YouTube Link to 3-min Video)](https://youtu.be/IXE98mcphmQ)


## Scholarly References:

Kohli, Ikjyot Singh. “Finding Common Characteristics among NBA Playoff Teams: A Machine Learning Approach.” SSRN Electronic Journal, 2016, https://doi.org/10.2139/ssrn.2764396.

Ma, Nigel. “NBA Playoff Prediction Using Several Machine Learning Methods.” 2021 3rd International Conference on Machine Learning, Big Data and Business Intelligence (MLBDBI), Dec. 2021, https://doi.org/10.1109/mlbdbi54094.2021.00030. 

Wang, Jingru, and Qishi Fan. “Application of Machine Learning on NBA Data Sets.” Journal of Physics: Conference Series, vol. 1802, no. 3, 1 Mar. 2021, p. 032036, https://doi.org/10.1088/1742-6596/1802/3/032036. 


## Contributions:

Samuel - Found 3 references of similar studies that we can leverage for use throughout the project proposal. Also found a couple datasets we can use for training data and edited github page (was in video)

Avi - Defined the problem definition and cummulated background knowledge to provide to foundation for our algorithm. Also created our github repository and worked on script/slides for the video and github page

Divyesh - Structured the algorithm and defined which methods are useful in relation to the libraries and data available, and edited all parts of page for cohesiveness and to reach word count (was in video)

Param - Worked on finishing the Gantt chart and assisted in the ideation for the results and Discussion. Discussed overall purpose and useful applications of algorithm (was in video)

Saahas - Lead the overall discussion and results for the project and figured out the quantitative metrics that we will use to predict how useful the algorithm will be, and worked on slides/script for video
