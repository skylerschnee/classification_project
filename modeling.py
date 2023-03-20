#!/usr/bin/env python
# coding: utf-8

# In[24]:


##### Imports

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np

#### prep data

def model_prep(train,validate,test):
    '''
    Prepare train, validate, and test data for modeling
    '''

    # drop unused columns 
    keep_cols = ['churn','monthly_charges','senior_citizen','tech_support']

    train = train[keep_cols]
    validate = validate[keep_cols]
    test = test[keep_cols]
    
    # Split data into predicting variables (X) and target variable (y) and reset the index for each dataframe
    train_X = train.drop(columns='churn').reset_index(drop=True)
    train_y = train[['churn']].reset_index(drop=True)

    validate_X = validate.drop(columns='churn').reset_index(drop=True)
    validate_y = validate[['churn']].reset_index(drop=True)

    test_X = test.drop(columns='churn').reset_index(drop=True)
    test_y = test[['churn']].reset_index(drop=True)
    
    # manual encoding
    train_X['senior_citizen'] = train_X.senior_citizen.apply(lambda value: 1 if value == 'Yes' else 0)
    train_X['tech_support'] = train_X.tech_support.apply(lambda value: 1 if value == 'Yes' else 0)
    
    validate_X['senior_citizen'] = train_X.senior_citizen.apply(lambda value: 1 if value == 'Yes' else 0)
    validate_X['tech_support'] = train_X.tech_support.apply(lambda value: 1 if value == 'Yes' else 0)
    
    test_X['senior_citizen'] = train_X.senior_citizen.apply(lambda value: 1 if value == 'Yes' else 0)
    test_X['tech_support'] = train_X.tech_support.apply(lambda value: 1 if value == 'Yes' else 0)

    # Change target column to show values as upset or non-upset
    train_y['churn'] = train_y.churn.apply(lambda value: "churn" if value == 'Yes' else "no-churn")
    validate_y['churn'] = validate_y.churn.apply(lambda value: "churn" if value == 'Yes' else "no-churn")
    test_y['churn'] = test_y.churn.apply(lambda value: "churn" if value == 'Yes' else "no-churn")

    return train_X, train_y, validate_X, validate_y, test_X, test_y

#### model evaluation

def dec_tree_acc(train_X, validate_X, train_y, validate_y):
    '''
    return accuracy of decision tree model on train and validate
    '''

    # create classifier object
    clf = DecisionTreeClassifier(max_depth=7, random_state=828)

    #fit model on training data
    clf = clf.fit(train_X, train_y)

    # print result
    print(f'Decision Tree accuracy on train data: {clf.score(train_X, train_y)}')
    print(f'Decision Tree accuracy on validate data: {clf.score(validate_X, validate_y)}')

def ran_forest_acc(train_X, validate_X, train_y, validate_y):
    '''
    return accuracy of random forest model on train and validate
    '''

    # create model object and fit it to training data
    rf = RandomForestClassifier(max_depth=5, random_state=903)
    rf.fit(train_X,train_y)

    # print result
    print(f'Random Forest accuracy on train data: {rf.score(train_X, train_y)}')
    print(f'Random Forest accuracy on validate data: {rf.score(validate_X, validate_y)}')

def log_reg_acc(train_X, validate_X, train_y, validate_y):
    '''
    return accuracy of logistic model on train and validate
    '''

    # create model object and fit it to the training data
    logit = LogisticRegression(penalty = 'l2', solver='lbfgs')
    logit.fit(train_X, train_y)

    # print result
    print(f'Logistic Regression accuracy on train data: {logit.score(train_X, train_y)}')
    print(f'Logistic Regression accuracy on validate data: {logit.score(validate_X, validate_y)}')

def knn_acc(train_X, validate_X, train_y, validate_y):
    '''
    return accuracy of knn model on train and validate
    '''

    # create model object and fit it to the training data
    knn = KNeighborsClassifier(n_neighbors=3, weights='distance')
    knn.fit(train_X, train_y)

    # print results
    print(f'KNN accuracy on train: {knn.score(train_X, train_y)}')
    print(f'KNN accuracy on on validate: {knn.score(validate_X, validate_y)}')
    
##### Test Set
    
def ran_forest_test(train_X, test_X, train_y, test_y):
    '''
    return accuracy of random forest model on test set
    '''

    # create model object and fit it to training data
    rf = RandomForestClassifier(max_depth=5, random_state=903)
    rf.fit(train_X,train_y)

    # print result
    print(f'Random Forest accuracy on test data: {rf.score(test_X, test_y)}')


# In[ ]:




