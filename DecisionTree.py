import pandas as pd
import numpy as np
from sklearn import tree
from sklearn import preprocessing
titanic_train  = pd.read_csv("E:/vivek/Study Material Data Science/26 - Decision Tree/train.csv")
#titanic_train = pd.read_csv("E:/vivek/Study Material Data Science/26 - Decision Tree/train.csv",sheet_name=0)
print(titanic_train.head())
new_age_var=np.where(titanic_train["Age"].isnull(),28,titanic_train["Age"])
titanic_train["Age"]=new_age_var
#print(titanic_train["Age"])
label_encoder=preprocessing.LabelEncoder()
encoded_sex=label_encoder.fit_transform(titanic_train["Sex"])
tree_model=tree.DecisionTreeClassifier()
print(tree_model.fit(X=pd.DataFrame(encoded_sex),y=titanic_train["Survived"]))
with open("E:/vivek/Study Material Data Science/26 - Decision Tree/DTree1.dot", 'w') as f:
    f = tree.export_graphviz(tree_model, feature_names=["Sex"], out_file=f)

from IPython.display import Image
print(Image("E:/vivek/Study Material Data Science/26 - Decision Tree/DTree1.png"))