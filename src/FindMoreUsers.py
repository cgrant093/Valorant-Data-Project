'''
MatchAndRankRequest calls an API to collect:
    1. Last 5 matches
    2. Current account rank
    
API called: https://github.com/Henrik-3
'''

import pandas as pd
from MatchAndRankRequest import get_matches, get_rank
from AccountDataCollection import average_stats


###########################################################################
def get_new_users(match):
    '''finds new users from a given match'''
    
    ## returns empty set if match doesn't exists
    if match == None:
        return set()
    
    ## returns empty set if match data wasn't properly collected
    if not('players' in match):
        return set()
    
    players = match['players']['all_players']
    
    return set([(player['name'], player['tag']) for player in players])



###########################################################################
def find_more_users(account, curr_set, df, depth):
    '''Recursiver method:
        Acquires data for a given account
            Data: info from last five matches and account rank
            
        Averages the info from the five matches together
        
        If max_depth hasn't been reached:
            Use match data to find more account
            Then run this method again on those accounts'''
    
    ## see if account exists in set
    if account in curr_set:
        return set(), pd.DataFrame()
    
    rank = get_rank(account[0], account[1])
    
    if rank == None:
        return set(), pd.DataFrame()
    
    ## generate last 5 matches 
        ## and if no matches available return nothing
    matches = get_matches(account[0], account[1])  
    
    if matches == None: 
        return set(), pd.DataFrame()
    
    for match in matches:
        match_info = {
                    'User' : account[0],
                    'Tag' : account[1],
                    'Rank' : rank,
                    'Match' : match
                    }
        
        df = df.append(match_info , ignore_index=True)
    
    ## add account to set
    curr_set.add(account)
    
    
    ## if we have NOT reached max_depth, find more users and add to set
    if depth > 0:
        new_users = set().union(*[get_new_users(match) for match in matches])
        
        new_list, df = [find_more_users(user, curr_set, df, depth-1) for user in new_users]

        curr_set |= set().union(*new_list)

    
    return curr_set, df
    
    

###########################################################################
def find_user_rank(name, tag):

    ## gets account rank
    rank = get_rank(name, tag)
    
    if rank == None:
        return None
    
    return rank

def find_user_matches(name, tag):
    ''' '''
    
    ## generate last 5 matches 
        ## and if no matches available return nothing
    matches = get_matches(name, tag)  
    
    if matches == None: 
        return pd.DataFrame()
   
    df = pd.DataFrame(columns = ['User', 'Tag', 'Rank', 'Match'])
    
    for match in matches:
        match_info = {
                    'User' : name,
                    'Tag' : tag,
                    'Rank' : rank,
                    'Match' : match
                    }
        
        df = df.append(match_info , ignore_index=True)
    
    return df