


rank_order = [
    'Iron 1', 'Iron 2', 'Iron 3', 
    'Bronze 1', 'Bronze 2', 'Bronze 3',
    'Silver 1', 'Silver 2', 'Silver 3',
    'Gold 1', 'Gold 2', 'Gold 3',
    'Platinum 1', 'Platinum 2', 'Platinum 3',
    'Diamond 1', 'Diamond 2', 'Diamond 3',
    'Ascendant 1', 'Ascendant 2', 'Ascendant 3',
    'Immortal 1', 'Immortal 2', 'Immortal 3',
    'Radiant'
]


def get_ranked_df(df):
    '''Returns the mean, std, and sem for a given dataframe.
        Returns it in a dictionary.
        It orders it by a specific rank order'''
    
    ranked_df_dict = {
        'mean' : df.groupby(['Rank']).mean().reindex(rank_order),
        'std' : df.groupby(['Rank']).std().reindex(rank_order),
        'sem' : df.groupby(['Rank']).sem().reindex(rank_order)
    }
    
    return ranked_df_dict


def position_df(df, position):
    '''Returns specific subdataframes based on position.
        calls ranked_df to get subdictionary of mean, std, and sem
        Returns it in a dictionary.'''
    
    pos_df = df.loc[(df['Position'] == position)]

    return get_ranked_df(pos_df)

    
def get_ranked_pos_df(df):
    '''Creates dictionary of all positions dataframes.'''
    
    position_dict = {
        'Duelist' : position_df(df, 'Duelist'),
        'Initiator' : position_df(df, 'Initiator'),
        'Sentinel' : position_df(df, 'Sentinel'),
        'Controller' : position_df(df, 'Controller'),
        'Flex' : position_df(df, 'Flex')
    }
    
    return position_dict
    
    
