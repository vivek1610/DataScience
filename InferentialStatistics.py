import pandas as pd
from scipy.stats import wilcoxon
from scipy.stats import friedmanchisquare
from scipy.stats import mannwhitneyu
from scipy.stats import kruskal
###### Wilcoxon ################

dataset = pd.read_excel("E:/vivek/Study Material Data Science/8 - Descriptive Statistics & Hypothesis/10 - Inferential Stats/Wilcoxon.xlsx",sheet_name=0)
print(dataset.head())
d1=dataset.TOTALCIN
d2=dataset.TOTALCW2
stat, p=wilcoxon(d1,d2)
print(stat,p)
### P(Significance level) vlaue is less than .05 then Null hypothesis is rejected
###29.5 0.00259741456482452
################ Friedmen Test ##################################################

d3 = dataset.TOTALCW4
stat,p = friedmanchisquare(d1,d2,d3)
print(stat,p)
### P(Significance level) vlaue is greater than .05 then Null hypothesis is accepted
###27.927710843373504 8.62133745016363e-07

############## Manwhiteney  test ####################################################
dataset1 = pd.read_excel("E:/vivek/Study Material Data Science/8 - Descriptive Statistics & Hypothesis/10 - Inferential Stats/Mann Whitney.xlsx",sheet_name=1)
print(dataset1.head())
a1=dataset1.Design1
a2=dataset1.Design2
stat, p=mannwhitneyu(a1,a2)
print(stat, p)
###9.0 0.2641796636354743

##################### Kruskal Walis ##################################################
dataset2 = pd.read_excel("E:/vivek/Study Material Data Science/8 - Descriptive Statistics & Hypothesis/10 - Inferential Stats/Kruskal Wallis.xlsx",sheet_name=0)
a3=dataset2.Design1
a4=dataset2.Design2
a5=dataset2.Design3
stat, p=kruskal(a3,a4,a5)
print(stat,p)
#####9.057039711191344 0.010796644845236254

############# one sample T test #############
from scipy.stats import ttest_1samp
dataset3 = pd.read_excel("E:/vivek/Study Material Data Science/8 - Descriptive Statistics & Hypothesis/10 - Inferential Stats/One Sample.xlsx",sheet_name=0)
print(dataset3.head())
y1 = dataset3.Height
stat, p=ttest_1samp(y1,65)
print(stat, p)

##### two sample paired test ################
from scipy.stats import ttest_rel
dataset4 = pd.read_excel("E:/vivek/Study Material Data Science/8 - Descriptive Statistics & Hypothesis/10 - Inferential Stats/Paired Sample.xlsx",sheet_name=0)
print(dataset4.head())
b1=dataset4.English
b2=dataset4.Math
stat,p=ttest_rel(b1,b2)
print(stat,p)

###### Two Samples Seprate T test ####################
from scipy.stats import ttest_ind
dataset5 = pd.read_excel("E:/vivek/Study Material Data Science/8 - Descriptive Statistics & Hypothesis/10 - Inferential Stats/Independent Sample.xlsx",sheet_name=3)
print(dataset5.head())
z1=dataset5.Nonathelete
z2=dataset5.Athelete
stat, p=ttest_ind(z1,z2)
print(stat, p)