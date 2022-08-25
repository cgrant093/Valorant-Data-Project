import pandas as pd
import matplotlib.pyplot as plt

def rank_order():   
    return [
        'Iron 1', 'Iron 2', 'Iron 3', 
        'Bronze 1', 'Bronze 2', 'Bronze 3',
        'Silver 1', 'Silver 2', 'Silver 3',
        'Gold 1', 'Gold 2', 'Gold 3',
        'Platinum 1', 'Platinum 2', 'Platinum 3',
        'Diamond 1', 'Diamond 2', 'Diamond 3',
        'Ascendant 1', 'Ascendant 2', 'Ascendant 3',
        'Immortal 1', 'Immortal 2', 'Immortal 3',
        'Radiant'
    ]

color_order = [
    '#5d5d5d', '#5d5d5d', '#5d5d5d', 
    '#966c18', '#966c18', '#966c18',
    '#e1e8e7', '#e1e8e7', '#e1e8e7',
    '#e9c44c', '#e9c44c', '#e9c44c',
    '#52d5de', '#52d5de', '#52d5de',
    '#f197f4', '#f197f4', '#f197f4',
    '#3cb57b', '#3cb57b', '#3cb57b',
    '#b02638', '#b02638', '#b02638',
    '#ffffb5'
]

label_rot = 75
label_size = 8

def change_plot_color(fig, color):
    fig.spines['bottom'].set_color(color)
    fig.spines['top'].set_color(color) 
    fig.spines['right'].set_color(color)
    fig.spines['left'].set_color(color)
    
    fig.tick_params(axis='x', colors=color)
    fig.tick_params(axis='y', colors=color)
    
    fig.yaxis.label.set_color(color)
    fig.xaxis.label.set_color(color)

    return fig


def plot_rank_distribution(df, data_path, plot_path, keyword):
    df['count'] = 1
    
    groupby_ranked = df.groupby(['Rank']).count()['count']
    groupby_ranked = groupby_ranked.reindex(rank_order())
    data = zip(rank_order(), groupby_ranked)

    groupby_ranked_df = pd.DataFrame(data, columns=['Rank', 'count'])
    groupby_ranked_df.to_csv(f'{data_path}{keyword}_dist.csv', index=False)
    
    fig = plt.figure().add_subplot()
    
    plt.bar(rank_order(), groupby_ranked, color=color_order)
    plt.xticks(rank_order(), rotation=label_rot, size=label_size)
    plt.ylabel('Total players in a rank')
    plt.xlabel('Rank')
    plt.tight_layout()
    
    fig = change_plot_color(fig, 'white') 
    plt.savefig(f'{plot_path}{keyword}_dist_white.png')

    fig = change_plot_color(fig, 'black')
    plt.savefig(f'{plot_path}{keyword}_dist_black.png')
    
    plt.show()


def plot_avg_value(stat, group, y, plot_path):
    x = rank_order()

    fig = plt.figure().add_subplot()
    
    plt.errorbar(x, y['mean'][stat], y['sem'][stat], fmt='go-', 
                 ecolor='g', lw=2, capsize=2, capthick=2)

    plt.xticks(rank_order(), rotation=label_rot, size=label_size)
    plt.ylabel(f'Avg {stat} per {group}')
    plt.xlabel('Rank')
    plt.tight_layout() 
    
    fig = change_plot_color(fig, 'white') 
    plt.savefig(f'{plot_path}{stat}_rank_white.png')

    fig = change_plot_color(fig, 'black')
    plt.savefig(f'{plot_path}{stat}_rank_black.png')
    
    plt.show()


def plot_avg_value_per_position(stat, group, y, plot_path):
    x = rank_order()
    
    colors = ['g', 'b', 'r', 'm', 'k']
    position_list = ['Duelist', 'Initiator', 'Sentinel', 'Controller']
    i = 0
    
    fig = plt.figure().add_subplot()
    
    for position in y:
        plt.errorbar(x, y[position]['mean'][stat], y[position]['sem'][stat], 
                     fmt=f'{colors[i]}o-', ecolor=colors[i], 
                     lw=2, capsize=2, capthick=2)
        i += 1
        
    plt.legend(position_list, loc=2)
    plt.xticks(rank_order(), rotation=label_rot, size=label_size)
    plt.ylabel(f'Avg {stat} per {group}')
    plt.xlabel(group)
    plt.tight_layout()
    
    fig = change_plot_color(fig, 'white') 
    plt.savefig(f'{plot_path}{stat}_rank_pos_white.png')

    fig = change_plot_color(fig, 'black')
    plt.savefig(f'{plot_path}{stat}_rank_pos_black.png')
    
    plt.show()