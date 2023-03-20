#!/usr/bin/env python
# coding: utf-8

# In[445]:


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
    plt.title('Seniors are Roughly 25% of the Churned Customer Population')
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
    ax2.title.set_text('Seniors are roughly 25% of the Churned Customer Population')


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
    return a bar chart visualizing the amount of churned customers paying 
    more or less than the population avg monthly charges as well as those 
    in the same categories who have not churned
    '''
    
    # defined groups
    avg_mon_charges = train.monthly_charges.mean()
    tot_more_than_avg = len(train[(train['monthly_charges'] > avg_mon_charges)])
    churned_pay_more = len(train[(train['churn'] == 'Yes') & (train['monthly_charges'] > avg_mon_charges)])
    tot_less_than_avg = len(train[(train['monthly_charges'] < avg_mon_charges)])
    churned_pay_less = len(train[(train['churn'] == 'Yes') & (train['monthly_charges'] < avg_mon_charges)])
    
    # establish variables
    groups = ['Pays More Than Average', 'Pays More Than Average(Churned)', 'Pays Less Than Average', 'Pays Less Than Average(Churned)']
    values = [tot_more_than_avg, churned_pay_more, tot_less_than_avg, churned_pay_less]
    colors_list = ['lightgreen', 'red', 'lightgreen', 'red']
    
    fig = plt.figure(figsize = (12, 6))

    # creating the bar plot
    plt.bar(groups, values, color =colors_list, width = .5, edgecolor = 'black')

    # label and show
    plt.ylabel("Number of Customers")
    plt.title("Monthly Charges")
    plt.show()
    
def charges_churn_tstat(train): 
    '''
    charges_churn_tstat wil return the tstat and p-value of and independent t-test
    comapring the monthly charges of churned customer with non-churned customers
    '''
    #identify the two groups
    churn_sample = train[(train['churn'] == 'Yes')].monthly_charges
    nonchurn_sample = train[(train['churn'] == 'No')].monthly_charges
    
    #perform ttest, equal variances confirmed False
    t, p = stats.ttest_ind(churn_sample, nonchurn_sample, equal_var=False)
    
    # print the tstat and pvalue
    print(f't-stat = {t:.4f}')
    print(f'p     = {p:.4f}')
    
def get_bar_support(train):
    '''
    return a bar chart visualizing the churn of customers
    who have tech support vs those who do not
    '''
    
    # identify groups 
    churned_has_support = len(train[(train['churn'] == 'Yes') & (train['tech_support'] == 'Yes')])
    not_churned_has_support = len(train[(train['churn'] == 'No') & (train['tech_support'] == 'Yes')])
    
    churned_no_support = len(train[(train['churn'] == 'Yes')  & (train['tech_support'] == 'No')])
    not_churned_no_support = len(train[(train['churn'] == 'No')  & (train['tech_support'] == 'No')])
    
    # set parameters
    groups = ['Churned With Support', 'Retained With Support',
                'Churned Without Support', 'Retained Without Support']
   
    values = [churned_has_support, not_churned_has_support,
              churned_no_support, not_churned_no_support]
    colors_list = ['red', 'lightgreen', 'red', 'lightgreen']

    fig = plt.figure(figsize = (12, 6))

    # creating the bar plot
    plt.bar(groups, values, color =colors_list, edgecolor = 'black')

    # show plot
    plt.ylabel("Count of Customers")
    plt.title("Say Goodbye to Customers Without Tech Support!")
    plt.show()

def get_chi_techsupp(train):
    '''
    get rusults of chi-square for churn and tech support 
    '''    
    # crosstab of columns to compare
    observed = pd.crosstab(train.tech_support, train.churn)
    
    # perform chi2 test
    chi2, p, degf, expected = stats.chi2_contingency(observed)

    #print results
    print(f'chi^2 = {chi2:.4f}')
    print(f'p     = {p:.8f}')


# In[ ]:





# In[ ]:




