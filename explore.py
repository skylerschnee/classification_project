#!/usr/bin/env python
# coding: utf-8

# In[353]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats

################# Visuals #####################

def get_pie_churn(train):
    '''
    returns a pie chart visualizing the proportions of customer churn
    '''
    
    # set parameters
    x = [len(train.churn[train.churn == 'Yes']), len(train.churn[train.churn == 'No'])] 
    y = ['Churn','Retained'] 
    explodechurn = (0.1, 0)  # only explode the churn slice 
    
    # generate and show chart
    plt.pie(x, labels=y, explode =explodechurn, autopct='%.0f%%', colors=['red', 'green'])
    plt.title('27% of Telco Customers Have Churned')
    plt.show()
    
def get_pie_sen_churn(train):
    '''
    returns a pie charts visualizing the percentage of churned senior citizens
    compared to the rest of the population
    '''
    
    # identify counts of churned customers, senior and non senior
    non_senior_churn_count = len(train[(train['churn'] == 'Yes') & (train['senior_citizen'] == 0)])
    senior_churn_count = len(train[(train['churn'] == 'Yes') & (train['senior_citizen'] == 1)])

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Non-Senior Churn', 'Senior Churn'
    sizes = [non_senior_churn_count, senior_churn_count]
    explode = (0, 0.1)  # only explode the senior slice 

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90, colors=['lightblue', 'yellow'])
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Seniors are Over 25% of the Churned Customer Population')
    plt.show()
    
def get_pie_sen_compared(train):
    '''
    returns pie charts visualizing the percentage of senior citizens compared
    to the rest of the population, and the percentage of churned senior citizens
    compared to the rest of the population
    '''
    #identify the two groups
    non_senior_cust_count = len(train[(train['senior_citizen'] == 0)])
    senior_cust_count = len(train[(train['senior_citizen'] == 1)])
    
    non_senior_churn_count = len(train[(train['churn'] == 'Yes') & (train['senior_citizen'] == 0)])
    senior_churn_count = len(train[(train['churn'] == 'Yes') & (train['senior_citizen'] == 1)])
    
    # create objects and size the figure
    fig, (ax1,ax2) = plt.subplots(1,2,figsize=(11,11))

    # generate pie chart and assign it to ax1
    labels1 = 'Non-Senior Customers', 'Senior Customers'
    sizes1 = [non_senior_cust_count, senior_cust_count]
    explode1 = (0, 0.1)  # only explode the senior slice 

    ax1.pie(sizes1, explode=explode1, labels=labels1, autopct='%1.1f%%',
        shadow=True, startangle=90, colors=['lightblue', 'yellow'])
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.title.set_text('Seniors are Roughly 16% of the Customer Population')

    # generate pie chart and assign it to ax2
    labels2 = 'Non-Senior Churn', 'Senior Churn'
    sizes2 = [non_senior_churn_count, senior_churn_count]
    explode2 = (0, 0.1)  # only explode the senior slice  

    ax2.pie(sizes2, explode=explode2, labels=labels2, autopct='%1.1f%%',
        shadow=True, startangle=90, colors=['lightblue', 'yellow'])
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax2.title.set_text('Seniors are Over 25% of the Churned Customer Population')


    # display and format plot for a clean fit
    plt.tight_layout(pad=2, rect=(0, 0, 1, .6))
    plt.show()

def get_chi_senior(train):   
    '''
    return results of chi2 test of churn & senior_citizen
    '''
    # crosstab of columns to compare
    observed = pd.crosstab(train.senior_citizen, train.churn)

    # perform chi2 test
    chi2, p, degf, expected = stats.chi2_contingency(observed)

    print(f'chi2 = {chi2:.4f}')
    print(f'p     = {p:.8f}')    
        
def get_bar_charges(train):
    '''
    return a bar chart visualizing the discrepancy in monthly
    charges between seniors and non seniors
    '''
    
    # quantify avg monthly charges for seniors an non-seniors
    sen_avg_charges = train.monthly_charges[(train['senior_citizen'] == 1)].mean()
    non_sen_avg_charges = train.monthly_charges[(train['senior_citizen'] == 0)].mean()
    
    # establish variables
    courses = ['Senior Avg Monthly Charges','Non - Senior Avg Monthly Charges']
    values = [sen_avg_charges, non_sen_avg_charges]

    fig = plt.figure(figsize = (5, 6))

    # creating the bar plot
    plt.bar(courses, values, color ='orange',
            width = .5, edgecolor = 'black')

    # label and show
    plt.ylabel("Mean of Monthly Charges ($)")
    plt.title("Senior Citizens Pay 29% More Than Non-Seniors Monthly")
    plt.show()
    
def sen_churn_tstat(train): 
    '''
    sen_churn_tstat wil return the tstat and p-value of and independent t-test
    comapring the monthlt charges of churned seniors with non-churned seniors
    '''
    #identify the two groups
    senior_churn_sample = train[(train['churn'] == 'Yes') & (train['senior_citizen'] == 1)].monthly_charges
    senior_nonchurn_sample = train[(train['churn'] == 'No') & (train['senior_citizen'] == 1)].monthly_charges
    
    #perform ttest, equal variances confirmed False
    t, p = stats.ttest_ind(senior_churn_sample, senior_nonchurn_sample, equal_var=False)
    
    # print the tstat and pvalue
    print(f't-stat = {t:.4f}')
    print(f'p     = {p:.4f}')
    
def get_bar_support(train):
    '''
    return a bar chart visualizing the churn of senior customers
    who have tech support vs seniors who do not
    '''
    
    # quantify churned seniors based on tech support 
    has_support = len(train[(train['churn'] == 'Yes') & (
        train['senior_citizen'] == 1) & (train['tech_support'] == 'Yes')])
    
    no_support = len(train[(train['churn'] == 'Yes') & (
        train['senior_citizen'] == 1) & (train['tech_support'] == 'No')])
    
    no_support_no_internet = len(train[(train['churn'] == 'Yes') & (train['senior_citizen'] == 1) & (
        train['tech_support'] == 'No internet service')])
    
    # set parameters
    courses = ['Churned Seniors With Support',
               'Churned Seniors Without Support', 
               'Churned Seniors Without Support (no internet)']
    values = [has_support, no_support, no_support_no_internet]

    fig = plt.figure(figsize = (12, 6))

    # creating the bar plot
    plt.bar(courses, values, color ='silver',
            width = .5, edgecolor = 'black')

    # show plot
    plt.ylabel("Count of Churned Seniors")
    plt.title("Say Goodbye to Seniors Without Tech Support!")
    plt.show()

def get_chi_techsupp_sen(train):
    '''
    get rusults of chi-square for churn and tech support among senior citizens 
    '''
    
    # isolate the senior citizens
    subset = train.loc[train['senior_citizen'] == 1]
    
    # crosstab of columns to compare
    observed = pd.crosstab(subset.tech_support, subset.churn)
    
    # perform chi2 test
    chi2, p, degf, expected = stats.chi2_contingency(observed)

    #print results
    print(f'chi^2 = {chi2:.4f}')
    print(f'p     = {p:.8f}')


# In[ ]:




