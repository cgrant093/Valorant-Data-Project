'''
MatchDataCollection is a set of methods that:
    1. Extract data from a single a match info
    2. Calculate some values off of that data
    3. Check for error in url request.
        If the info wasn't collect, to correct for that
'''


###########################################################################
def headshot_percentage(headshots, bodyshots, legshots):
    '''Calculates the headshot percentage for a given map'''
    
    ## If any shots were not collected, set that shot to zero
    if headshots == None:
        headshots = 0
    
    if bodyshots == None:
        bodyshots = 0
    
    if legshots == None:
        legshots = 0

    total_shots = headshots + bodyshots + legshots
    
    ## If total shots = 0, then return 0, so we don't blow up the computer
    if total_shots == 0:
        return 0
    
    return headshots * 100 / (total_shots)


###########################################################################
def sum_abilities(abilities):
    '''Calculates total ability usage for a given map'''
    
    ## If any abilities were not collected, set that ability value to zero
    if abilities['e_cast'] == None:
        abilities['e_cast'] = 0
    
    if abilities['q_cast'] == None:
        abilities['q_cast'] = 0
    
    if abilities['c_cast'] == None:
        abilities['c_cast'] = 0
    
    if abilities['x_cast'] == None:
        abilities['x_cast'] = 0
    
    return (abilities['e_cast'] + abilities['q_cast'] 
        + abilities['c_cast'] + abilities['x_cast'])


###########################################################################
def KD_calc(kills, deaths):
    '''Calculates kill/death ratio for a given map'''
    
    ## If either stat wasn't not collected, set it to zero
    if kills == None:
        return 0
    
    if deaths == None:
        return 0
    
    ## If deaths = 0, then return 0, so we don't blow up the computer
    if deaths == 0:
        return 0
    
    return kills / deaths


###########################################################################
def get_data(match, account):
    '''Collects all significant stats for a given map
        and returns them in a dictionary'''
    
    ## if match data wasn't properly collect, return empty dictionary
    if not('players' in match.keys()):
        return {}
    
    all_players = match['players']['all_players']
    
    user = next((player for player in all_players if player["name"] == account[0]), None)

    ## if user no longer exists, return empty dictionary
    if user == None:
        return {}
    
    user_stats = user['stats']
    ability_usage = sum_abilities(user['ability_casts']) 
    HS_perc = headshot_percentage(user_stats['headshots'], user_stats['bodyshots'], user_stats['legshots'])
    assists = user_stats['assists']
    
    ## if assists weren't properly collected, set them to zero
    if assists == None:
        assists = 0 
    
    user_info = {
        'KD' : KD_calc(user_stats['kills'], user_stats['deaths']),
        'assists' : assists,
        'headshot_perc' : HS_perc,
        'character' : user['character'],
        'ability_usage' : ability_usage
    }

    return user_info