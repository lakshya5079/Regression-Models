#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing dataset
data=pd.read_csv('train_v9rqX0R.csv')

#treating the missing dataset
################################################################################################################
from sklearn.preprocessing import LabelEncoder
""" This function is universal to onehot encode the whole data-set"""

#Auto encodes any dataframe column of type category or object.
def dummyEncode(df):
        columnsToEncode = list(df.select_dtypes(include=['category','object']))
        le = LabelEncoder()
        for feature in columnsToEncode:
            try:
                df[feature] = le.fit_transform(df[feature])
            except:
                print('Error encoding '+feature)
        return df

dummyEncode(dataset)
##################################################################################################################
