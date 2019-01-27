import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
import numpy as np
dataset = pd.read_excel("E:/vivek/Study Material Data Science/30 - Factor Analysis-Unsuper/Factor Analysis.xlsx",sheet_name=0)
print(dataset.head())
X=dataset.values
X=scale(X)
pca = PCA(n_components=7)
print(pca.fit(X))
print(pca.explained_variance_) ### variance
print(pca.explained_variance_ratio_) ## VAriance Ratio
pca=PCA(n_components=3)
print(pca.fit(X))
print(pd.DataFrame(pca.components_))