# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 08:34:17 2020

@author: cpx
"""
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

RelicsData = pd.read_excel('圣遗物副属性.xlsx')
RelicsData.fillna(0, inplace=True )
features = ['ATK', 'ATK_1', 'CR', 'CD', 'EM', 'EE', 'HP', 'HP_1', 'DEF', 'DEF_1']
# print(features[:10])
X_train = RelicsData[features]
len_X = len(X_train)
Y_train = np.ones((len_X,), dtype = np.int)*4
# X_train.info()
linreg = LinearRegression(fit_intercept = False)#将截距设置为0
linreg.fit(X_train,Y_train)
y_predict = linreg.predict(X_train)
print(linreg.score(X_train, Y_train))
print(linreg.coef_, '截距:%.3f' %linreg.intercept_)
# print(linreg.get_params())
# RelicsData.info()
# print('ok')
# print(RelicsData.describe())