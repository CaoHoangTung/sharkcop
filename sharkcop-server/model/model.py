import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from mlxtend.plotting import plot_decision_regions
# from sklearn import datasets
from pandas.plotting import scatter_matrix
from joblib import dump, load
import collections

kaggle_data = pd.read_csv('data/kaggle.csv')
data = pd.read_csv('data/new_data.csv')

kaggle_X = kaggle_data.iloc[:, :30].values
X = data.drop(['index'],axis=1).iloc[:, :30].values
y = data.iloc[:,-1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.99)
kaggle_X_train, kaggle_X_test, kaggle_y_train, kaggle_y_test = train_test_split(X, y, test_size = 0.02)

svclassifier = SVC(kernel='poly',degree=5)
svclassifier.fit(kaggle_X_train, kaggle_y_train)
dump(svclassifier, 'pre_model.joblib')

y_pred = svclassifier.predict(X_test)

print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
# print("X=%s, Predicted=%s" % (test_2d, y_pred_test[0]))
# print(y_pred.shape)

# TESTING ZONE

X = [[-1,1,0,-1,-1,-1,1,0,-1,1,1,-1,0,0,-1,-1,-1,-1,0,1,0,0,0,-1,1,1,1,1,-1,-1]]
print("PREDICTION:",svclassifier.predict(X))
