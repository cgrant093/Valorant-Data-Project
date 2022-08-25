Firstly, I would like to say that this is a work in progress. Currently, I was refactoring my code and rewriting the files to match the PEP8 documentation. More detailed progress updates can be found at the bottom of the readme.


# What is Valorant?
Valorant is an online game where two teams (each with 5 players) compete to be the first team to win 13 rounds in a game. An individual player can be better at the game in one of two generic ways: 

1. they have more mechanical ability (equates to pressing buttons faster and moving their mouse more precisely) 
2. they have a smarter game strategy, which can make up for mechanical ability by outplaying the players on the opposite team


## Valorant has a 'smurfing' problem
Valorant, like any other online game, has a smurfing problem. This is when a player creates new accounts to play with people signifcantly worse than them (with regards to mechanical ability and/or game strategy). This is a problem because Valorant has a built in match making system that is supposed to queue you with players of the same skill level via some hidden algorithm. This problem makes the game not fun to play for the lower skilled players because the game feels unfair.


## Can we do something about the smurfing problem?
Due to the complexity of the game, there are many in-game statistics that can relate to a person's mechanical ability, and some that can imply their game strategy. I want to see how these statistics change based on the given rank a player is. Rank is set by a different hidden algorithm in Valorant, the higher your rank, the better player Valorant thinks you are. Perhaps we can reverse engineer the aspects of the algorithm that are important to rank and be able to catch a player's true rank before their new account catches up to their skill level.

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Current Progress

