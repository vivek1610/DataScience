import pandas as pd
import numpy as np
import statsmodels.api as sm

dataset = pd.read_excel("E:/vivek/Study Material Data Science/29 - Logistic Regression/Logistic Regression.xlsx",sheet_name=0)
print(dataset.head())
#print(dataset.shape)
#print(dataset.describe())
#print(dataset[['GRE','GPA']].std())
Y = dataset.Admit
X = dataset[['GRE','GPA','Rank']]
logit_model=sm.Logit(Y,X)
result=logit_model.fit()
print(result.summary())
print(result.predict(X))