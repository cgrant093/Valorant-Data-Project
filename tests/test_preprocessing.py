# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 13:53:20 2022

@author: cgran
"""
import pytest
import pandas as pd
from sklearn import preprocessing
from graphs import rank_order

from preprocessing import (rank_lables, decode_rank_labels, encode_ranks, 
                           normalize_features, partition_dataset)

class TestRankLabels(object):
    def test_for_normal_values_1(self):
        labels = rank_lables()
        le = preprocessing.LabelEncoder()
        labels_from_transform = le.fit_transform(rank_order())
        assert len(labels) == len(labels_from_transform)
        assert all([l == t for l, t in zip(labels, labels_from_transform)])
    

class TestDecodeRankLabels(object):
    def test_for_normal_values_1(self):
        decoded_ranks = decode_rank_labels()
        ranks_labels = {
            label : rank
            for label, rank in zip(rank_lables(), rank_order())
            }
        assert len(decoded_ranks) == len(ranks_labels)
        assert all([d == r for d, r in zip(decoded_ranks, ranks_labels)])
        
    
class TestEncodeRanks(object):
    def test_for_normal_values_1(self):
        encoded_ranks = encode_ranks(rank_order())
        labels = rank_lables()
        assert len(encoded_ranks) == len(labels)
        assert all([e == l for e, l in zip(encoded_ranks, labels)])
    
    def test_for_empty_list(self):
        assert encode_ranks([]).size == 0
         
'''    
class TestNormalizeFeatures(object):
    def test_for_normal_values_1(self):
        features_list = ['red', 'green', 'blue']
        feature_dict = {feature : [1] for feature in features_list}
        df = pd.DataFrame(feature_dict)
        norm_df = normalize_features(df, features_list)
        
    
#class TestPartitionDataset(object):
#    def test_for_normal_values_1(self):
#        assert partition_dataset(2, 1, 1) == pytest.approx(2*100/4)'''

    

    
