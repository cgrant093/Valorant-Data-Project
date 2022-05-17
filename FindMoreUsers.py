'''
MatchAndRankRequest calls an API to collect:
    1. Last 5 matches
    2. Current account rank
    
API called: https://github.com/Henrik-3
'''

from MatchAndRankRequest import get_matches_and_rank
from AccountDataCollection import average_stats


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



def find_more_users(account, current_set, depth):
    '''Recursiver method:
        Acquires data for a given account
            Data: info from last five matches and account rank
            
        Averages the info from the five matches together
        
        If max_depth hasn't been reached:
            Use match data to find more account
            Then run this method again on those accounts'''
    
    
    ## see if account exists in set
    if account in current_set:
        return set()
    
    
    ## generate last 5 matches 
        ## and if no matches available return nothing
    matches, rank = get_matches_and_rank(account[0], account[1])
    
    if (matches == None) or (rank == None): 
        return set()
    
    
    ## acquire important account info from each match 
        # and average it together
    account = average_stats(account, matches, rank)
    
    
    ## add account to set
    current_set.add(account)
    
    
    ## if we have NOT reached max_depth, find more users and add to set
    if depth > 0:
        new_users = set().union(*[get_new_users(match) for match in matches])
        
        current_set |= set().union(*[find_more_users(user, current_set, depth-1) for user in new_users])

    
    return current_set