import numpy as np
import pandas as pd
from sklearn import preprocessing

df = pd.read_csv('data/master.csv')

#  Drop Team and Age columns
df = df.drop(columns=['TEAM', 'AGE'])

#  Change height to inches
height = df.loc[:,'HEIGHT']
height = pd.DataFrame(height.str.split('-'))
ht_inch = [int(row[0][0])*12 + int(row[0][1]) for idx, row in height.iterrows()]
df['HEIGHT'] = ht_inch

#  Cast all columns as ints or floats
df.dtypes
shooting_vars = ['FGA (LESS THAN 8FT)', 'FGA (8-16 FT)', 'FGA (16-24 FT)', 'FGA (24+ FT)']
df[shooting_vars] = df[shooting_vars].apply(pd.to_numeric, errors='coerce')
playtype_vars = ['ISO %', 'ROLL-HANDLE %', 'ROLL-MAN %', 'POST-UP %']
for p in playtype_vars:
    df[p] = pd.to_numeric(df[p].str.rstrip('%'))
df[playtype_vars] = df[playtype_vars]/100

#  The shooting variables will be percentages interpreted as the proportion of
#    shots from that region. To do this we simply divide by FGA.
df[shooting_vars] = df[shooting_vars].div(df['FGA'], axis=0)

#  Because not all players play the same amount of minutes we'll divide the 
#    below features by total minutes ('MIN') to get a per minute value.
per_min_vars = ['FGA', 'OFF BOX OUTS', 'DEF BOX OUTS', 'DIST MILES OFF', 
                    'DIST MILES DEF', 'DFGA', 'TOUCHES', 'FRONT CT TOUCHES',
                    'TIME OF POSS', 'ELBOW TOUCHES', 'POST UPS', 'PAINT TOUCHES']
df[per_min_vars] = df[per_min_vars].div(df['MIN'], axis=0)

#  The last step is to normalize the below columns between 0 and 1. Because of
#    the features that are proportions already exist between 0 and 1, it will
#    be helpful to be consistent with the range of all features.
norm_vars = ['HEIGHT', 'WEIGHT', 'AVG SEC/TOUCH', 'AVG DRIB/TOUCH']
norm_vars.extend(per_min_vars)
norm_df = df[norm_vars]
df[norm_vars] = (norm_df - norm_df.min())/(norm_df.max()-norm_df.min())

#  We're all good. This is the dataframe we want for this clustering exercise.
# df.head
df.to_csv('C:/projects/cs6140/nba_clustering/data/clustering_df1.csv')