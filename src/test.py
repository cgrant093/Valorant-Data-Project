# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 17:59:02 2022

@author: cgran
"""

from sklearn import preprocessing
from graphs import rank_order
from preprocessing import rank_lables

money = rank_lables()
print(money)

le = preprocessing.LabelEncoder()
print(le.fit_transform(rank_order()))

