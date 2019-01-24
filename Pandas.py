import pandas as pd
import numpy as np
from numpy import nan as NA

###### read CSV File
csvObj = pd.read_csv("E:/vivek/Study Material Data Science/DataSet/TestData.csv")

### For null values count in data for each column

print(csvObj.isnull().sum())

###### Read top 5 lines of file
print(csvObj.head())

###### print no of rows and columns
print(csvObj.shape)

###### Find the class of a file
print(type(csvObj))

###### Data type of all the column
print(csvObj.dtypes)

###### Info of every column
print(csvObj.info())

###### Describe all the column
print(csvObj.describe())

###### Select first 10 rows of a column
print(csvObj['Order ID'][0:10])

###### Find the Mean of column
print(csvObj['Order ID'].mean())

###### Find the Median
print(csvObj['Order ID'].median())

###### Select any column and required rows
print(csvObj[['Region','Item Type','Order ID']][0:50])

###### filter no of rows on condition basis
print(csvObj[csvObj['Units Sold']>8000])

###### Filter no of rows on Condition Basis and required specific column
print(csvObj[csvObj['Units Sold']>8000][['Region','Item Type','Order ID']])

###### Calculation Nul rows and column
###### filter no of rows on condition basis
print(csvObj[csvObj['Units Sold'].isnull()])

###### My Seriese###############################################################
my_series = csvObj['Order ID'][0:10]
print(my_series)
###### Count unique value in rows and count
print(my_series.value_counts())
####### find total no of rows
print(my_series.count())
#################################################################################
###### Create a Data Frame#######################################################

###Syntax  = pandas.DataFrame( data, index, columns, dtype, copy)
data = pd.DataFrame(np.arange(16).reshape(4,4), index=['Ohio', 'Colorado', 'Utah', 'New York'], columns=['one', 'two', 'three', 'four'])
print(data)

###### Drop Rows
print(data.drop(['Ohio','Utah']))

###### Drop Column
print(data.drop(['two'],axis=1))

#################################################################################
### Handlin Missing Data
string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])
print(string_data)

######### Checkimg Null Values
print(string_data.isnull())

######### Filterig Missing Data
datastr = pd.Series([1, NA, 3.5, NA, 7])
#### Drop All NA Values in a seriese
print(datastr.dropna())

####### Drop NA from Data Frame
datafrm = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA],[NA, NA, NA], [NA, 6.5, 3.]])
print(datafrm)
####### Drop All NA values
print(datafrm.dropna())

####### drop only those rows which have all NA value
print(datafrm.dropna(how='all'))

##### Dropping columns in the same way is only a matter of passing axis=1:
datafrm[4] = NA
print(datafrm)
print(datafrm.dropna(how='all',axis=1))

######## Combining and merging Data Set
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
print(df1)
df2 = pd.DataFrame({'key': ['a', 'b', 'd'],'data2': range(3)})
print(df2)

####### Merge two data frame or inner join
print(pd.merge(df1, df2))

###### Merge two data frame by outer join
print(pd.merge(df1, df2, how='outer'))

###### Merge two data frame by left join
print(pd.merge(df1,df2,how='left',on='key'))

###### Merge two data frame by right join
print(pd.merge(df1,df2,how='right'))

######### Concatenate numpy Arrays

npr = np.arange(12).reshape(3,4)
print(npr)
#### concatenate array by column wise
print(np.concatenate([npr,npr],axis=1))

#### concatenate array by row wise
print(np.concatenate([npr,npr],axis=0))

####### Concate Data Frames
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'], 'B': ['B0', 'B1', 'B2', 'B3'], 'C': ['C0', 'C1', 'C2', 'C3'], 'D': ['D0', 'D1', 'D2', 'D3']}, index=[0, 1, 2, 3])
print(df1)
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],'B': ['B4', 'B5', 'B6', 'B7'],'C': ['C4', 'C5', 'C6', 'C7'],'D': ['D4', 'D5', 'D6', 'D7']},index=[4, 5, 6, 7])
print(df2)
print(pd.concat([df1,df2]))

