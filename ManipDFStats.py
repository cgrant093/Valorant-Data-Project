import pandas as pd


###########################################################################
def rank_order():
    '''returns a list of the rank order'''
    
    ro = ['Iron 1', 'Iron 2', 'Iron 3', 
              'Bronze 1', 'Bronze 2', 'Bronze 3',
              'Silver 1', 'Silver 2', 'Silver 3',
              'Gold 1', 'Gold 2', 'Gold 3',
              'Platinum 1', 'Platinum 2', 'Platinum 3',
              'Diamond 1', 'Diamond 2', 'Diamond 3',
              'Immortal 1', 'Immortal 2', 'Immortal 3',
              'Radiant']
    
    return ro


###########################################################################
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


###########################################################################
def position_df(df, position):
    '''Returns specific subdataframes based on position.
        calls ranked_df to get subdictionary of mean, std, and sem
        Returns it in a dictionary.'''
    
    pos_df = df.loc[(df['Position'] == position)]

    return get_ranked_df(pos_df)

    
###########################################################################
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
    
    
###########################################################################
def separate_df_by_rank(df):
    '''Creates separate dfs for each rank.
        For the purpose of finding and removing statistical outliners'''
    
    rank_dict = {rank : df.loc[(df['Rank'] == rank)] for rank in rank_order()}
    
    return rank_dict
    
    
###########################################################################
def combined_rank_df(rank_dict):
    '''Combines the separate rank dfs into one'''
    
    df = pd.DataFrame(columns=rank_dict['Radiant'].columns)
    
    for rank in rank_order():
        df = pd.concat([df, rank_dict[rank]])
    
    return df
    
    
###########################################################################   
def not_outliers_IQR(df):
    '''a function to find outliers using IQR
        and return the ones that are not outliers'''
    
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    
    not_outliers = df[~((df.lt(Q1 - 1.5 * IQR)) | (df.gt(Q3 + 1.5 * IQR))).any(axis=1)]
    
    return not_outliers
    
    
###########################################################################
def remove_stat_outliers(df):
    '''removes statistical outliers from each rank'''
    
    rank_dict = separate_df_by_rank(df)
    
    no_outliers_dict = {rank: not_outliers_IQR(rank_dict[rank]) for rank in rank_dict}
    
    return combined_rank_df(no_outliers_dict)