## A. Acquire a large list of accounts and account statistics
Aside from leaderboards found on websites, like [tracker.gg](https://tracker.gg/valorant/leaderboards/ranked/all/default?page=1), there is no player list in Valorant. The leaderboard found on [tracker.gg](https://tracker.gg/valorant/leaderboards/ranked/all/default?page=1) only has the top 1000 accounts or so in any given region. This of course would be a biased dataset if I only used these accounts as it would only give me statistics about the upper ranks. With the help of an [API](https://github.com/Henrik-3/unofficial-valorant-api) by Henrik-3, I wrote a recursive program that collects accounts from small list of players. It would look at their past few games played and collect all the accounts they played with. These accounts would be added to a set, and I did this until I had 10s of thousands, if not 100s of thousands, of accounts. 

Afterwards, I sent another [API](https://github.com/Henrik-3/unofficial-valorant-api) to the whole list of accounts and found all relevant data for their last couple of matches. If I were to do this again, I would probably do them in the same step, and/or add the accounts as keys to a dictionary where the value is a boolean that tells me if their account statistics has been added to the pandas dataframe yet.


## B. Cleaning the data

The data needs to be cleaned. The first thing that needs to be done is a restructuring of data. For the API requests to run as fast as possible, I collected all game data for X number of games from a player and moved on. However, there is a lot of game data that I didn't think was necessary for my project. So this column in the dataframe was 'exploded' to multiple rows for users with multiple games saved, and expanded to multiple columns for the in-game statistics that I thought necessary for the project. 

I also removed the accounts with missing data and removed the statistical outliers from the data. Whether someone was a statistical outlier depended on their in-game rank, and I did this to remove the people who are perhaps smurfing, cheating, or hadn't played the game in a while as to not skew the data in either direction.

After cleaning the data, I was left with this distribution of account ranks:

![my rank distribution](./plots/clean_dist_black.png#gh-dark-mode-only)
![my rank distribution](./plots/clean_dist_white.png#gh-light-mode-only)

Which is very similar to the bar chart found on [tracker.gg](https://tracker.gg/valorant/leaderboards/ranked/all/default?page=1). Although, I have not written a statistical test to check how similar the two distributions are, and will do that in the future.


## C. Finding the significant features

I plotted each in-game statistics per rank to find the signficant features. The features labels are in video game jargon and there isn't much I can do about that. Labeling the features without video game jargon would make the project more confusing in the code and to the people that understand valorant.

The features I found that can relate mechanical ability and/or game strategy to a persons rank are:
1. KD Ratio (number of times the player killed someone divided by the number of times they died)

![KD rank](./plots/KD_rank_black.png#gh-dark-mode-only)
![KD_rank](./plots/KD_rank_white.png#gh-light-mode-only)

I found that some other features I chose had nearly the same lineplot as the one above, so I decided to not utilize Average Combat Score (ACS) and Average Damage Given. This makes sense that they are similar as damage can be closely related to kills and kills are the main decider in the hidden algorithm for ACS.


2. Headshot Percentage (number of times the players gun bullet hit another's head divided by the number of bullets that hit another player (head, body, legs))

![HS perc rank](./plots/HS_perc_rank_black.png#gh-dark-mode-only)
![HS perc rank](./plots/HS_perc_rank_white.png#gh-light-mode-only)


3. Average Ability Usage (players choose character with different ability (or super powers) along side the guns they use in each game)

![avg Ability Usage_rank](./plots/avg_ability_usage_rank_black.png#gh-dark-mode-only)
![avg Ability Usage_rank](./plots/avg_ability_usage_rank_white.png#gh-light-mode-only)


4. Average Damage Received (damage the player received from others per round)

![Avg Dam Rec_rank](./plots/avg_dmg_rec_rank_black.png#gh-dark-mode-only)
![Avg Dam Rec_rank](./plots/avg_dmg_rec_rank_white.png#gh-light-mode-only)


5. Average spent (guns and abilities cost money which you earn during rounds by doing various things)

![Avg econ spent](./plots/avg_spent_rank_black.png#gh-dark-mode-only)
![Avg econ spent](./plots/avg_spent_rank_white.png#gh-light-mode-only)


6. Average loadout (you can keep a gun from a previous round by not dying, and this gun doesn't cost you money this round by still contribute to your average loadout)

![Avg econ loadout](./plots/avg_loadout_rank_black.png#gh-dark-mode-only)
![Avg econ loadout](./plots/avg_loadout_rank_white.png#gh-light-mode-only)


7. Account level (this is leveled up by playing games, you can be someone with a high account level because you play a lot, but that doesn't necessarily mean you'll get better at the game). Although, the graph shows that it's roughly exponential.

![Account level](./plots/level_rank_black.png#gh-dark-mode-only)
![Account level](./plots/level_rank_white.png#gh-light-mode-only)


8. Lastly, there is Average Assists (this is for if you've helped kill an enemy player in some way, but didn't give the killing blow). I'm not sure this feature is useful due to it leveling out relatively quickly.

![Avg assists](./plots/avg_assists_rank_black.png#gh-dark-mode-only)
![Avg assists](./plots/avg_assists_rank_white.png#gh-light-mode-only)

 
 
Also, in terms of rank, a player can also have a particular 'position' on the team. When choosing a character, they have different abilities (or super powers) and these abilities have different uses. Valorant has divided up the characters into four main groups depending on their set of abilities. 

I also wanted to look at the statistics based on rank and position. However, I found that other than the Average Assists plot, the plots for each stat based position (and rank) largely follow the same curve as the one only based on rank, and different characters a player chooses seems to have negligable outcomes on their rank.




## D. Future update: Creating a model to determine if someones stats and rank make up 
This is a future feature at the moment, but I am thinking of using a k nearest neighbor (KNN) model generated in PyTorch or with scikit-learn. I am also mulling over the idea of using a couple machine learning models and statistical tests to see if they all stat the same thing.

Afterwards, I should be able to run the model with a specific player account. If that account has a rank, it should tell me if it believes they should be that rank and if not, what rank they should be with some confidence level. If it doesn't have a rank, it should be able to just execute the second part.

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Software
The code is comprised of Python (.py) files as well as Jupyter notebooks. The main packages in use are pandas, matplotlib, requests, and numpy.

All .py files are essentially libraries/method holders so the Jupyter notebooks are less cluttered:

| File                          	| What does it do?     |
| ----------------------------- 	| -------------:|
| initial_data_scrap            	| Jupyter notebook that collects the account data from the different seeded accounts, exports to CSVs, merges all CSVs, and plots distribution of ranks | 
| feature_study  			| Jupyter notebook that removes data with missing information, removes statistical outliers from each rank by calling ManipDFStats.py, and plots average account stats vs rank (and position) | 
| api_requests.py          		| functions that call the [API](https://github.com/Henrik-3/unofficial-valorant-api) to request account data | 
| combine_and_expand_match_data.py      | expands the match data dictionary column into multiple rows and columns |
| composite_stats.py			| calculates all composite and averaged stats for each row | 
| graphs.py				| customizes and plots all the graphs |
| rank_and_position_dfs.py		| separates dataframe into individual ones based on rank (and position) | 
| remove_statistical_outliers.py	| removes statistical outlier rows from dataframe per player rank | 
| FindMoreUsers.py              	| main recursive function that calls to collect more accounts. This file is the next to be reworked which is why the naming convention is different | 

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Potential Future Adjustments
1. The way I collected new accounts separately from match data wasted lots of time as they were the same API request. In the future, I would implement this at the same time and maybe have a second dictionary where the keys are accounts and the values are a boolean telling me if their account was already accessed for this step of the API. Should save lots of time if I ever implement it for the other regions of the game (currently only have NA players).

2. Of course the model creation described in two sections up. Whether it one or several machine learning models or statistical tests, this still needs to be researched and implemented.

3. I recently learned about unit testing and test driven development, if I were to start again, I would do this. However, since it is already this far along, I may implement them at a later date.

4. The Seaborn package seems to have easier options when it comes to graphing data from a pandas dataframe. I may rework the graphs, but next time I would definitely use them in conjunction with matplotlib.

5. Of course this code isn't completely up to date with PEP8 standards, so I will continue to work on that.

--------------------------------------------------------------------------------------------------------------------------------------------------------------