########## Removing Duplicates
data = pd.DataFrame({'k1': ['one'] * 3 + ['two'] * 4,'k2': [1, 1, 2, 3, 3, 4, 4]})
print(data)
print(data.duplicated())
print(data.drop_duplicates())

##### Drop Duplicates on the basis of column wise
print(data.drop_duplicates(['k1']))

Data = [['Steve',22,'M','Newyork'],['Vivek',30,'M','Noida'],['Vartika',28,'F','Noida'],['James',34,'M','LONDON']]
info = pd.DataFrame(Data,columns=['Name','Age','Gender','City'],dtype=int)
print(info)

#################################################################
### Index order is persisted with Nan when key missing in given dictionary

dict ={'a':0,'b':2,'c':7}
print(pd.Series(dict,index=['a','b','c','d']))
#################################################################
########Create a Seriese from Scalar ############################
### data is a scalar value, an index must be provided. The value will be repeated to match the length of index
print(pd.Series(4,index=[0,1,2,3,4]))
#################################################################
#### Create a DataFrame by using Nd arrays
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42],'City':['US','UK','Japan','IND']}
print(pd.DataFrame(data))
##################################################################
##Create a DataFrame from List of Dicts
data  = [{'a':1,'b':3,'c':4},{'a':2,'b':3}]
print(pd.DataFrame(data))
print(pd.DataFrame(data,index=['r1','r2']))
########## Dimension #############################################
print(pd.DataFrame(data).ndim)
print(pd.DataFrame(data).axes)
print(pd.DataFrame(data).size)
print(pd.DataFrame(data).shape)
##################################################################
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
###Returns the sum of the values for the requested axis
### sum():
print(pd.DataFrame(d).sum())
### axis = 1
print(pd.DataFrame(d).sum(1))

### mean(): Returns the average value
print(pd.DataFrame(d).mean())

### std() : Returns the Bressel standard deviation of the numerical columns.
print(pd.DataFrame(d).std())
### count() : returns number of rows in data frame for each column
print(pd.DataFrame(d).count())
### median(): median of all val
print(pd.DataFrame(d).median())
### min(): min val
print(pd.DataFrame(d).min())
### max(): max val
print(pd.DataFrame(d).max())
### describe(): describe the data frame
###1 - summarise all column
print(pd.DataFrame(d).describe(include='all'))
### 2- Sumaarise Number column
print(pd.DataFrame(d).describe(include='number'))
### 3 - summarise string column
print(pd.DataFrame(d).describe(include=['object']))
### adder function
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
########################################################
############ Pandas Reindexing #########################
N=20
df = pd.DataFrame({
   'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
   'x': np.linspace(0,stop=N-1,num=N),
   'y': np.random.rand(N),
   'C': np.random.choice(['Low','Medium','High'],N).tolist(),
   'D': np.random.normal(100, 10, size=(N)).tolist()
})
print(df)
#reindex the DataFrame menas required filtered data from data frame
df_reindexed = df.reindex(index=[0,2,5], columns=['A', 'C', 'B'])
print(df_reindexed)
###################################################################
############ Iterate in Pandas ####################################
N = 20
#converting all the ndarray value in to list
print(len(np.random.normal(100, 10, size=(N)).tolist()))
df = pd.DataFrame({
    'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
    'x': np.linspace(0,stop=N-1,num=N),
    'y': np.random.rand(N),
    'C': np.random.choice(['Low','Medium','High'],N).tolist(),
    'D': np.random.normal(100, 10, size=(N)).tolist()
    })

for col in df.keys():
   print(col," is key -----------",df[col])
#### Select Multiple column from data Frame
print(df['A'])
print(df.loc[:,['A','D']])
####iteritems() − to iterate over the (key,value) pairs
####iterrows() − iterate over the rows as (index,series) pairs
####itertuples() − iterate over the rows as namedtuples
df = pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])
for key,value in df.iteritems():
   print(key,value)

