import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import GradientBoostingRegressor
import pickle

from propertypro.propertypro import Propertypro

scraper = Propertypro()
data = scraper.scrape_data(2000, ['lagos','enugu', 'abuja'])



numeric = ['price', 'bedroom', 'bathroom', 'toilet', 'newly_built', 'furnished', 'serviced']
data[numeric] = data[numeric].apply(pd.to_numeric, errors='coerce').fillna(0).astype(np.int64)
data['location'] = LabelEncoder().fit_transform(data['location'])


X = data.drop(['title','price'],axis=1)
y = data['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

clf = GradientBoostingRegressor()
clf.fit(X_train, y_train)

# export pickle file
with open('model.pkl', 'wb') as fh:
   pickle.dump(clf, fh)


