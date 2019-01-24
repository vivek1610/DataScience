import numpy as np

####### Defining a list
Listdata = [[1,2,3,4],[5,6,7,8]]
print(Listdata)

####### Create an array from the list
Array = np.array(Listdata)
print(Array)

####### Find the class of data structure
print(Listdata.__class__)
print(Array.__class__)

####### Find the dimension of the array
print(Array.ndim)

####### Find the shape of the array
print(Array.shape)

####### Find Data Type that array holds
print(Array.dtype)

####### Create an array of zeros
print(np.zeros((3,6)))

####### An array of first 15 Numbers
print(np.arange(15))

####### An array of first 15 numbers and reshape all those numbers
print(np.arange(15).reshape(3,5))

###### Single Dimentional array
arrvar = np.arange(10)
print(arrvar)
print(arrvar[5])
print(arrvar[:5])
print(arrvar[5:])
print(arrvar[5:8])
print(arrvar[-1])
print(arrvar[-2])
print(arrvar[::-1])
arrvar[5:8] = 12
print(arrvar)

###### Multi dimentional Arraqy

mularr =np.arange(15).reshape(3,5)
print(mularr)
print(mularr[0,2])
print(mularr[2,4])

######## Selecting all rows and 1st 2 columns
print(mularr[:,0:2])
print(mularr[1:3,:])
print(mularr[0:2,0:2])

######## array transpose from row to column
print(mularr.T)
print(np.random.randn(6, 3))

######### Universal Fn.

uarr = np.arange(10)
print(np.sqrt(uarr))
print(np.exp(uarr))
print(np.square(uarr))

#############################################
######## Creating New Array
x = np.random.random(10)
y = np.random.random(10)
z = np.random.random(10)

arrdata = np.array(zip(x,y,z))
print(arrdata)
a = np.array([[1,2,3],[4,5,6]])
print(a)
b = np.zeros((2,1))
c = np.zeros((2,3))
print(b)
############### colum wise add
print(np.append(a,b,axis=1))
###############row wise add
print(np.append(a,c,axis=0))

######## Concatenating numpy arrays
arr = np.arange(12).reshape(3,4)
print(np.concatenate([arr,arr],axis=1))
print(np.concatenate([arr,arr],axis=0))
