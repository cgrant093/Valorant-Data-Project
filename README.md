# Valorant Data Science Project

## What is Valorant?
Valorant is a 5v5 first-person tactile shooter game where the players choose different agents with unique abilities. It mixes together games like CS:GO and Overwatch.

Tactile shooter games are ones where there are unually two teams, one is attacking and one is defending. The attackers are trying to plant a bomb, or in Valorant's case a spike. There is limited time to plant the spike before the defenders win. Once a bomb has been planted, there is a limited amount of time for the defenders to defuse, otherwise the attackers take the win. If the spike is not planted and one team completely eliminates the other, that team wins. If the spike has been planted and the defenders eliminate the attacking team, they still have to defuse before the spike timer runs out. Valorant specifically is a first to 13 rounds, win by 2, and after 12 rounds, the teams switch sides. There is usually an 'economy' in which you save money over some number of rounds acquired through kills, spike plants/defuses, and winning/losing the round. You would use this money to buy better weapons (guns) and tools (abilities) to help you win the next round.

Games like Overwatch (or League of Legends) have teams of people where each team can choose one of each hero/agent/champion, etc. The agents each have a different set of abilites and you'd use these abilities in combination with your teammates to win the round. At higher levels, different team compositions (comps) are used to perform a different set of strategies and the team with the best strategy that game is more likely to win. 

In CS:GO anyone can purchase smokes (smoke bombs) or flashes (flash grenades) to help the team get in better positions and hide some of your movements. However, in Valorant, those plus many other abilities are tied to a specific agent, and this makes the roles on each team more clear for the players, specifically new users.

## Major problem in Valorant?
Valorant, like any other online game, has a cheating and smurfing problem. Cheating is when you utilized external software to help you perform better than you are, so you can achieve a better rank. Smurfing is essentially the opposite problem, you create new accounts and purposely play badly to have your rank set to a much lower level than the ability you can actually play at. You'd then play on teams and against teams with people much worse than you and effectively dominate every single game you play. Both of these can ruin the game for players who are trying to play fairly, and Valorant has anti-cheat software to help deal with the cheating problem.

## Can we do something about the smurfing problem?
This was my main question I wanted to answer. I wanted to do this by creating a model of accounts statistics (kill/death ratio, assists, headshot percentage, and ability usage) versus the rank and position you play on the team.

--------------------------------------------------------------------------------------------------------------------------------------------------------------

## Steps to creating my model
### 1. Acquire a large list of accounts with statistics
This process is currently being done. I am using the API created by https://github.com/Henrik-3 to get it done. However, it is not simple to create a large list of accounts. I have to use the API to generate the last 5 matches/games an account played, find the other accounts in those games, add them to my set if they aren't already there, and request their account statistics and their last 5 matches. My current depth is 2 on this, it takes many hours to perform, and I can only acquire about 9000 accounts. Going one more depth takes an exponetially longer amount of time. Maybe I'll run depth-2 every week or 2 and the list should grow from that.

### 2. Clean data and find average stats with uncertainty for each rank
I do have a problem where the data does have to be cleaned. If I am finding new accounts and have a tiny blimp of internet loss, I'll lose at least one accounts worth of data. I'll also need to find the outliers in each rank (potentially smurfs/cheaters) and cleans their data from the rank for the model.

### 3. Usings t-test to compare to given rank
I think using a couple t-tests (or z-tests) to compare the alleged smurf accounts average statistics to that of the clean data for their given rank. I am hoping the confidence level will be significant, and it may not be perfect, but I am hoping it gives a good starting spot.

--------------------------------------------------------------------------------------------------------------------------------------------------------------

## Potential issues/future adjustments
1. I and my friends have the occasional game where we do really well and games where we do poorly, so that's why I'm not comparing just their last game, but their average. 

2. Due to the API, I can only acquire the last 5 games for each account, which means their average statistics could be highly violatile. This could only be compensated for by saving everyone's information and updating it over time. I am not sure I have the space for this, and this would only work if I initially had a large number of user accounts that I didn't ever have to add to, those accounts consistantly played the game for years. However, if my 'seed' accounts continue to play, then getting a new set of 9000 accounts every couple weeks will hopefully keep all the average rank statistics pretty fair with the population that plays the game.

3. Currently, I only am including North American (NA) players. Different regions do not play with one another, and all my seed accounts are NA, and to find info for all the other accounts would take much longer as there's like 7-10 regions for Valorant.

