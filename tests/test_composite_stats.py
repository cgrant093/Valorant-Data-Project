'''

'''
import pytest
import numpy as np
import pandas as pd

from composite_stats import (headshot_percentage, KD_calc, 
                             team_position, composite_player_stats)

class TestHeadshotPercentage(object):
    def test_for_normal_values_1(self):
        assert headshot_percentage(2, 1, 1) == pytest.approx(2*100/4)
        
    def test_for_normal_values_2(self):
        assert headshot_percentage(3, 3, 7) == pytest.approx(3*100/13)
        
    def test_for_normal_values_3(self):
        assert headshot_percentage(1, 4, 3) == pytest.approx(100/8)
    
    def test_for_no_headshots(self):
        assert headshot_percentage(0, 1, 1) == pytest.approx(0)
        
    def test_for_only_headshots(self):
        assert headshot_percentage(1, 0, 0) == pytest.approx(100)
        
        
class TestKDCalc(object):
    def test_for_normal_values_1(self):
        assert KD_calc(2, 1) == pytest.approx(2/1)
    
    def test_for_normal_values_2(self):
        assert KD_calc(3, 2) == pytest.approx(3/2)
        
    def test_for_normal_values_3(self):
        assert KD_calc(4, 4) == pytest.approx(4/4)
        
    def test_for_no_kills(self):
        assert KD_calc(0, 1) == pytest.approx(0)
    
    def test_for_no_deaths(self):
        assert KD_calc(1, 0) == pytest.approx(1)

   
class TestTeamPosition(object):
    def test_for_normal_values_1(self):
        assert team_position('Astra') == 'Controller'
    
    def test_for_normal_values_2(self):
        assert team_position('Fade') == 'Initiator'
        
    def test_for_normal_values_3(self):
        assert team_position('Sage') == 'Sentinel'
    
    def test_for_wrong_character(self):
        assert np.isnan(team_position('Cody'))
    
    def test_for_None_character(self):
        assert np.isnan(team_position(None))
    
    def test_for_nan_character(self):
        assert np.isnan(team_position(np.nan))
    
  
#class TestCompositePlayerStats(object):
    
"""
def composite_player_stats(match_df):
    
    match_df = match_df.dropna(how='any')
    match_df = match_df[~(match_df['avg_spent'] == 0)]
    match_df = match_df[~(match_df['avg_loadout'] == 0)]
    
    rounds = match_df['total_spent'].values / match_df['avg_spent'].values
    match_df['rounds'] = np.rint(rounds).astype(int)
    
    match_df['ability_usage'] = (match_df['c_cast'] 
                                 + match_df['q_cast']
                                 + match_df['e_cast'] 
                                 + match_df['x_cast']) 
    
    df = match_df[['User', 'Tag', 'Rank', 'level', 
                   'avg_spent', 'avg_loadout']].copy()
    
    df['Position'] = match_df.apply(
        lambda r: team_position(r.character), 
        axis=1)
        
    df['HS_perc'] = match_df.apply(
        lambda r: headshot_percentage(r.headshots, r.bodyshots, r.legshots), 
        axis=1)
    
    df['KD'] = match_df['kills'] / match_df['deaths']
    df['avg_assists'] = match_df['assists'] / match_df['rounds']
    df['avg_ability_usage'] = match_df['ability_usage'] / match_df['rounds']
    df['avg_score'] = match_df['score'] / match_df['rounds']
    df['avg_dmg_made'] = match_df['damage_made'] / match_df['rounds']
    df['avg_dmg_rec'] = match_df['damage_received'] / match_df['rounds']

    return df"""