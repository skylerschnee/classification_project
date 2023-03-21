# Telco Churn

# Project Description
 
Customer retention is arguably the most important aspect of a long lasting, profitable business. Considering the massive proportion of gross profit business' spend on new customer aquisition, we can easily understand the value of retaining these customers. This begs the literal million dollar question- why have our customers left? And what actionable information can we draw from a scientific approach to analyzing our customer data? We will be exploring that in this project and attempt to build a machine learning model that accurately predicts churn.

# Project Goal
 
* Discover drivers of customer church at Telco.
* Use drivers to develop a machine learning model that accurately predicts churn. 
* This information could be used to further our understanding of which drivers have the most effect on churn.

# Initial Thoughts
 
My initial hypothesis is that monthly chargesm senior citizen status, and access to tech support are the driving factors of churn.

# The Plan
 
* Aquire data from Code Up Database
 
* Prepare data
   * Create Engineered columns from existing data
       * churn
       * senior_citizen
       * tech_support
       * monthly_charges
      
* Explore data in search of drivers of churn
   * Answer the following initial questions
       * How often do senior citizens churn?
       * Does tech support influence churn?
       * Does the way customers pay influence churn?
       * Does the monthly charges impact on churn?

* Develop a Model to predict if a customer is likely to churn
   * Use drivers identified in explore to build predictive models of different types
   * Evaluate models on train and validate data
   * Select the best model based on highest accuracy
   * Evaluate the best model on test data
 
* Draw conclusions

# Data Dictionary

| Feature | Definition |
|:--------|:-----------|
|Gender| The gender of the primary account holder|
|Senior Citizen| True or False, is the primary account holder 62 years or age or older|
|Partner| Yes or No, does the primary account holder have a partner in the household|
|Dependants| Yes or No, does the primary account holder have at least 1 dependent in the household|
|Tenure| The time in years the primary account holder has been a customer|
|Phone Service| Yes or No, does the primary account holder have phone service with Telco|
|Multiple Lines| Yes or No, does the primary account holder have multiple lines with Telco|
|Internet Service Type ID|  **1** (DSL), **2** (Fiber Optic), **3** (None)
|Tech Support| Yes or No, Has the client contacted tech support|
|Contract Type ID|  **1** (Month-to-Month), **2** (One-Year), **3** (Two-Year)|
|Payment Type ID| **1** (Electronic Check), **2** (Mailed Check), **3** (Automatic Bank Transfer), **4** (Credit Card)|
|Monthly Charges| Monthly bill assesed to the cusotmer|
|Total Charges| Total revenue paid by the cusotmer|
|Churn| Yes or No, has the customer stopped doing business with us|

# Steps to Reproduce
1) Clone this repo.
2) Acquire the data from [Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
3) Put the data in the file containing the cloned repo.
4) Run notebook.

# Takeaways and Conclusions
- Approximately 27% of customers churn

- Customers that pay more than the mean monthly charges are more likely to churn tthan those paying less than the mean

- Senior Citizens are more likey to churn than customer who are not seniors

- Customers with tech support are much less likely to churn than those without

- Our KNN model performed well on train data, but appeared overfit once validated

- Our best performing model was random forest, but did not beat the baseline. Likely reason:

    - We know the features we chose are valuble, but we only used 3 to attempt to predict churn. 
    
- while our machine learning models did not prove to be very usefull as predictors of churn compared to the baseline accuracy, we certainly drew some actionable information from our exploration. I would urge stakeholders to approve further investigation into the probable causes senior citizen churn, as they are clearly over represented in the churned customer population

- Secondly, I would recommend further analysis regarding tech support. Depending on the company's cost to provide customers with tech support, there may be significant value in providing the customers with this service at a much lower or even no cost, as it direclty influences customer retention. 

# Recommendations
- Regarding monthly charges, use multiple bins of charges instead of just above or below the mean of monthly charges.
- Continue exploration to identify more features that influence churn
- Include these features into our models 
