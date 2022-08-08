'''
api_requests calls an API to collect:
    1. Last 5 matches
    2. Current account rank
    
API: https://docs.henrikdev.xyz/valorant.html
(github repo: https://github.com/Henrik-3/unofficial-valorant-api)
'''


import requests
import urllib.parse
import numpy as np
    
    
def get_rank(name, tag):
    
    base_webpage = 'https://api.henrikdev.xyz/valorant/'
    
    username_and_tag = f'{urllib.parse.quote(name)}/{urllib.parse.quote(tag)}'
    
    url = f'{base_webpage}v1/mmr/na/{username_and_tag}'
    
    # tries to request data from url json
    try:
        r = requests.get(url).json()
        
        rank = r['data']['currenttierpatched']
    
    except Exception:
        return np.nan
    
    else:
        return rank
      
    
def get_matches(name, tag, filter=False):
    
    base_webpage = 'https://api.henrikdev.xyz/valorant/'
    
    game_mode = ''
    
    username_and_tag = f'{urllib.parse.quote(name)}/{urllib.parse.quote(tag)}'
    
    if filter:
        game_mode = f'?filter={filter}'
    
    url = f'{base_webpage}v3/matches/na/{username_and_tag}{game_mode}'
    
    # tries to request data from url json   
    try:
        r = requests.get(url).json()
        
        matches = r['data']
        
        filtered_data = []
    
        for match in matches:
            # find list of all players
            all_players = match['players']['all_players']
            
            user_list = (user for user in all_players if user["name"] == name)
            
            # find the player matching the account information
            match_info = next(user_list, {})
        
            filtered_data.append(match_info)
            
    except Exception:
        return np.nan
    
    else:
        return filtered_data
    
    