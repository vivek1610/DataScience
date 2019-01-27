import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_excel("E:/vivek/Study Material Data Science/8 - Descriptive Statistics & Hypothesis/8 - Descriptive statistics/Descriptive Statistics.xlsx",sheet_name=0)
print(dataset)
print(dataset.head())
############### Mean ################
print(dataset['CurrentSalary'].mean())

############## Median ################
print(dataset['CurrentSalary'].median())

############# Mode ####################
print(dataset['CurrentSalary'].mode())

############# Standard Deviation ####################
print(dataset['CurrentSalary'].std())

############# Variance ####################
print(dataset['CurrentSalary'].var())

############ Describe #####################
print(dataset['CurrentSalary'].describe())

############ skew #####################
print(dataset['CurrentSalary'].skew())

############ Kurt #####################
print(dataset['CurrentSalary'].kurt())

############ Box Plot ##################
plt.boxplot(dataset['CurrentSalary'])
print(plt.show())
