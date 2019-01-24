import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import random

##### It will equaly divide the no from 0 to 5 in 10 times
#print(np.linspace(0,5,10))

#### boundry will create
#plt.figure()
########### line Graph
x = [1,2,3,]
y = [3,5,7]
x1 = [1,2,3]
y1 = [10,12,15]
plt.title('Line Chart')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
# Formatting the line colors
#plt.plot(x,y,'r')
# Formatting the line type
#plt.plot(x,y,'<')
#####################################################################
#Annotate
#plt.annotate(xy=[1,3], s='First Entry')
#plt.annotate(xy=[2,5], s='Second Entry')
######################################################################
# Adding Legends

######################################################################
#t=np.arange(0.,5.,0.2)
#plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
#plt.show()

#######################################################################
### Box Plot #################

# df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
# df.plot.box(grid='True')
# plt.show()
#######################################################################
####################### Line chart#####################################
# plt.plot(x,y, label ='first', color="red",linewidth=3)
# plt.plot(x1,y1, label ='Second', color="green",linewidth=3)
# plt.legend()
# plt.show()
#######################################################################
############## Bar CHART#############################################
# x = [2,4,6,8,10]
# y = [6,7,8,2,4]
# plt.bar(x,y,label ='bar1', color ='red')
# x2  = [1,3,5,9,11]
# y2  = [7,8,4,6,3]
# plt.bar(x2,y2,label ='bar2', color ='green')
########################################################################
####################### HIstogram ######################################
# population_ages = [22,55,62,45,21,22,34,42,42,4,99,35,64,100,102,88,78,67,58,49,93,87,67,58,101,104,111,80,45,60,36,39,47]
# bins = np.arange(0,130,10)
# plt.hist(population_ages,bins,histtype='bar')
# plt.legend(['Histogram'])
# plt.show()
########################################################################
##################### Scatter Plot######################################
# x = [1,2,3,4,5,6,7,8,9]
# y = [5,3,6,2,7,8,1,6,9]
# plt.scatter(x,y,label='Scatterchart', color = 'red',marker='*',s =100)
########################################################################
################### Stack Plots ########################################
# days = [1,2,3,4,5]
# sleeping = [7,8,6,11,5]
# eating = [4,5,3,8,9]
# working = [7,8,7,2,2]
# playing = [8,5,4,6,3]
# plt.stackplot(days,sleeping,eating,working,playing, colors =['m','c','r','k'],labels = ['Sleeping', 'Eating', 'Working','Playing'])
#########################################################################
############ Pie Chart##################################################
# slices  = [7,2,2,13]
# activities =['sleeping','eating','working','playing']
# colors =['c','m','r','b']
# plt.pie(slices, labels=activities,colors=colors,startangle=90,shadow= True,explode=(0,0.1,0,0),autopct='%1.1f%%')
#########################################################################
############### Read data from file ###############################
'''
### By Normal open file and read
x=[]
y=[]
with open('DataSet/Datacsv.csv','r') as fobj:
    plotvar = csv.reader(fobj,delimiter=',')
    for fvar in plotvar:
        x.append(int(fvar[0]))
        y.append(int(fvar[1]))
plt.plot(x,y,label ='Loaded from File',color ='red')
#######################################################
########### By numpy method############################
x,y = np.loadtxt('DataSet/Datacsv.csv',delimiter=',',unpack=True)
plt.plot(x,y,label ='Loaded from File',color ='green')
'''

########################## SubPlots##############################
fig = plt.figure()
def create_plot():
    xs = []
    ys = []
    for i in range(10):
        x = i
        y = random.randrange(10)
        xs.append(x)
        ys.append(y)
    return xs,ys

ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
x,y = create_plot()
ax1.plot(x,y)
x,y = create_plot()
ax2.plot(x,y)
#plt.legend()
plt.show()

print(random.randrange(10))

