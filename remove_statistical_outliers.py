# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 15:30:15 2022

@author: cgran
"""


import pandas as pd


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


def separate_df_by_rank(df):
    '''Creates separate dfs for each rank.
        For the purpose of finding and removing statistical outliners'''
    
    rank_dict = {rank : df.loc[(df['Rank'] == rank)] for rank in rank_order}
    
    return rank_dict
    
    
def combined_rank_df(rank_dict):
    '''Combines the separate rank dfs into one'''
    
    df = pd.DataFrame(columns=rank_dict['Radiant'].columns)
    
    for rank in rank_order:
        df = pd.concat([df, rank_dict[rank]])
    
    return df
    
       
def no_IQR_outliers(df):
    '''a function to find outliers using IQR
        and return the ones that are not outliers'''
    
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    
    not_outliers = df[~((df.lt(Q1 - 1.5*IQR)) 
                        | (df.gt(Q3 + 1.5*IQR))).any(axis=1)]
    
    return not_outliers
    
    
def remove_stat_outliers(df, data_path):
    '''removes statistical outliers from each rank'''
    
    rank_dict = separate_df_by_rank(df)
    
    no_outliers_dict = {rank: no_IQR_outliers(rank_dict[rank]) 
                        for rank in rank_dict}
    
    new_df = combined_rank_df(no_outliers_dict).reset_index(drop=True) 

    new_df.to_csv(f'{data_path}cleaned_total_list.csv', index=False)
    
    return new_df