'''

'''
import pytest
import numpy as np

from api_requests import (get_rank, get_matches)


class TestGetRank(object):
    def test_for_bad_name(self):
        assert np.isnan(get_rank('beta4days', '888w'))
        
    
class TestGetMatches(object):
    def test_for_bad_name(self):
        assert np.isnan(get_matches('beta4days', '888w'))


