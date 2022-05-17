'''
AccountDataCollection is a set of methods that:
    1. Averages values collect from MatchDataCollection
    
 
    the method average_stats is the main method of this file
        and the one that should be called
'''

from MatchDataCollection import get_data


###########################################################################
def character_to_position(character): 
    '''Given a specific agent, return class/position type'''
    char_pos_dict ={
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
    if not character in char_pos_dict:
        return None
    
    return char_pos_dict[character]


###########################################################################
def calc_position(position_dict):
    '''Finds the average agent class/team position of an account'''
    for position, count in position_dict.items():
        if count >= 3:
            return position
 
    ## if no obvious agent class, return Flex
    return 'Flex'


###########################################################################
def find_team_position(user_characters):
    '''Given the last five agents played,
        sets number of time a class/position was played'''

    position_count = {
        'Controller' : 0,
        'Initiator' : 0,
        'Sentinel' : 0,
        'Duelist' : 0
    }
    
    for character in user_characters:
        position = character_to_position(character)
        
        ## Checks to make sure agent data was properly collected
        if not (position == None):
            position_count[position] = position_count.get(position) + 1
    
    return calc_position(position_count)


###########################################################################
def average(key, match_stats):
    '''Calculates the average value for a specific stat
        given that some info was properly collected'''
    
    denom = len(match_stats)
    value = 0
    
    for d in match_stats:
        ## if they happen to have less than five matches
            ## I can still get a (smaller) average
        if d.get(key) == None:
            denom -= 1
        
        else:
            value += d.get(key)
    
    ## if no matches collected, return zero for the stat
    if denom == 0:
        return 'NaN'
    
    return round(value / denom, 4)


###########################################################################
def average_stats(account, matches, rank):
    '''Given a specific account and their last ~5 matches
        finds the average values for those important statistics'''
    
    match_stats = [get_data(match, account) for match in matches]
    
    avg_KD = average('KD', match_stats)
    avg_assists = average('assists', match_stats)
    avg_HS_perc = average('headshot_perc', match_stats)
    avg_ability_usage = average('ability_usage', match_stats)
    avg_team_position = find_team_position(list(d.get('character') for d in match_stats))
    
    return (account[0], account[1], rank, avg_team_position, 
        avg_KD, avg_assists, avg_HS_perc, avg_ability_usage)