######################################################################
#################### Sorting##########################################
unsorted_df=pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns=['col2','col1'])
print(unsorted_df)
######### sorting by Index#############################################
print(unsorted_df.sort_index())
######### Order of sorting#############################################
print(unsorted_df.sort_index(ascending=False))
######### Sort the columns ############################################
print(unsorted_df.sort_index(axis=1))
#########  Sort by Value #############################################
print(unsorted_df.sort_values(by='col1'))
######### Sorted by both the columns value ###########################
print(unsorted_df.sort_values(by=['col1','col2']))

######################################################################
#############Function for texr data process###########################

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])
print(s)
# lower()	Converts strings in the Series/Index to lower case.
# upper()	Converts strings in the Series/Index to upper case.
# len()	Computes String length().
# strip()	Helps strip whitespace(including newline) from each string in the Series/index from both the sides.
# split(' ')	Splits each string with the given pattern.
# cat(sep=' ')	Concatenates the series/index elements with given separator.
# get_dummies()	Returns the DataFrame with One-Hot Encoded values.
# contains(pattern)	Returns a Boolean value True for each element if the substring contains in the element, else False.
# replace(a,b)	Replaces the value a with the value b.
# repeat(value)	Repeats each element with specified number of times.
# count(pattern)	Returns count of appearance of pattern in each element.
# startswith(pattern)	Returns true if the element in the Series/Index starts with the pattern.
# endswith(pattern)	Returns true if the element in the Series/Index ends with the pattern.
# find(pattern)	Returns the first position of the first occurrence of the pattern.
# findall(pattern)	Returns a list of all occurrence of the pattern.
# swapcase	Swaps the case lower/upper.
# islower()	Checks whether all characters in each string in the Series/Index in lower case or not. Returns Boolean
# isupper()	Checks whether all characters in each string in the Series/Index in upper case or not. Returns Boolean.
# isnumeric()	Checks whether all characters in each string in the Series/Index are numeric. Returns Boolean.
print(s.str.lower())

########################################################################
########### Pandas indexing and selecting ##############################
########### Multiple coloumn ###########################################
print(df.loc[:,['col1','col2']])
print(df.loc[:,'col1'])
df = pd.DataFrame(np.random.randn(8, 4),index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

# Select few rows for multiple columns, say list[]
print(df.loc[['a','b','f','h'],['A','C']])

# Select range of rows for all columns
print(df.loc['a':'h'])

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

# select all rows for a specific column
print(df.iloc[:4])

# Integer slicing
print(df.iloc[1:5, 2:4])

# Slicing through list of values
print(df.iloc[[1, 3, 5], [1, 3]])
print(df.iloc[1:3, :])
print(df.iloc[:,1:3])
print(df[['A','B']])

##############################################################################
############### Pandas Missing Data ##########################################
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f','h'],columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df)
##### Check for Missing Values
print(df['one'].isnull())
print(df['one'].notnull())
#Calculations with Missing Data
#When summing data, NA will be treated as Zero
print(df['one'].sum())
#If the data are all NA, then the result will be NA
df = pd.DataFrame(index=[0,1,2,3,4,5],columns=['one','two'])
print(df['one'].sum())
#########################################################################
#Cleaning / Filling Missing Data
#### Replace NAN with scalar value
df = pd.DataFrame(np.random.randn(3, 3), index=['a', 'c', 'e'],columns=['one','two', 'three'])
df = df.reindex(['a', 'b', 'c'])
print(df)
print ("NaN replaced with '0':")
print(df.fillna(0))
##########################################################################
###Fill NA Forward and Backward
#pad/fill	Fill methods Forward
#bfill/backfill	Fill methods Backward
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print(df.fillna(method='pad'))
print(df.fillna(method='bfill'))
###########################################################################
##Drop Missing Values
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
## by row wise
print(df.dropna())
## By column wise
print(df.dropna(axis=1))
###########################################################################
####Replace Missing (or) Generic Values
df = pd.DataFrame({'one':[10,20,30,40,50,2000],'two':[1000,0,30,40,50,60]})
print(df.replace({1000:99,2000:89}))
###########################################################################
############### Pandas Group By############################################
ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)
### Split Data into Groups
#obj.groupby('key')
#obj.groupby(['key1','key2'])
#obj.groupby(key,axis=1)
### Group by single column
print(df.groupby('Team').groups)
### Group by multiple column
print(df.groupby(['Team','Year']).groups)
####Iterating through Groups
grouped = df.groupby('Year')
for name,group in grouped:
    print(name)
    print(group)

