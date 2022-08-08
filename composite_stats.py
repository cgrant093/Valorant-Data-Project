'''
composite_stats is a set of methods that:
    1. Extract data from a single a match info
    2. Calculate some values off of that data
    3. Check for error in url request.
        If the info wasn't collect, to correct for that
'''


import numpy as np


def headshot_percentage(headshots, bodyshots, legshots):
    '''Calculates the headshot percentage for a given map'''

    total_shots = headshots + bodyshots + legshots
    
    ## If total shots = 0, then return 0, so we don't blow up the computer
    if total_shots == 0:
        return 0
    
    return (headshots*100/(total_shots))


def KD_calc(kills, deaths):
    '''Calculates kill/death ratio for a given map'''
    
    ## If deaths = 0, then return 0, so we don't blow up the computer
    if deaths == 0:
        return 0
    
    return (kills/deaths)


def team_position(character): 
    '''Given a specific agent, return class/position type'''
    
    position_dict ={
        'Astra' : 'Controller',
        'Breach' : 'Initiator',
        'Brimstone' : 'Controller',
        'Chamber' : 'Sentinel',
        'Cypher' : 'Sentinel',
        'Fade' : 'Initiator',
        'Jett' : 'Duelist',
        'KAY/O' : 'Initiator',
        'Killjoy ' : 'Sentinel',
        'Neon' : 'Duelist',
        'Omen' : 'Controller',
        'Phoenix' : 'Duelist',
        'Raze' : 'Duelist',
        'Reyna' : 'Duelist',
        'Sage' : 'Sentinel',
        'Skye' : 'Initiator',
        'Sova' : 'Initiator',
        'Viper' : 'Controller',
        'Yoru' : 'Duelist'
    }
    
    ## If character not properly collected, return None
    if not character in position_dict:
        return np.nan
    
    return position_dict[character]


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

    return df