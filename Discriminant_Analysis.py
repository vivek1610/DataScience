import pandas as pd
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# data = pd.read_excel("E:/vivek/Study Material Data Science/DataSet/Discriminant Analysis.xlsx")
# print(data)

dataset = pd.read_excel("E:/vivek/Study Material Data Science/41 - Discriminant Analysis/Discriminant Analysis.xlsx")
print(dataset.head())
y=dataset.ResortVisit
print(y)
x=dataset[['AnnualFamilyIncome','AttitudeTowardTravel','ImportanceAttachedtoFamilyVacatioin','HouseholdSize','AgeofHeadofHousehold']]
print(x)
clf=LinearDiscriminantAnalysis()
print(clf.fit(x,y))
print(clf.predict(x))
print(clf.score(x,y))

y=dataset.AmountSpentonFamilyVacation
print(clf.fit(x,y))
print(clf.predict(x))
print(clf.score(x,y))
