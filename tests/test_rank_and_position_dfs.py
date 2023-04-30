import pytest
from rank_and_position_dfs import (get_ranked_df, position_df, 
                                   get_ranked_pos_df)

class TestGetRankedDf(object):
    def test_for_normal_values_1(self):
        assert get_ranked_df(2, 1, 1) == pytest.approx(2*100/4)


class TestPositionDf(object):
    def test_for_normal_values_1(self):
        assert position_df(2, 1, 1) == pytest.approx(2*100/4)


class TestGetRankedPosDf(object):
    def test_for_normal_values_1(self):
        assert get_ranked_pos_df(2, 1, 1) == pytest.approx(2*100/4)



