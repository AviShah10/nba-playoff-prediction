# NBA Playoff Prediction Algorithm


## Introduction/Background:

The NBA is the world’s most competitive professional basketball league and each of its 30 teams try to win the NBA championship every season. Our project goal is to create a model to accurately predict which NBA teams have the best chance to make the NBA playoffs and win the championship. Our team is looking to use machine learning to predict the end ranking of teams by the halfway point, and find common traits in success so that teams can know what to improve to make the playoffs, or what they need to do to remain in the playoff picture.

## Problem Definition:

NBA teams all want to make the playoffs to get a chance to win an NBA championship, but teams would like to know where they stand in relation to the rest of the teams in their respective conferences at the half point of the season. Our team is looking to use machine learning to predict the ranking of all teams at the end of the season so that in the middle of the season, teams know what they need to do to get into the playoffs, or what they need to do to stay in the playoffs.


## Data Collection:

Our data on a team's average statistics is from this [Kaggle dataset](https://www.kaggle.com/datasets/wyattowalsh/basketball/discussion), which has multiple different CSV’s for different basketball statistics. One of the CSV’s that we will use is the `game.csv` file which has information on all basketball games since 1946 and until January 2023. We downloaded this CSV from the Kaggle website and then used data processing to clean the data and only keep the years and features we need to train our models.

