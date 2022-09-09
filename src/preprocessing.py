# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 13:53:20 2022

@author: cgran
"""

import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from graphs import rank_order
        
def rank_lables():
    #creating labelEncoder
    le = preprocessing.LabelEncoder()
    return le.fit_transform(rank_order())

def decode_rank_labels():
    rank_labels = {
        label : rank
        for label, rank in zip(rank_lables(), rank_order())
        }
    return rank_labels

def encode_ranks(ranks):
    #creating labelEncoder
    le = preprocessing.LabelEncoder()
    return le.fit_transform(ranks)

def normalize_features(full_df, features_list):
    df = full_df[features_list].copy()
    df = df / df.max()
    
    return df.values

def partition_dataset(full_df, features_list):
    # normalize features
    features = normalize_features(full_df, features_list)
    # convert ranks to labels (ints)
    rank_labels = encode_ranks(full_df.Rank)
    
    # Shuffle Entire Dataset to Make Random
    X_train, X_test, y_train, y_test = train_test_split(
        features, rank_labels, test_size=0.2
        )
    
    return X_train, X_test, y_train, y_test
    
    
    
    
    
    

    
