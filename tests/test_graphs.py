import pytest
from graphs import (rank_order, change_plot_color, plot_rank_distribution, 
                    plot_avg_value, plot_avg_value_per_position)

class TestRankOrder(object):
    def test_for_normal_values_1(self):
        assert rank_order(2, 1, 1) == pytest.approx(2*100/4)
        
    
class TestChangePlotColor(object):
    def test_for_normal_values_1(self):
        assert change_plot_color(2, 1, 1) == pytest.approx(2*100/4)
        

class TestPlotRankDistribution(object):
    def test_for_normal_values_1(self):
        assert plot_rank_distribution(2, 1, 1) == pytest.approx(2*100/4)
        

class TestPlotAvgValue(object):
    def test_for_normal_values_1(self):
        assert plot_avg_value(2, 1, 1) == pytest.approx(2*100/4)
        

class TestPlotAvgValuePerPosition(object):
    def test_for_normal_values_1(self):
        assert plot_avg_value_per_position(2, 1, 1) == pytest.approx(2*100/4)
        
