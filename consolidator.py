#Script that merges east, west dataframes into single dataframe for all testing and validation
import pandas as pd
import os
import numpy as np
import statgetter

trainingyears = [2000, 2001, 2002, 2003, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
validationyears = [2020, 2021, 2022]

#Load all csv's for training
east2000 = pd.read_csv('./season_stats/east2000.csv', index_col=None)
east2000['SEASON'] = 2000
east2001 = pd.read_csv('./season_stats/east2001.csv', index_col=None)
east2001['SEASON'] = 2001
east2002 = pd.read_csv('./season_stats/east2002.csv', index_col=None)
east2002['SEASON'] = 2002
east2003 = pd.read_csv('./season_stats/east2003.csv', index_col=None)
east2003['SEASON'] = 2003
east2005 = pd.read_csv('./season_stats/east2005.csv', index_col=None)
east2005['SEASON'] = 2005
east2006 = pd.read_csv('./season_stats/east2006.csv', index_col=None)
east2006['SEASON'] = 2006
east2007 = pd.read_csv('./season_stats/east2007.csv', index_col=None)
east2007['SEASON'] = 2007
east2008 = pd.read_csv('./season_stats/east2008.csv', index_col=None)
east2008['SEASON'] = 2008
east2009 = pd.read_csv('./season_stats/east2009.csv', index_col=None)
east2009['SEASON'] = 2009
east2010 = pd.read_csv('./season_stats/east2010.csv', index_col=None)
east2010['SEASON'] = 2010
east2011 = pd.read_csv('./season_stats/east2011.csv', index_col=None)
east2011['SEASON'] = 2011
east2012 = pd.read_csv('./season_stats/east2012.csv', index_col=None)
east2012['SEASON'] = 2012
east2013 = pd.read_csv('./season_stats/east2013.csv', index_col=None)
east2013['SEASON'] = 2013
east2014 = pd.read_csv('./season_stats/east2014.csv', index_col=None)
east2014['SEASON'] = 2014
east2015 = pd.read_csv('./season_stats/east2015.csv', index_col=None)
east2015['SEASON'] = 2015
east2016 = pd.read_csv('./season_stats/east2016.csv', index_col=None)
east2016['SEASON'] = 2016
east2017 = pd.read_csv('./season_stats/east2017.csv', index_col=None)
east2017['SEASON'] = 2017
east2018 = pd.read_csv('./season_stats/east2018.csv', index_col=None)
east2018['SEASON'] = 2018
east2019 = pd.read_csv('./season_stats/east2019.csv', index_col=None)
east2019['SEASON'] = 2019

west2000 = pd.read_csv('./season_stats/west2000.csv', index_col=None)
west2000['SEASON'] = 2000
west2001 = pd.read_csv('./season_stats/west2001.csv', index_col=None)
west2001['SEASON'] = 2001
west2002 = pd.read_csv('./season_stats/west2002.csv', index_col=None)
west2002['SEASON'] = 2002
west2003 = pd.read_csv('./season_stats/west2003.csv', index_col=None)
west2003['SEASON'] = 2003
west2005 = pd.read_csv('./season_stats/west2005.csv', index_col=None)
west2005['SEASON'] = 2005
west2006 = pd.read_csv('./season_stats/west2006.csv', index_col=None)
west2006['SEASON'] = 2006
west2007 = pd.read_csv('./season_stats/west2007.csv', index_col=None)
west2007['SEASON'] = 2007
west2008 = pd.read_csv('./season_stats/west2008.csv', index_col=None)
west2008['SEASON'] = 2008
west2009 = pd.read_csv('./season_stats/west2009.csv', index_col=None)
west2009['SEASON'] = 2009
west2010 = pd.read_csv('./season_stats/west2010.csv', index_col=None)
west2010['SEASON'] = 2010
west2011 = pd.read_csv('./season_stats/west2011.csv', index_col=None)
west2011['SEASON'] = 2011
west2012 = pd.read_csv('./season_stats/west2012.csv', index_col=None)
west2012['SEASON'] = 2012
west2013 = pd.read_csv('./season_stats/west2013.csv', index_col=None)
west2013['SEASON'] = 2013
west2014 = pd.read_csv('./season_stats/west2014.csv', index_col=None)
west2014['SEASON'] = 2014
west2015 = pd.read_csv('./season_stats/west2015.csv', index_col=None)
west2015['SEASON'] = 2015
west2016 = pd.read_csv('./season_stats/west2016.csv', index_col=None)
west2016['SEASON'] = 2016
west2017 = pd.read_csv('./season_stats/west2017.csv', index_col=None)
west2017['SEASON'] = 2017
west2018 = pd.read_csv('./season_stats/west2018.csv', index_col=None)
west2018['SEASON'] = 2018
west2019 = pd.read_csv('./season_stats/west2019.csv', index_col=None)
west2019['SEASON'] = 2019

#Merge into one dataframe
eastTrainingData = pd.concat([east2000, east2001, east2002, east2003, east2005, east2006, east2007, east2008, east2009, east2010, east2011, east2012, east2013, east2014, east2015, east2016, east2017, east2018, east2019])
westTrainingData = pd.concat([west2000, west2001, west2002, west2003, west2005, west2006, west2007, west2008, west2009, west2010, west2011, west2012, west2013, west2014, west2015, west2016, west2017, west2018, west2019])

eastTrainingData = eastTrainingData.sort_values(by=['SEASON', 'TEAM'])
westTrainingData = westTrainingData.sort_values(by=['SEASON', 'TEAM'])

eastTrainingData.to_csv('./eastTrainingData.csv')
westTrainingData.to_csv('./westTrainingData.csv')

#Load playoff data for training
east2000playoff = pd.read_csv('./playoff_labels/east2000playoff.csv', index_col=None)
east2000playoff['SEASON'] = 2000
east2001playoff = pd.read_csv('./playoff_labels/east2001playoff.csv', index_col=None)
east2001playoff['SEASON'] = 2001
east2002playoff = pd.read_csv('./playoff_labels/east2002playoff.csv', index_col=None)
east2002playoff['SEASON'] = 2002
east2003playoff = pd.read_csv('./playoff_labels/east2003playoff.csv', index_col=None)
east2003playoff['SEASON'] = 2003
east2005playoff = pd.read_csv('./playoff_labels/east2005playoff.csv', index_col=None)
east2005playoff['SEASON'] = 2005
east2006playoff = pd.read_csv('./playoff_labels/east2006playoff.csv', index_col=None)
east2006playoff['SEASON'] = 2006
east2007playoff = pd.read_csv('./playoff_labels/east2007playoff.csv', index_col=None)
east2007playoff['SEASON'] = 2007
east2008playoff = pd.read_csv('./playoff_labels/east2008playoff.csv', index_col=None)
east2008playoff['SEASON'] = 2008
east2009playoff = pd.read_csv('./playoff_labels/east2009playoff.csv', index_col=None)
east2009playoff['SEASON'] = 2009
east2010playoff = pd.read_csv('./playoff_labels/east2010playoff.csv', index_col=None)
east2010playoff['SEASON'] = 2010
east2011playoff = pd.read_csv('./playoff_labels/east2011playoff.csv', index_col=None)
east2011playoff['SEASON'] = 2011
east2012playoff = pd.read_csv('./playoff_labels/east2012playoff.csv', index_col=None)
east2012playoff['SEASON'] = 2012
east2013playoff = pd.read_csv('./playoff_labels/east2013playoff.csv', index_col=None)
east2013playoff['SEASON'] = 2013
east2014playoff = pd.read_csv('./playoff_labels/east2014playoff.csv', index_col=None)
east2014playoff['SEASON'] = 2014
east2015playoff = pd.read_csv('./playoff_labels/east2015playoff.csv', index_col=None)
east2015playoff['SEASON'] = 2015
east2016playoff = pd.read_csv('./playoff_labels/east2016playoff.csv', index_col=None)
east2016playoff['SEASON'] = 2016
east2017playoff = pd.read_csv('./playoff_labels/east2017playoff.csv', index_col=None)
east2017playoff['SEASON'] = 2017
east2018playoff = pd.read_csv('./playoff_labels/east2018playoff.csv', index_col=None)
east2018playoff['SEASON'] = 2018
east2019playoff = pd.read_csv('./playoff_labels/east2019playoff.csv', index_col=None)
east2019playoff['SEASON'] = 2019

west2000playoff = pd.read_csv('./playoff_labels/west2000playoff.csv', index_col=None)
west2000playoff['SEASON'] = 2000
west2001playoff = pd.read_csv('./playoff_labels/west2001playoff.csv', index_col=None)
west2001playoff['SEASON'] = 2001
west2002playoff = pd.read_csv('./playoff_labels/west2002playoff.csv', index_col=None)
west2002playoff['SEASON'] = 2002
west2003playoff = pd.read_csv('./playoff_labels/west2003playoff.csv', index_col=None)
west2003playoff['SEASON'] = 2003
west2005playoff = pd.read_csv('./playoff_labels/west2005playoff.csv', index_col=None)
west2005playoff['SEASON'] = 2005
west2006playoff = pd.read_csv('./playoff_labels/west2006playoff.csv', index_col=None)
west2006playoff['SEASON'] = 2006
west2007playoff = pd.read_csv('./playoff_labels/west2007playoff.csv', index_col=None)
west2007playoff['SEASON'] = 2007
west2008playoff = pd.read_csv('./playoff_labels/west2008playoff.csv', index_col=None)
west2008playoff['SEASON'] = 2008
west2009playoff = pd.read_csv('./playoff_labels/west2009playoff.csv', index_col=None)
west2009playoff['SEASON'] = 2009
west2010playoff = pd.read_csv('./playoff_labels/west2010playoff.csv', index_col=None)
west2010playoff['SEASON'] = 2010
west2011playoff = pd.read_csv('./playoff_labels/west2011playoff.csv', index_col=None)
west2011playoff['SEASON'] = 2011
west2012playoff = pd.read_csv('./playoff_labels/west2012playoff.csv', index_col=None)
west2012playoff['SEASON'] = 2012
west2013playoff = pd.read_csv('./playoff_labels/west2013playoff.csv', index_col=None)
west2013playoff['SEASON'] = 2013
west2014playoff = pd.read_csv('./playoff_labels/west2014playoff.csv', index_col=None)
west2014playoff['SEASON'] = 2014
west2015playoff = pd.read_csv('./playoff_labels/west2015playoff.csv', index_col=None)
west2015playoff['SEASON'] = 2015
west2016playoff = pd.read_csv('./playoff_labels/west2016playoff.csv', index_col=None)
west2016playoff['SEASON'] = 2016
west2017playoff = pd.read_csv('./playoff_labels/west2017playoff.csv', index_col=None)
west2017playoff['SEASON'] = 2017
west2018playoff = pd.read_csv('./playoff_labels/west2018playoff.csv', index_col=None)
west2018playoff['SEASON'] = 2018
west2019playoff = pd.read_csv('./playoff_labels/west2019playoff.csv', index_col=None)
west2019playoff['SEASON'] = 2019

eastTrainingPlayoffs = pd.concat([east2000playoff, east2001playoff, east2002playoff, east2003playoff, east2005playoff, east2006playoff, east2007playoff, east2008playoff, east2009playoff, east2010playoff, east2011playoff, east2012playoff, east2013playoff, east2014playoff, east2015playoff, east2016playoff, east2017playoff, east2018playoff, east2019playoff], ignore_index=True)
westTrainingPlayoffs = pd.concat([west2000playoff, west2001playoff, west2002playoff, west2003playoff, west2005playoff, west2006playoff, west2007playoff, west2008playoff, west2009playoff, west2010playoff, west2011playoff, west2012playoff, west2013playoff, west2014playoff, west2015playoff, west2016playoff, west2017playoff, west2018playoff, west2019playoff], ignore_index=True)

eastTrainingPlayoffs = eastTrainingPlayoffs.sort_values(by=['SEASON', 'TEAM'])
westTrainingPlayoffs = westTrainingPlayoffs.sort_values(by=['SEASON', 'TEAM'])

eastTrainingPlayoffs.to_csv('./eastTrainingPlayoffs.csv')
westTrainingPlayoffs.to_csv('./westTrainingPlayoffs.csv')

#Load all csv's for validation
east2020 = pd.read_csv('./season_stats/east2020.csv', index_col=None)
east2020['SEASON'] = 2020
east2021 = pd.read_csv('./season_stats/east2021.csv', index_col=None)
east2021['SEASON'] = 2021
east2022 = pd.read_csv('./season_stats/east2022.csv', index_col=None)
east2022['SEASON'] = 2022
west2020 = pd.read_csv('./season_stats/west2020.csv', index_col=None)
west2020['SEASON'] = 2020
west2021 = pd.read_csv('./season_stats/west2021.csv', index_col=None)
west2021['SEASON'] = 2021
west2022 = pd.read_csv('./season_stats/west2022.csv', index_col=None)
west2022['SEASON'] = 2022

eastValidationData = pd.concat([east2020, east2021, east2022])
westValidationData = pd.concat([west2020, west2021, west2022])

eastValidationData = eastValidationData.sort_values(by=['SEASON', 'TEAM'])
westValidationData = westValidationData.sort_values(by=['SEASON', 'TEAM'])

eastValidationData.to_csv('./eastValidationData.csv')
westValidationData.to_csv('./westValidationData.csv')

#Load playoff data for validation
east2020playoff = pd.read_csv('./playoff_labels/east2020playoff.csv', index_col=None)
east2020playoff['SEASON'] = 2020
east2021playoff = pd.read_csv('./playoff_labels/east2021playoff.csv', index_col=None)
east2021playoff['SEASON'] = 2021
east2022playoff = pd.read_csv('./playoff_labels/east2022playoff.csv', index_col=None)
east2022playoff['SEASON'] = 2022
west2020playoff = pd.read_csv('./playoff_labels/west2020playoff.csv', index_col=None)
west2020playoff['SEASON'] = 2020
west2021playoff = pd.read_csv('./playoff_labels/west2021playoff.csv', index_col=None)
west2021playoff['SEASON'] = 2021
west2022playoff = pd.read_csv('./playoff_labels/west2022playoff.csv', index_col=None)
west2022playoff['SEASON'] = 2022

eastValidationPlayoffs = pd.concat([east2020, east2021, east2022], ignore_index=True)
westValidationPlayoffs = pd.concat([west2020, west2021, west2022], ignore_index=True)

eastValidationPlayoffs = eastValidationPlayoffs.sort_values(by=['SEASON', 'TEAM'])
westValidationPlayoffs = westValidationPlayoffs.sort_values(by=['SEASON', 'TEAM'])

eastValidationPlayoffs.to_csv('./eastValidationPlayoffs.csv')
westValidationPlayoffs.to_csv('./westValidationPlayoffs.csv')
