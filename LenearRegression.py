import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn import linear_model as lm

#### By stats Model############################################

dataset = pd.read_excel("E:/vivek/Study Material Data Science/16 - Linear Regression/Correlation.xlsx",sheet_name=0)
#print(dataset)
#print(dataset.describe())
#print(dataset.info())
#print(dataset.shape)

### Single dependent variable ########################
#Y=dataset.Attitude
# X=dataset.Duration
# X=sm.add_constant(X)
# result=sm.OLS(Y,X)
# simple=result.fit()
#print(simple.summary())
######################################################
### multiple dependent variable ######################
dataset1 = pd.read_excel("E:/vivek/Study Material Data Science/16 - Linear Regression/Correlation.xlsx",sheet_name=1)

#print(dataset1)
Y=dataset.Attitude
X=dataset1[['Duration','Importance']]
X=sm.add_constant(X)
result=sm.OLS(Y,X)
multiple=result.fit()
print(multiple.predict(X))
print(multiple.summary())

#### By Sklearn #################
Y=dataset.Attitude
X=dataset1[['Duration','Importance']]
ln = lm.LinearRegression()
model = ln.fit(X,Y)
print(model.predict(X))
print(model.score(X,Y))
