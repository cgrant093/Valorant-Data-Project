# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 15:57:46 2022

@author: cgran
"""
import pytest
from combine_and_expand_match_data import (json_recomp, new_df_from_file, 
                                           expand_economy_data, 
                                           expand_match_data, 
                                           combine_match_dfs)

class TestJsonRecomp(object):
    def test_for_normal_values_1(self):
        assert json_recomp(2, 1, 1) == pytest.approx(2*100/4)


class TestNewDfFromFile(object):
    def test_for_normal_values_1(self):
        assert new_df_from_file(2, 1, 1) == pytest.approx(2*100/4)
    

class TestExpandEconomyData(object):
    def test_for_normal_values_1(self):
        assert expand_economy_data(2, 1, 1) == pytest.approx(2*100/4)
    

class TestExpandMatchData(object):
    def test_for_normal_values_1(self):
        assert expand_match_data(2, 1, 1) == pytest.approx(2*100/4)
        

class TestCombineMatchDfs(object):
    def test_for_normal_values_1(self):
        assert combine_match_dfs(2, 1, 1) == pytest.approx(2*100/4)
