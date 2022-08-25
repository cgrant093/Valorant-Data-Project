from graphs import rank_order


def get_ranked_df(df):
    '''Returns the mean, std, and sem for a given dataframe.
        Returns it in a dictionary.
        It orders it by a specific rank order'''
    
    ranked_df_dict = {
        'mean' : df.groupby(['Rank']).mean().reindex(rank_order()),
        'std' : df.groupby(['Rank']).std().reindex(rank_order()),
        'sem' : df.groupby(['Rank']).sem().reindex(rank_order())
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
        'Controller' : position_df(df, 'Controller')
    }
    
    return position_dict
    
    
