import pandas as pd
import numpy as np
from sklearn import neighbors
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

dataset = pd.read_csv("E:/vivek/Study Material Data Science/35 - KNN/Titanic_Survival_train.csv")
print(dataset.head())
dataset.rename(columns={60:'pclass'},inplace=True)
print(dataset)
y=dataset["Pclass"]
X=dataset.drop(["Pclass"],axis=1)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)
knn = neighbors.KNeighborsClassifier(n_neighbors=4)
print(knn.fit(X_train,y_train).score(X_test,y_test))
y_pred=knn.predict(X_test)
print(y_pred)
print(confusion_matrix(y_test,y_pred))

### 0.7265917602996255 means 72% data is classified when 4 neighbors

#Below is confusion matrix
#[[135   7   6]
# [ 34   9   6]
# [ 13   7  50]]