The Kaggle dataset we are using for season averages for teams does not include any data on whether or not a team made the playoffs. We need this data in train and test our models, so we decided to pull playoff data from [Basketball Reference](https://www.basketball-reference.com/), which we extracted through a web data scraper.

Additionally, the Kaggle dataset had no distinguishment between teams in the Eastern and Western Conferences, which have separate scheduling rules and playoffs. As a result, we decided to divide the Kaggle dataset into East and West subdatasets to run the algorithm on.


## Methods:

### Data Cleaning/Pre-processing

#### Relocated/Expanded Teams
There were a few issues with the dataset in handling teams that moved cities and/or conferences, but Kaggle included a 'team_id' column which was used in querying to keep consistent with present day team names. 

##### Charlotte/New Oreleans
A particularly difficult situation emerged as Charlotte was an eastern conference team in 2000, 2001, 2002, and 2003. It changed to New Orleans for 2004, 2005 but stayed in eastern conference. We removed the 2005 season's data due to midseason shift to a new city/conference but in 2004 New Orleans (NOP) was shifted to the east and the first few years only have 29 teams up until the expansion.

#### Feature Extraction (Mid-Season Averages)
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

#### Feature Selection

We experimented with some backwards feature selection, particularly by removing some features that we believed to be less relevant (i.e. 'TEAM', 'YEAR', and 'MATCHUP' ratio, although we re-included 'MATCHUP') in order to see if it led to better results. We also used Principle Component Analysis (PCA) on our dataset for diminsionality reduction on our selected feature set, although it did not seem to benefit results very much, as it seems most NBA statistics are quite intertwined with performance and are all at least somewhat necessary to predict success.


### Training Models

We have created four supervised learning models for predicting which NBA teams will be making the playoffs for any given season: a logistic regression model and a support vector machine (SVM) model, a Random Forest Classifier model, and a Decision Tree Classifier model.

For all four of our supervised learning models, we proceeded with the same following steps. We used the mid-season averages for each team from the years 2000 (1999-2020 season) to 2020 (2019-2020 season) as the training data. We used the mid-season averages for each team for the 2021 and 2022 seasons as training data for predicting the 2021 and 2022 playoffs, respectively.

We have ran the models on all features in our dataset including WLPCT, MATCHUP, FGM, FGA, FGPCT, FG3M, FG3A, FG3PCT, FTM, FTA, FTPCT, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS, PM. We omitted the TEAM and YEAR features because they do not have an impact on the performance of the team itself.


## Results and Discussion:

### Feature Correlation Matrix

To initially visualize our feature set, we created a feature correlation matrix that quantifies the relationship between the different features. It quantifies the strength of the relationship between various features and the direction of their relation (positive or negative). Our main objective to construct the matrix is to find the features that are affecting the chance of a team making the playoffs, thus, our target variable will be playoff, telling us whether the team made the playoff or not.

The column we will be focusing on is the one that has been highlighted with the green box, which looks at the correlation between our feature set and whether or not a team makes the playoffs. There are certain features that are positively correlated with the playoff target variable, including the PM, WLPCT, and FGPCT feature. This means that a higher PM ratio, higher WLPCT, and higher FGPCT are positively correlated with the chances a team has to make the playoffs. On the other hand, there are other features that are negatively correlated with the playoff target variable, including TOV. This means that a lower TOV rate also increases a team's chances of making the playoffs.

In general, the feature correlation matrix helped narrow down the features that we would focus on, simplifying some of our models and helped us gain a greater understanding about the underlying patterns in the dataset.

<img width="1200" alt="image" src="correlation_matrix.jpeg" height="400">

### Visualizations

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

### Results

#### Logistic Regression

<img width="800" alt="image" src="results/LRResults.png">

#### Support Vector Machine

<img width="800" alt="image" src="results/SVMResults.png">

#### Random Forest Classifier

<img width="800" alt="image" src="results/RFResults.png">

#### Decision Tree Classifier

<img width="800" alt="image" src="results/DTResults.png">


#### Playoff Predictions

|2021 Predictions|2022 Predictions  |
|-------------|-------------|
|<img width="500" alt="image" src="confusion_matrix/Screen Shot 2023-04-24 at 11.49.36 PM.png">   |<img width="500" alt="image" src="confusion_matrix/Screen Shot 2023-04-24 at 11.50.04 PM.png">        |

From the results shown above, each model predicted whether a team would make playoffs marked with a 1 = make playoffs, 0 = miss playoffs. These results were compared with the actual results. Some models predicted more teams than were possible to make the playoffs (8), due to the model having multiple teams with a probability that exceeded 50% chance of making the posteseason.

#### Confusion Matrices

Logistic Regression:

  <img width="294" alt="image" src="confusion_matrix/LR_cm.jpeg">
  
  Accuracy = (11+31)/(11+17+1+31) = 0.73
  
  Precision = 11/(11+1) = 0.92
  
  Recall = 11/(11+17) = 0.39
  
  F1-score = 2 * (precision * recall) / (precision + recall) = 0.54
  
SVM:

  <img width="294" alt="image" src="confusion_matrix/SVM_cm.jpeg">
  
  Accuracy = (12+31)/(12+16+1+31) = 0.75
  
  Precision = 12/(12+1) = 0.92
  
  Recall = 12/(12+16) = 0.43
  
  F1-score = 2 * (precision * recall) / (precision + recall) = 0.58
  
Decision Tree:

  <img width="294" alt="image" src="confusion_matrix/DT_cm.jpeg">
  
  Accuracy = (19+27)/(19+9+5+27) = 0.78
  
  Precision = 19/(19+5) = 0.79
  
  Recall = 19/(19+9) = 0.68
  
  F1-score = 2 * (precision * recall) / (precision + recall) = 0.73
  
Random Forest:

  <img width="294" alt="image" src="confusion_matrix/RF_cm.jpeg">
  
  Accuracy = (17+30)/(17+11+2+30) = 0.81
  
  Precision = 17/(17+2) = 0.89
  
  Recall = 17/(17+11) = 0.61
  
  F1-score = 2 * (precision * recall) / (precision + recall) = 0.72

<!-- <img width="500" alt="image" src="confusion_matrix/Screen Shot 2023-04-24 at 11.49.36 PM.png"> -->
<!-- <img width="500" alt="image" src="confusion_matrix/Screen Shot 2023-04-24 at 11.50.04 PM.png"> -->

### Discussion

Our best logistic regression model was the 2021 Western Conference logistic regression model and the worst models were the 2021 and 2021 Eastern Conference models. The most important features were positive PM ratio, higher WLPCT, and higher FGPCT, all of which match the results from our data vizualizations and feature correlation matrix.

Our best SVM models were the 2021 and 2022 Western Conference SVM models and the worst model was the 2021 Eastern Conference model. In our SVM models, one interesting thing we noticed is that after a positive PM ratio and higher WLPCT, the next important features were different stats including a negative TOV rate and a positive STL rate. These defensive statistic trends also match up with our initial data visualizations and our feature correlation matrix.

The rest of our logistic regression and SVM models predict more playoff teams than there should be due to the algorithms basing playoff predictions off of a probability threshold (> 0.5). As a result, our algorithm is often less accurate than it could be than if it were to take the top 8 probabilities, but we wanted to display the actual probabilities and decisionmaking of our algorithm. We also know that our models are often overfitting the playoff predictions because the calculated training accuracy scores are greater than the testing accuracy scores for our models. This overfitting is likely due to the fact that our different splits of training and testing data may be too large. We trained our models on years 2000-2020 and tested our models on 2021 and 2022, and these splits may be too large. With the addition of more seasons, we could be able to expand our training and testing data splits to be larger and eliminate overfitting.

Our best Random Forest model was the 2021 Western Conference model and the worst models were the 2021 and 2022 Eastern Conference models. In addition to the normal positive PM ratio and higher WLPCT, higher FGPCT and higher FG3PCT were also calculated to be the most important features. In our initial data visualizations, we noticed that 3 point shooting has drastically increased in the recent NBA seasons which is confirmed by our Random Forest Models.

Our best Decision Tree models were the Western Conference models and the worst models were the Eastern Conference models. Across all four models, we noticed that test accuracies for the Eastern Conference have generally been worse than for the Western Conference. We believe that this is likely due to the fact that the Eastern Conference is generally more balanced and there is less entropy compared to the Western Conference, making it harder to predict.

When initially creating Decision Tree models, we did not tune any hyperparameters such as max_depth, max_features, min_samples_leaf, etc. which led to poor results for all Decision Tree models. Thus, we used the GridSearchCV module from scikit-learn to cross-validate the most optimal set of hyperparameters for each model (for each conference and season). We created a dictionary of hyperparameters to choose from for the max_depth, max_features, and min_samples_leaf hyperparameters. We then created a GridSearchCV object with set fields including a Decision Tree model, the dictionary of hyperparameters, the cross-validation splitting strategy, and the scoring strategy. After fitting the GridSearchCV object with our training data, we determined the optimal set of hyperparameters and then created a new DecisionTreeClassifier object with the new optimal hyperparameters set. Each conference and each season called for a different set of optimal hyperparameters, but each model was improved in terms of test accuracy score.

Overall, the best performing models were the Random Forest models for both the 2021 and 2022 seasons. The training and testing accuracies were both greater than 0.85 for both of these models. Decision Trees and SVM also had decent results, with SVM having the least overfitting issues, since the difference between testing and training scores was the smallest, and testing scores often overperformed. Logistic regression performed decently, but was consistently lower in testing data.

Overall, the top two features across all models for each season were high WLPCT and high PM ratio. This both makes sense intuitively and also matches the analysis from our visualizations of the WLPCT and PM statistics as well as the correlation matrix. Teams with above 0.500 WLPCT and a positive PM ratio often make the playoffs while teams with the opposite tend to miss the playoffs. Other important features include high FGPCT, high STL, low TOV, and high FGA. This also matches the analysis from our visualizations as we see that teams with high FGPCT and FGA and better defensive statistics are more likely to make the playoffs.

For all models, we also scaled and normalized our feature data, which made each performance statistic and feature normalized and comparable across each season. To scale and normalize our dataset, we used the StandardScaler object from scikit-learn and then used the fit_transform and normalize functions to scale and normalize the data. Before we scaled and normalized the data, our model performance was weaker with respect to test accuracy scores, so adding this data transformation was helpful across all models.

We tried using PCA for dimensionality reduction on all of our models to reduce features from our dataset, but the models run with PCA all had worse testing and training accuracy scores. We initialized a PCA object with assigning a value for the `n_components` value equal to 0.95, which means that PCA will select the optimal number of components such that the 95% of the variance in the data is preserved. Below is a plot for vizualizing the explained variance ratio of the principle components left after running PCA on our data:

<img width="600" alt="image" src="confusion_matrix/PCA.png">

For further analysis we created confusion matrices for all four different models: Logistic Regression, SVM, Decision Tree, and Random Forest. Each matrix showed the performance of the model in predicting whether a team would make the playoffs or not, based on the known truth (actual results) for the years 2021 and 2022.

After analyzing the confusion matrices, evaluation metrics such as accuracy, precision, recall, and F1-score were calculated for each model. The accuracy represents the ratio of correct predictions to the total number of samples. Precision measures the percentage of correct positive predictions out of all positive predictions made by the model. Recall measures the percentage of true positive predictions out of all actual positive samples. The F1-score is a harmonic mean of precision and recall.

Overall, the best models based on our confusion matrices were the Random Forest and Decision Tree classifier models with accuracy scores greater than 78% and F1-scores of greater than 73%. Another interesting trend we notices is that there were more false positives than false negatives, which is likely due to overfitting, especially for our logistic regression and SVM models.

#### Model Comparison

|Algorithm|Accuracy  |
|-------------|-------------|
|Logistic Regression   |0.72        |
|Support Vector Machine  |0.80        |
|Random Forest Classifier  |0.87        |
|Decision Tree Classifier   |0.80        |

Overall, the Random Forest Classifier and Decision Tree Classifier models most likely performed better than the Logistic Regression and Support Vector Machine models because of the non-linear relationships between most of the features in our dataset. Predicting which teams make the playoffs for any given conference in any given season is difficult because each conference has different characteristics and each team’s success is different by conference and season. Due to this non-linearity across seasons and conferences, Random Forest and Decision Tree classifiers generally perform better because they can capture such non-linear relationships between features. This happens through partitioning the different sets of features into smaller regions and fitting a simple classification model to each region. On the other hand, Logistic Regression and Support Vector Machine models assume a linear relationship which is why the training data from the 2000-2020 seasons may not necessarily correspond linearly to the feature sets for the 2021 and 2022 seasons.

### Future Work

To further improve our existing models, we would like to use different sets of features when training and testing. Currently, we are only testing our models with all features as mentioned above. We would like to include other advanced statistics that are not tracked in the Kaggle dataset that we chose to get all of our data from. The NBA tracks advanced statistics such as offensive rating (OFFRTG), defensive rating (DEFRTG), effective field-goal percentage (eFG%), true shooting percentage (TS%), and points per possession (PPP). These statistics are computed through several calculations that take into account the different statistics that are normally kept track of, like the features used in our project. These statistics may lead to more accurate algorithms because they scale and normalize simple statistics that are optimal across the NBA. This would give us more features to test our models on and give us the ability to remove more features that do not have any correlation to a team’s playoff chances.

We also want to integrate non-statistical factors in playoff success, such as player-specific information due to midseason trades, MVP votegetters, All star players, and recent momentum to see how this can impact playoff success.

We also may switch from a probability threshold prediction basis to one of taking the top 8 teams' likelihoods, as this would avoid our issue of some models predicting more or less playoff teams than is possible.

We also would like to build a neural network in the future due to the ability of a neural network to capture more abstract correlations between features. Predicting the NBA Playoffs has proven to be a difficult task, so the use of a neural network and tuning hyperparameters could result in a more accurate model for predicting playoff teams. Neural networks also have more flexibility with parameters, which means we can use our existing features combined with more advanced statistics to produce a model with higher accuracy.


## Youtube Link to Presentation:

 https://youtu.be/1txURXwxewM

## Scholarly References:

Kohli, Ikjyot Singh. “Finding Common Characteristics among NBA Playoff Teams: A Machine Learning Approach.” SSRN Electronic Journal, 2016, https://doi.org/10.2139/ssrn.2764396.

Ma, Nigel. “NBA Playoff Prediction Using Several Machine Learning Methods.” 2021 3rd International Conference on Machine Learning, Big Data and Business Intelligence (MLBDBI), Dec. 2021, https://doi.org/10.1109/mlbdbi54094.2021.00030. 

Wang, Jingru, and Qishi Fan. “Application of Machine Learning on NBA Data Sets.” Journal of Physics: Conference Series, vol. 1802, no. 3, 1 Mar. 2021, p. 032036, https://doi.org/10.1088/1742-6596/1802/3/032036. 


## Contributions

Samuel: Was in charge of later data cleaning and processing, such as troubleshooting issues with conferences/team relocations, averaging the teams' midseason stats, and reshaping to be compatible with the learning models. Helped with the implementation of the models by fixing any errors that could be dealt with on the data side such as mismatching rows, incorrect labeling, etc. and contributed in writing the 'Data Collection' and 'Methods' sections of this report. Also helped with organizing the results for each of the models with regards to the successes and failures in predicting playoff outcomes. Helped in analyzing code and converting files to notebook files and with the presentation recording.

Divyesh: Was in charge of the early data cleaning and processing. Experimented different techniques of cleaning ans storing data: by year or by team. Parsed through the game.csv file and took the 2000-2022 seasons and split into each team's games. Also helped with the creation and debugging of SVM and logistic regression models. 

Avi: Was in charge implementing all of the supervised learning models including Logistic Regression, SVM, Random Forest, and Decision Tree models to predict playoff results based on midseason averages. Calculated all predictions for playoffs, most important features, and model accuracy scores using the Logistic Regression, SVM, Random Forest, and Decision Tree models. Was critically important in communicating any issues with the dataset that needed fixing, as well as helping interpret results for the analysis and graphs. Contributed to Results, Playoff Predictions, Discussion, Model Comparison, and Future Work sections of the report. Wrote the corresponding slides for video presentation as well. Organized final report as a whole and moved sections around to make report complete.

Param: Was in charge of creating the visuals and the explanations for why these visuals are useful and what we will learn from them. Through this analysis, we gained a better understadning as to our goals/aims for the coming months. Was a huge contributor of writing the visualization portion of the "Results and Discussion" section of this report.

Saahas: Was in charge of creating the python code for the visuals and helped with the explanations for why these visuals are useful and what learned from them. Created all the scatterplots and the 3-D graphs using matplotlib. Was insightful in figuring out which features were the best to base our model around. Assisted with writing the visualization portion and the model results portions of the "Results and Discussion" section of this report, as well as helping interpret the results from the analysis and the plots. Was important in communicating any errors or issues within the dataset, and contributed to the Introuction/Background, Problem Definition, Feature Correlation Matrix, and Feature Visualization within the Final Report. Wrote the corresponding slides for the video presentation and talked within the video presentation explaining all about the slides mentioned above. 