##Select a Group value
print(grouped.get_group(2014))

#### Aggregations on group by by agg method
print(grouped['Points'].agg(np.mean))
###size total no of rows in each group
print(grouped['Points'].agg(np.size))
## in all column it found total rows in each group
print(grouped.agg(np.size))
### Multiple aggregate function at once
print(grouped['Points'].agg([np.sum, np.mean, np.std]))
### Filtration filters the data on a defined criteria and returns the subset of data. The filter() function is used to filter the data.
print(df.groupby('Team').filter(lambda x: len(x) >= 3))
###################################################################################

######### Merge Two data Framse on a key ##########################################
##on − Columns (names) to join on. Must be found in both the left and right DataFrame objects.
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,6],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
print(pd.merge(left,right,on='id'))
############################################################
###Merge Two DataFrames on Multiple Keys
print(pd.merge(left,right,on=['id','subject_id']))
##### Merge Using 'how' Argument
##LEFT
print(pd.merge(left, right, on='subject_id', how='left'))
##Right
print(pd.merge(left, right, on='subject_id', how='right'))
## Outer : full outer join Uniom
print(pd.merge(left, right, on='subject_id', how='outer'))
## Outer : full inner join means intersection
print(pd.merge(left, right, on='subject_id', how='inner'))

#########################################################################################

###Python Pandas - Concatenation

one = pd.DataFrame({
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5'],
         'Marks_scored':[98,90,87,69,78]},index=[1,2,3,4,5])
two = pd.DataFrame({
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5'],
         'Marks_scored':[89,80,79,97,88]},index=[1,2,3,4,5])
print(pd.concat([one,two]))

##Suppose we wanted to associate specific keys with each of the pieces of the chopped up DataFrame.
print(pd.concat([one,two],keys=['x','y']))

## for new own index
#If the resultant object has to follow its own indexing, set ignore_index to True.
print(pd.concat([one,two],keys=['x','y'],ignore_index=True))
#####Concatenating Using append
print(one.append(two))
##################################################################################
### time series###################################################################
print(pd.datetime.now())
########### Create a time stamp###################################################
print(pd.Timestamp('2017-03-01'))
#### Create a range of time
print(pd.date_range("11:00", "13:30", freq="30min").time)
############# Create a Range of Dates ############################################
## create the dates by date wise
print(pd.date_range('1/1/2011', periods=5))
## create the date by month wise
print(pd.date_range('1/1/2011', periods=5,freq='M'))
###################################################################################
###############  Categorical Data #################################################
#pd.Categorical Using the standard pandas Categorical constructor, we can create a category object.
cat = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c','v'])
print(cat)
cat = pd.Categorical(['a','b','c','a','b','c','d'], ['c', 'b', 'a'])
print(cat)
###################################################################################
## Pandas Input Out put file operation#############################################

##read.csv  :read.csv reads data from the csv files and creates a DataFrame object.
csv = pd.read_csv("E:/vivek/Study Material Data Science/DataSet/TestData.csv")
print(csv)

### Create custom index
#csv = pd.read_csv("E:/vivek/Study Material Data Science/DataSet/TestData.csv",index_col=['S.No'])
#print(csv)

print(csvObj.isnull().sum())