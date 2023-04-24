# NBA Playoff Prediction Algorithm (MIDTERM)


## Introduction/Background:

The NBA is the world’s most competitive professional basketball league and each of its 30 teams try to win the NBA championship every season. Our project goal is to create a model to accurately predict which NBA teams have the best chance to make the NBA playoffs and win the championship. Our team is looking to use machine learning to predict the end ranking of teams by the halfway point, and find common traits in success so that teams can know what to improve to make the playoffs, or what they need to do to remain in the playoff picture.

## Problem Definition:

NBA teams all want to make the playoffs to get a chance to win an NBA championship, but teams would like to know where they stand in relation to the rest of the teams in their respective conferences at the half point of the season. Our team is looking to use machine learning to predict the ranking of all teams at the end of the season so towards the end of the season, teams know what they need to do to get into the playoffs, or what they need to do to stay in the playoffs.


## Data Collection:

Our data on a team's average statistics is from this [Kaggle dataset](https://www.kaggle.com/datasets/wyattowalsh/basketball/discussion), which has multiple different CSV’s for different basketball statistics. One of the CSV’s that we will use is the `game.csv` file which has information on all basketball games since 1946 and until January 2023. We downloaded this CSV from the Kaggle website and then used data processing to clean the data and only keep the years and features we need to train our models.

The Kaggle dataset we are using for season averages for teams does not include any data on whether or not a team made the playoffs. We need this data in train and test our models, so we decided to pull playoff data from [Basketball Reference](https://www.basketball-reference.com/), which we extracted through a web data scraper.


## Methods:

### Data Cleaning/Pre-processing

CHARLOTTE/NEW ORLEANS:
Charlotte was an eastern conference team in 2000, 2001, 2002. Changed to New Orleans for 2003, 2004 but stayed in eastern conference. We removed 2004 due to midseason shift but in 2003 New Orleans (NOP) was shifted to the east and the first few years only have 29 teams up until the expansion.

Features we parsed and kept from the Kaggle dataset:

- Win-loss percentage (WLPCT)
- Home versus away game ratio (MATCHUP)
- Field goal makes (FGM)
- Field goal attempts (FGA)
- Field goal percentage (FGPCT)
- 3 point field goal makes (FG3M)
- 3 point field goal attempts (FG3A)
- 3 point field goal percentage (FG3PCT)
- Free throw makes (FTM)
- Free throw attempts (FTA)
- Free throw percentage (FTPCT)
- Offensive rebounds (OREB)
- Defensive rebounds (DREB)
- Rebounds (REB)
- Assists (AST)
- Steals (STL)
- Blocks (BLK)
- Turnovers (TOV)
- Personal fouls (PF)
- Points (PTS)
- Plus-minus ratio (PM)

### Training Models

Thus far, we have created two models for predicting which NBA teams will be making the playoffs for any given season: a logistic regression model and a support vector machine (SVM) model.

For both our logistic regression and SVM models, we proceeded with the same following steps. We used the season averages for each team from the years 2000 (1999-2020 season) to 2020 (2019-2020 season) as the training data. We used the season averages for each team for the 2021 and 2022 seasons as training data for predicting the 2021 and 2022 playoffs, respectively. 

So far, we have ran the models on all features in our dataset including WLPCT, MATCHUP, FGM, FGA, FGPCT, FG3M, FG3A, FG3PCT, FTM, FTA, FTPCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS, PM. We omitted the TEAM and YEAR features because they do not have an impact on the performance of the team itself.

## Results and Discussion:

REQUIREMENTS AS PER THE ASSIGNMENT DESCRIPTION:
We expect to see data pre-processing in your project such as feature selection (Forward or backward feature selection, dimensionality reduction methods such as PCA, Lasso, LDA, .. ), taking care of missing features in your dataset, …
We expect to see at least one supervised or unsupervised method implemented and the results need to be studied in details. For example evaluating your predictive model performance using different metrics (take a look at ML Metrics)
You MUST include visualizations of your dataset (if possible) and your results. Visualizations include graphs, charts, tables. Code snippets do not count as visualizations. You can use Matplotlib or Seaborn to create your visualizations. We recommend using Plotly for interactive visualizations in Python as well as interactive visualizations on your website.
(PLEASE FILL THIS WITH NECESSARY FIGURES, ETC.)

## Scholarly References:

Kohli, Ikjyot Singh. “Finding Common Characteristics among NBA Playoff Teams: A Machine Learning Approach.” SSRN Electronic Journal, 2016, https://doi.org/10.2139/ssrn.2764396.

Ma, Nigel. “NBA Playoff Prediction Using Several Machine Learning Methods.” 2021 3rd International Conference on Machine Learning, Big Data and Business Intelligence (MLBDBI), Dec. 2021, https://doi.org/10.1109/mlbdbi54094.2021.00030. 

Wang, Jingru, and Qishi Fan. “Application of Machine Learning on NBA Data Sets.” Journal of Physics: Conference Series, vol. 1802, no. 3, 1 Mar. 2021, p. 032036, https://doi.org/10.1088/1742-6596/1802/3/032036. 


## Contributions:


