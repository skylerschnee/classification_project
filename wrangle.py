#!/usr/bin/env python
# coding: utf-8

# In[22]:


#################################### imports #####################################

import os
import pandas as pd
import numpy as np
import env
from sklearn.model_selection import train_test_split

############################# acquire main function ##############################

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def wrangle_telco_data():
    '''
    wrangle_telco_data will acuire the telco_churn data and 
    proceed to drop redundant columns and non-usefull info in 
    addition to encoding categorical variables
    '''
    filename = "telco_churn_prepared.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql('SELECT * FROM customers', get_connection('telco_churn'))

        # drop redundancies and columns not needed for this exploration
        df = df.drop(columns=['online_security','online_backup',                              'device_protection','streaming_tv',                              'streaming_movies','paperless_billing',                              'customer_id'])

        # modify total_charges column by removing spaces and convert to float
        df['total_charges'] = df['total_charges'].str.replace(' ', '')
        df['total_charges'] = pd.to_numeric(df['total_charges'])

        # only 11 missing values from 1 column. I will drop these rows
        df = df.dropna()
        
        # saving to csv
        df.to_csv('telco_churn_prepared.csv', index = False)

        return pd.read_csv(filename)

################################ Split Data #####################################                         
                         
def split_my_data(df):
    '''
    split_my_data will take in a dataframe and split into 3 subsets, 
    train, validate, and test. 
    '''
    train_val, test = train_test_split(
        df,
        train_size = 0.8,
        random_state = 828,
        stratify = df['churn']
    )

    train, validate = train_test_split(
        train_val,
        train_size = 0.7,
        random_state = 828,
        stratify = train_val['churn']
    )

    # reset index for train validate and test
    train.reset_index(drop=True, inplace=True)
    validate.reset_index(drop=True, inplace=True)
    test.reset_index(drop=True, inplace=True)

    return train, validate, test


# In[ ]:




