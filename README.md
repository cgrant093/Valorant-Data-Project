### **Players are prematurely leaving Valorant due to the other players abusing the match-making algorithm, which is losing Riot money!**

Woah... woah... woah... let's step back for a moment. What's Valorant? What's Riot? What's going on?

## What is Valorant/Riot?
Riot's Valorant is a free-to-play online video game where two teams compete in a strategic competition of map control and team elimination.
The match-making algorithm is set to have you compete with/against players that are approximately your skill level.
A player's skill-level can be determined with two generic traits: 

1. better mechanical ability (presses buttons faster, more precisemouse movements, etc.) 
2. smarter game sense/strategy (why/how to take map control, when/how to use abilities, crosshair placement, etc.)

Now, I have used some jargon in the parentheses above, but we'll ignore them for now.

## How are some players are abusing match-making?
There are two ways some players abuse match-making: either by cheating or smurfing. 

Cheating is using external software to artificially raise their mechanical skill. There are 'ranks' in the game, and a higher rank holds more prestige, which is something some players deeply care about. To increase your rank, you need to win games, and some people do this by using external software to help them win. However, I am not here to fix this issue. Riot uses anti-cheat software, and it improves with every patch to the game. I am here to see if it's possible to fix the smurfing issue.

Smurfing is when a good player makes a new account, and match-making will queue them with players significantly worse than them (or new at the game). This doesn't use external software, so it's harder to detect with a program. This can be discouraging and not fun for the new or lower skilled players, and if they run into it enough they will permanently quit the game.

## Where is Riot losing money?
Valorant is free-to-play. They get their money from players making in-game purchases of new skins/cosmetics, new characters to play, or the battle-pass. The longer someone plays the game, the more likely they are to make these purchases. If new or low skilled players are quitting the game prematurely due to smurfs, then Riot is losing money due to smurfs.

## Can we do something about the smurfing problem?
Due to the complexity of the game, there are many in-game statistics that are measured and relate to a person's mechanical ability and some imply their game sense. I want to see how these statistics change based a player's rank. Can statistical outliers and machine learning catch a smurfing player?

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Current Progress


## A. Acquire a large list of accounts and account statistics
Aside from leaderboards found on websites, like [tracker.gg](https://tracker.gg/valorant/leaderboards/ranked/all/default?page=1), there is no player list in Valorant. The leaderboard found on [tracker.gg](https://tracker.gg/valorant/leaderboards/ranked/all/default?page=1) only has the top 1000 accounts or so in any given region. This of course would be a biased dataset if I only used these accounts as it would only give me statistics about the upper ranks. With the help of an [API](https://github.com/Henrik-3/unofficial-valorant-api) by Henrik-3, I wrote a recursive program that collects accounts from small list of players. It would look at their past few games played and collect all the accounts they played with. These accounts would be added to a set, and I did this until I acquired ~100k accounts. 

Afterwards, I sent another [API](https://github.com/Henrik-3/unofficial-valorant-api) to the whole list of accounts and found all relevant data for their last couple of matches. If I were to do this again, I would probably do them in the same step, and/or add the accounts as keys to a dictionary where the value is a boolean that tells me if their account statistics has been added to the pandas dataframe yet.


## B. Restructuring and cleaning the data

First, the data needs to be restructured. For the API requests to run as fast as possible, I collected all game data for X number of games from a player and moved on. However, there is a lot of game data that I didn't think was necessary for my project. So this column in the dataframe was 'exploded' to multiple rows for users with multiple games saved, and expanded to multiple columns for the in-game statistics that I thought necessary for the project. I am having trouble in step D, so I may need to collect new features, and I may redo this step utilizing PostgreSQL because I think with the addition of some reference tables, I can extract the data better than I can in Pandas.

Aside from removing missing data, another aspect to cleaning the data needed to be performed: removing statistical outliers. This is done per rank, and was done using the simple IQR definition of 'outlier data'. An interesting notion here is the accounts removed here are potential smurfs/cheaters. However, they can also be players who have come back to the game after a long hiatus and in that time have somehow gotten better/worse at the game.

After cleaning the data, I was left with this distribution of account ranks:

![my rank distribution](./plots/clean_dist_black.png#gh-dark-mode-only)
![my rank distribution](./plots/clean_dist_white.png#gh-light-mode-only)

Which is very similar to the bar chart found on [tracker.gg](https://tracker.gg/valorant/leaderboards/ranked/all/default?page=1). Although, I have not written a statistical test to check how similar the two distributions are, and will potentially implement this in the future.


## C. Finding the significant features

I plotted each in-game statistics per rank to find the signficant features. The features labels are in video game jargon and there isn't much I can do about that. Labeling the features without video game jargon would make the project's code less readable to me and more confusing to the people that understand Valorant.

The features I have currently chose to match mechanical ability and game sense to a player's rank are:

![KD rank](./plots/KD_rank_black.png#gh-dark-mode-only) ![HS perc rank](./plots/HS_perc_rank_black.png#gh-dark-mode-only)
![KD rank](./plots/KD_rank_white.png#gh-light-mode-only) ![HS perc rank](./plots/HS_perc_rank_white.png#gh-light-mode-only)
![avg Ability Usage_rank](./plots/avg_ability_usage_rank_black.png#gh-dark-mode-only) ![Avg Dam Rec_rank](./plots/avg_dmg_rec_rank_black.png#gh-dark-mode-only)
![avg Ability Usage_rank](./plots/avg_ability_usage_rank_white.png#gh-light-mode-only) ![Avg Dam Rec_rank](./plots/avg_dmg_rec_rank_white.png#gh-light-mode-only)
![Avg econ spent](./plots/avg_spent_rank_black.png#gh-dark-mode-only) ![Avg econ loadout](./plots/avg_loadout_rank_black.png#gh-dark-mode-only)
![Avg econ spent](./plots/avg_spent_rank_white.png#gh-light-mode-only) ![Avg econ loadout](./plots/avg_loadout_rank_white.png#gh-light-mode-only)
![Account level](./plots/level_rank_black.png#gh-dark-mode-only) ![Avg assists](./plots/avg_assists_rank_black.png#gh-dark-mode-only)
![Account level](./plots/level_rank_white.png#gh-light-mode-only) ![Avg assists](./plots/avg_assists_rank_white.png#gh-light-mode-only)

I found that some other features I originally chose had nearly the same plot as the KD plot, and it makes sense that this is the case because they are highly related to KD. I decided to not include them to try to have non-repeated normalized features in the model. 

Also, in terms of rank, a player can also have a particular 'position' on the team. When choosing a character, they have different abilities (or super powers) and these abilities have different uses. Valorant has divided up the characters into four main groups depending on their set of abilities. 

I also wanted to look at the statistics based on rank and position. However, I found that other than the Average Assists plot, the plots for each stat based position (and rank) largely follow the same curve as the one only based on rank, and different characters a player chooses seems to have a negligable outcome on their rank. For instance,

![KD rank pos](./plots/KD_rank_pos_black.png#gh-dark-mode-only) ![HS perc rank pos](./plots/HS_perc_rank_pos_black.png#gh-dark-mode-only)
![KD_rank pos](./plots/KD_rank_pos_white.png#gh-light-mode-only) ![HS perc rank pos](./plots/HS_perc_rank_pos_white.png#gh-light-mode-only)

We can see for some features, it's closely the same plot, and for others, like headshot percentage is the exact same plot.


## D. Preprocess data and creating a classification model
Preprocessed data:
1. Normalized the features
2. Encoded the labels
3. Split data into 80% training and 20% testing

My first attempt at a classification model was the built in KNN from sklearn. I found that it has a very poor accuracy. I tried various neighbor values ranging from 3 to 1001, and the best accuracy found was 11%.

To improve the poor performance, a few ideas I had were:
1. Some of the features aren't great and/or have a logrithmic plot vs rank. For instance, average assists doesn't look very helpful due to its unique shape. When looking at the plots above, any logrithmic feature can't differentiate 2/3s of the player base and is not something I should use. So I either need to eliminate some current features, or add some others I didn't originally think about.
2. My model needs to change. Maybe a Random Forest or another classifier is a better choice? Maybe I need to implement a deep learning framework with PyTorch with a more customizable cost functions? Maybe a statistical test is a better way to go?
3. My dataset could be a poor one. There's a chance there isn't enough variability between a rank and the +/-2- ranks surrounding it. Perhaps I can even try implementing more loose cost function?
4. Perhaps I need to split off a validation data set to improve my very simple training algorithm with that with methods like early stopping, etc.


## E: Predicting an account's rank
This will have ~3 steps:
1. If someone does not have a rank, then send them to the classification model.
2. If someone does have a rank, use a t-test/ANOVA to confirm they are in the correct rank. If not, send them to the classification model.
3. Run the classification model to determine their rank.
   

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
| preprocessing.py	| normalizes features, encodes labels, and splits the dataset into multiple parts | 
| FindMoreUsers.py              	| main recursive function that calls to collect more accounts. This file is the next to be reworked which is why the naming convention is different | 

--------------------------------------------------------------------------------------------------------------------------------------------------------------

# Potential Future Adjustments
1. When collecting more accounts: don't use a recursive technique. Instead, use a dictionary where the keys are currently collected accounts, and the value is a boolean stating whether match data has been collected. Match data has other players in it, no reason to run this API request twice for each person.

2. When restructuring data, use a SQL database instead with custom reference tables, so it's easier to collect other features in the future.

3. Perhaps I need to run a statistical test to see if my account distribution matches that of the total account distribution on [tracker.gg](https://tracker.gg/valorant/leaderboards/ranked/all/default?page=1). However, this seems like a lot of work for something that is potentially unimportant.

4. The machine learning model needs to be reworked, or the selected features need to be readjusted. Instead of KNN, I need to try a Random Forest. Other ideas are using some kind of statistical test instead, or implement a deep learning neural net in PyTorch. Another thing is I've divided up the category by rank, which makes it a classification problem. However, your MMR is more continuous, and each rank is associated with an MMR range, so I could turn it into a regression problem if I have the players' MMR instead of rank.

5. I recently learned about unit testing and test driven development, if I were to start again, I would do this. However, since it is already this far along, I have to ignore TDD and try implementing unit testing on my previous functions.

6. The Seaborn package seems to be easier at implementing some options when graphing data. I may rework the graphs, but next time I would definitely use them in conjunction with matplotlib.

7. Of course this code isn't completely up to date with PEP8 standards, so I will continue to work on that.

8. Currently, I only have accounts from the NA region, but perhaps once it is done, it can be expanded to the other geographical regions.

--------------------------------------------------------------------------------------------------------------------------------------------------------------
