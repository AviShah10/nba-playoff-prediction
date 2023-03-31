# NBA Playoff Prediction Algorithm (MIDTERM)


## Introduction/Background:

The NBA is the world’s most competitive professional basketball league and each of its 30 teams try to win the NBA championship every season. Our project goal is to create a model to accurately predict which NBA teams have the best chance to make the NBA playoffs and win the championship. Our team is looking to use machine learning to predict the end ranking of teams by the halfway point, and find common traits in success so that teams can know what to improve to make the playoffs, or what they need to do to remain in the playoff picture.

## Problem Definition:

NBA teams all want to make the playoffs to get a chance to win an NBA championship, but teams would like to know where they stand in relation to the rest of the teams in their respective conferences at the half point of the season. Our team is looking to use machine learning to predict the ranking of all teams at the end of the season so towards the end of the season, teams know what they need to do to get into the playoffs, or what they need to do to stay in the playoffs.


## Data Collection:

Our data on a team's average statistics is from this [Kaggle dataset](https://www.kaggle.com/datasets/wyattowalsh/basketball/discussion), which has multiple different CSV’s for different basketball statistics. One of the CSV’s that we will use is the `game.csv` file which has information on all basketball games since 1946 and until January 2023. We downloaded this CSV from the Kaggle website and then used data processing to clean the data and only keep the years and features we need to train our models.

