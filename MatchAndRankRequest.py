'''
MatchAndRankRequest calls an API to collect:
    1. Last 5 matches
    2. Current account rank
    
API called: https://github.com/Henrik-3
'''


import requests
import urllib.parse


###########################################################################
def get_matches_and_rank(name, tag):
    '''Calls API from https://github.com/Henrik-3'''
    
    base_webpage = 'https://api.henrikdev.xyz/valorant/'
    
    urls = [f'{base_webpage}v3/matches/na/{urllib.parse.quote(name)}/{urllib.parse.quote(tag)}',
            f'{base_webpage}v1/mmr/na/{urllib.parse.quote(name)}/{urllib.parse.quote(tag)}']
    
    def get(url):
        try:
            return requests.get(url).json()
            
        except Exception:
            return None
    
    r = [get(url) for url in urls]
    
    if (r[0] == None) or (r[1] == None):
        return None, None
    
    ## sends back data from json if it exists
    if ('data' in r[0].keys()) and ('data' in r[1].keys()):
        return r[0]['data'], r[1]['data']['currenttierpatched']
    
    return None, None
    
    
    
###########################################################################
def get_rank(name, tag):
    '''Calls API from https://github.com/Henrik-3'''
    
    base_webpage = 'https://api.henrikdev.xyz/valorant/'
    
    url = f'{base_webpage}v1/mmr/na/{urllib.parse.quote(name)}/{urllib.parse.quote(tag)}'
    
    def get(url):
        try:
            return requests.get(url).json()
            
        except Exception:
            return None
    
    r = get(url)
    
    if (r == None):
        return None
    
    ## sends back data from json if it exists
    if ('data' in r.keys()) :
        return r['data']['currenttierpatched']
    
    return None
    
    
    
###########################################################################
def get_matches(name, tag):
    '''Calls API from https://github.com/Henrik-3'''
    
    base_webpage = 'https://api.henrikdev.xyz/valorant/'
    
    url = f'{base_webpage}v3/matches/na/{urllib.parse.quote(name)}/{urllib.parse.quote(tag)}',
    
    def get(url):
        try:
            return requests.get(url).json()
            
        except Exception:
            return None
    
    r = get(url)
    
    if (r == None):
        return None
    
    ## sends back data from json if it exists
    if ('data' in r.keys()) :
        return r['data']
    
    return None