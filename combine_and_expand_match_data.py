# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 15:57:46 2022

@author: cgran
"""


import os
import pandas as pd
import json


unnecessary_columns = [
    'Matches', 'session_playtime', 'player_card', 'assets', 'tag', 'spent', 
    'puuid', 'name', 'stats', 'player_title', 'party_id', 'behavior', 'team',
    'platform', 'currenttier', 'loadout_value', 'ability_casts', 'economy' 
]


def json_recomp(json_string):
    json_data = json_string
    
    if (type(json_string) == str):
        json_string = json_string.replace("None", "0")
        json_data = json.loads(json_string.replace("'", "\""))   
        
    return json_data


def new_df_from_file(match_path, file):
     # reads in new dataframe from file
     new_df = pd.read_csv(f'{match_path}{file}', 
                          na_filter=True, na_values='[]')
     new_df = new_df.dropna(how='any')
     
     # recomps the Matches column so that its a list and not a string
     df = new_df[['User', 'Tag', 'Rank']].copy()
     df['Matches'] = new_df['Matches'].apply(json_recomp)
     df = df.dropna(how='any')
     
     return df
     

def expand_economy_data(df):
    
    spent_df = df['spent'].apply(pd.Series)
    spent_df = spent_df.rename(columns={'overall': 'total_spent', 
                                        'average': 'avg_spent'})
    df = pd.concat([df, spent_df], axis=1)

    load_df = df['loadout_value'].apply(pd.Series)
    load_df = load_df.rename(columns={'overall': 'total_loadout', 
                                      'average': 'avg_loadout'})
    df = pd.concat([df, load_df], axis=1)
    
    return df


def expand_match_data(df):
    
    # converts list in Matches column
    # into multiple rows
    df = df.explode('Matches').reset_index(drop=True)
    
    # expands the dictionaries in the Matches column into multiple columns
    df = pd.concat([df, df['Matches'].apply(pd.Series)], axis=1)
    
    # expands dictionaries found in the new columns
    df = pd.concat([df, df['ability_casts'].apply(pd.Series)], axis=1)
    df = pd.concat([df, df['stats'].apply(pd.Series)], axis=1)
    df = pd.concat([df, df['economy'].apply(pd.Series)], axis=1)
    
    # expands the last dictionary found in the new economy column
    df = expand_economy_data(df)
    
    # drops all unnecessary columns
    df = df.drop(columns=unnecessary_columns)
    
    return df


def combine_match_dfs(data_path, match_path):
    
    match_df = pd.DataFrame()
    
    # compile into one dataframe
    files = [file for file in os.listdir(match_path) 
             if os.path.isfile(os.path.join(match_path, file))]
    
    for file in files:
        # reads in new dataframe from file
        # and cleans up some rows/columns
        df = new_df_from_file(match_path, file)
        
        # expands the match data column into multiple rows and columns
        df = expand_match_data(df)
        
        # concats to new df
        try:
            # some dfs have multiple columns labeled '0'
            # and the only values in the column are NaN
            if (0 in df.columns):
                df = df.drop(columns=[0])
                
            match_df = pd.concat([match_df, df])
        
        except:
            pass
    
    # resets index
    match_df = match_df.reset_index(drop=True)
    
    # saves to a list
    match_df.to_csv(f'{data_path}match_total_list.csv', index=False)
    
    return match_df