The Kaggle dataset we are using for season averages for teams does not include any data on whether or not a team made the playoffs. We need this data in train and test our models, so we decided to pull playoff data from [Basketball Reference](https://www.basketball-reference.com/), which we extracted through a web data scraper.

Additionally, the Kaggle dataset had no distinguishment between teams in the Eastern and Western Conferences, which have separate scheduling rules and playoffs. As a result, we decided to divide the Kaggle dataset into East and West subdatasets to run the algorithm on.


## Methods:

### Data Cleaning/Pre-processing

RELOCATED/EXPANDED TEAMS:
There were a few issues with the dataset in handling teams that moved cities and/or conferences, but Kaggle included a 'team_id' column which was used in querying to keep consistent with present day team names. 

CHARLOTTE/NEW ORLEANS:
A particularly difficult situation emerged as Charlotte was an eastern conference team in 2000, 2001, 2002, and 2003. It changed to New Orleans for 2004, 2005 but stayed in eastern conference. We removed the 2005 season's data due to midseason shift to a new city/conference but in 2004 New Orleans (NOP) was shifted to the east and the first few years only have 29 teams up until the expansion.

FEATURE EXTRACTION (MID-SEASON AVERAGES):
In the Kaggle dataset, we had a multi-step process for creating the statistical averages for each team at the midpoint of every season:
1. We first took a dataframe including every game from the 2000 season until 2022. 
2. We then divided it into 30 dataframes of each team's total games from 2000 to 2022. 
3. We divided each team's games into their respective seasons .
4. We then took the average of the first 41 games (first half) for each season. (NOTE: Since Kaggle did not have statistics for W/L%, we replaced the dataset's Win/Loss column values ('W', or 'L') with an int 1/0 that could be numerically averaged into a Win-loss percentage, and the Home/away location into an int 1/0 as well. 
5. Afterwards, we merged each of the season's team averages into separate east and west dataframes. The result was a dataframe for the east and west teams' statistical averages after half of the season had finished.
6. We sorted teams alphabetically (to stay consistent with the ordering for the playoff data from [Basketball Reference](https://www.basketball-reference.com/), and created a training set of data using seasons 2000-2019, and a testing set of data from 2020-2022.

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
  - Plus-minus points differential (PM)

FEATURE SELECTION:
We experimented with some backwards feature selection, particularly by removing some features that we believed to be less relevant (i.e. 'TEAM', 'YEAR', and 'MATCHUP' ratio, although we re-included 'MATCHUP') in order to see if it led to better results. We plan in the coming weeks to continue with backwards feature selection using research to determine what statistics are less relevant. We also plan to expand to include some additional features, using advanced metrics such as true shooting percentage, defensive efficience, etc. to see if those may also help with our model performance.


### Training Models

Thus far, we have created two models for predicting which NBA teams will be making the playoffs for any given season: a logistic regression model and a support vector machine (SVM) model.

For both our logistic regression and SVM models, we proceeded with the same following steps. We used the season averages for each team from the years 2000 (1999-2020 season) to 2020 (2019-2020 season) as the training data. We used the season averages for each team for the 2021 and 2022 seasons as training data for predicting the 2021 and 2022 playoffs, respectively. 

So far, we have ran the models on all features in our dataset including WLPCT, MATCHUP, FGM, FGA, FGPCT, FG3M, FG3A, FG3PCT, FTM, FTA, FTPCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS, PM. We omitted the TEAM and YEAR features because they do not have an impact on the performance of the team itself.

| TEAM | PLAYOFF | PREDICTION | PROBABILITY|
| ------------- | ------------- |
|12 |PHI       |1          |1    |0.997403|
|1   |BKN        |1           |1     |0.997387|
|9   |MIL        |1           |1     |0.997174|
|0   |ATL        |1           |1     |0.939988|
|7   |IND        |0           |1     |0.912472|
|13  |TOR        |0           |1     |0.845891|
|2   |BOS        |1           |1     |0.839305|
|8   |MIA        |1           |1     |0.813625|
|3   |CHA        |0           |1     |0.776989|
|10  |NYK        |1           |1     |0.748290|
|4   |CHI        |0           |1     |0.698376|
|14  |WAS        |1           |0     |0.331704|
|6   |DET        |0           |0     |0.220183|
|11  |ORL        |0           |0     |0.097384|
|5   |CLE        |0           |0     |0.066688|










## Results and Discussion:

Thus far, we have created two models for predicting which NBA teams will be making the playoffs for any given season: a logistic regression model and a support vector machine (SVM) model.

For both our logistic regression and SVM models, we proceeded with the same following steps. We used the season averages for each team from the years 2000 (1999-2020 season) to 2020 (2019-2020 season) as the training data. We used the season averages for each team for the 2021 and 2022 seasons as training data for predicting the 2021 and 2022 playoffs, respectively. 

So far, we have ran the models on all features in our dataset including WLPCT, MATCHUP, FGM, FGA, FGPCT, FG3M, FG3A, FG3PCT, FTM, FTA, FTPCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS, PM. We omitted the TEAM and YEAR features because they do not have an impact on the performance of the team itself.

Visualizations:
While creating our dataset we decided to run some visualizations to get an understanding of how the data is trending. Our next couple visualizations helps show a difference in many key features from playoff bound teams and non-playoff bound teams. 

RED indicates playoff clinch
BLUE indicares playoff miss

Below we see 3 charts, Field Goals Attempted by year for the East, Field Goals Attempted by year for the West & Field Goals Attempted by year for the East and West. Pre-2010 we see FGA fluctuate but mainly stay within its bounds. We have a couple outliers with teams experimenting different playing styles, which start to pick up in the coming years. As we look at the early 2010s, the FGAs start to increase but it isn't till around 2018 when the overall league average for FGA jumps. Infact within the 2020 season, most of the teams FGAs are above the teams from the 2000s. However when we look at the playoff clinching factor, there's no clear pattern for more Field Goals Attempted equating to making the playoffs.

<img width="281" alt="image" src="https://user-images.githubusercontent.com/126113216/229228470-982f26f9-c286-4f9a-a252-1acb4280b643.png">


Next, we explore how Field Goal Percentage for each team has an impact on those who make and dont make the playoffs. The next 3 charts are Field Goal Percentage by year for the East, Field Goal Percentage by year for the West & Field Goal Percentage by year for the East and West. Examining the FG%s by year, both the east and the west are a bit chaotic and a clear distinction can not be made pre-2010, however once we get past the 2010s, every year most of the teams that make the playoffs, have higher FG%s relative to those who were not able to make the playoffs. 

<img width="282" alt="image" src="https://user-images.githubusercontent.com/126113216/229227908-b23c509a-4e40-4fa2-b2a4-13ec479dc602.png">

This sparked some thought as we wanted to explore if 3pt shots had any indictor of making the playoffs. We explore 3 point field goal attempts (FG3A) & 3 point field goal percentage (FG3PCT) for the east and west in the next coupld of graphs. This has shown us that for the league, there has been a general increase in the last 10 years in FG3A, but not a huge differenciater for playoff success. We see a similar trend in FG3PCT as well. We see that in FG3PCT, the range of values becomes more narrow as time goes on and generally that there is no clear distinction in teams that make it to the playoffs based on this particular feature.

<img width="278" alt="image" src="https://user-images.githubusercontent.com/126113216/229228958-a04aad16-6266-4e09-8b46-ab02ee69b38a.png">
<img width="299" alt="image" src="https://user-images.githubusercontent.com/126113216/229229033-0abdee2a-11a3-4c01-8c28-95617c6228ea.png">



Moving onto the Defensive ability of a team, we would like to compare their Block and steals stats with those who made and did not make the playoffs. 
The next couple graphs explore this avenue. Overall, we see that for Blocks and Steals we have a very small subtle difference between those teams that make it compared to those that dont. While this could be a factor as to teams make the playoffs, this does not seem like the biggest driving force. 

<img width="262" alt="image" src="https://user-images.githubusercontent.com/126113216/229229180-baf73a25-44b2-48a8-aa9b-142533757c65.png">
<img width="263" alt="image" src="https://user-images.githubusercontent.com/126113216/229229234-fc70b9ac-1f84-4b57-8fd1-eb175e09a102.png">


Below, we look at how rebounds have an impact on a team's playoff success. In the earlier years, we see that there was a distinction with a couple of outliers, but as time moved forward, it became less definitive. Teams with a lot of rebounds didnt necessarily make the playoffs and those teams with less rebounds could still make it. Overall, currently, rebounds are not a good indicator of playoff sucess. 

<img width="269" alt="image" src="https://user-images.githubusercontent.com/126113216/229229309-6131f47d-64f5-45a5-abfa-1aa0600d1a51.png">


We wanted to see how Plus-minus points differential (PM) and Win-loss percentage (WLPCT) changed with time. We saw that both these factors were a clear indicator of Playoff attainment success. Regarding PM, there is a pretty clean cut at the 0 point with teams who have a Positive differencal, generally make the playoffs while those with negative differencials end up missing the playoffs. A similar distinction is made in Win-loss with teams higher than .5 end up making the playoffs and those who have a negative record end up missing the playoffs. 

<img width="273" alt="image" src="https://user-images.githubusercontent.com/126113216/229229361-b2c9a9d6-2dd3-4c7c-be4b-c07d8ba82995.png">
<img width="263" alt="image" src="https://user-images.githubusercontent.com/126113216/229229403-6f186943-2da9-404e-8d91-abfa16a7fecc.png">



In this plot, we compare 3 factors with eachother, WLPCT, PM & FGPCT.  We see that teams who did not make it tend to have negative WLPCT & PM and a lower FGPCT on the left of the chart, while teams who did make it tend to have positive WLPCT & PM and a higher FGPCT on the right of the chart. These are our top 3 indicators of playoff attainment success.

<img width="294" alt="image" src="https://user-images.githubusercontent.com/126113216/229229752-95b20e54-b152-4676-b6b9-7bb664876fa5.png">

## Scholarly References:

Kohli, Ikjyot Singh. “Finding Common Characteristics among NBA Playoff Teams: A Machine Learning Approach.” SSRN Electronic Journal, 2016, https://doi.org/10.2139/ssrn.2764396.

Ma, Nigel. “NBA Playoff Prediction Using Several Machine Learning Methods.” 2021 3rd International Conference on Machine Learning, Big Data and Business Intelligence (MLBDBI), Dec. 2021, https://doi.org/10.1109/mlbdbi54094.2021.00030. 

Wang, Jingru, and Qishi Fan. “Application of Machine Learning on NBA Data Sets.” Journal of Physics: Conference Series, vol. 1802, no. 3, 1 Mar. 2021, p. 032036, https://doi.org/10.1088/1742-6596/1802/3/032036. 


## Contributions (Midterm; for Project Proposal contributions please see the Proposal README):

Samuel: Was in charge of later data cleaning and processing, such as troubleshooting issues with conferences/team relocations, averaging the teams' midseason stats, and reshaping to be compatible with the learning models. Helped with the implementation of the models by fixing any errors that could be dealt with on the data side such as mismatching rows, incorrect labeling, etc. and contributed in writing the 'Data Collection' and 'Methods' sections of this report ...

Divyesh: Was in charge of the early data cleaning and processing. Experimented different techniques of cleaning ans storing data: by year or by team. Parsed through the game.csv file and took the 2000-2022 seasons and split into each team's games. Also helped with the creation and debugging of SVM and logistic regression models. 

Avi: Was in charge of the application of the learning models to the cleaned data. Implemented scikit.learn in python to train data to predict playoff results based on midseason averages. Was critically important in communicating any issues with the dataset that needed fixing, as well as helping interpret results for the analysis and graphs ...

Param: Was in charge of creating the visuals and the explanations for why these visuals are useful and what we will learn from them. Through this analysis, we gained a better understadning as to our goals/aims for the coming months. Was a huge contributor of writing the "Results and Discussion" of this report ...

Saahas: Was in charge of creating the python code for the visuals and helped with the explanations for why these visuals are useful and what learned from them. Created all the scatterplots and the 3-D graphs using matplotlib. Assisted with writing the "Results and Discussion" portion of this report, as well as helping interpret the results from the analysis and the plots ...


