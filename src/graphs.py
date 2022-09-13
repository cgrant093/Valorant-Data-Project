import pandas as pd
import seaborn as sns
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

def change_plot_color(fig, ax, color, background):
    ax.spines['bottom'].set_color(color)
    ax.spines['top'].set_color(color) 
    ax.spines['right'].set_color(color)
    ax.spines['left'].set_color(color)
    
    ax.tick_params(axis='x', colors=color)
    ax.tick_params(axis='y', colors=color)
    
    ax.yaxis.label.set_color(color)
    ax.xaxis.label.set_color(color)
    
    fig.patch.set_facecolor(background)
    ax.axes.set_facecolor(background)

    return fig, ax
    

def plot_rank_distribution(df, plot_path, keyword):
    fig = plt.figure(figsize=(9, 3.5))
    ax = fig.add_subplot()
    
    sns.histplot(data=df, x='Rank', hue='Rank', legend=None,
                 palette=sns.color_palette(color_order))
    
    plt.xticks(rank_order(), rotation=label_rot, size=label_size)
    plt.ylabel('Total players in a rank', size=label_size)
    plt.xlabel('Rank', size=label_size)
    plt.tight_layout()
    
    fig, ax = change_plot_color(fig, ax, 'white', 'black') 
    plt.savefig(f'{plot_path}{keyword}_dist_white.png')

    fig, ax = change_plot_color(fig, ax, 'black', 'white')
    plt.savefig(f'{plot_path}{keyword}_dist_black.png')
    
    plt.show()


def plot_avg_value(stat, df, plot_path, y_label):
    fig = plt.figure(figsize=(5, 3.5))
    ax = fig.add_subplot()
    
    sns.lineplot(data=df, x="Rank", y=stat,
                 marker='o', markersize=6, dashes=False,
                 err_style='bars', errorbar=(('sd', 1)) )
    
    plt.xticks(rank_order(), rotation=label_rot, size=label_size)
    plt.ylabel(y_label, size=label_size)
    plt.xlabel('Rank', size=label_size)
    plt.tight_layout() 
    
    fig, ax = change_plot_color(fig, ax, 'white', 'black') 
    plt.savefig(f'{plot_path}{stat}_rank_white.png')

    fig, ax = change_plot_color(fig, ax, 'black', 'white')
    plt.savefig(f'{plot_path}{stat}_rank_black.png')
    
    plt.show()


def plot_avg_value_per_position(stat, df, plot_path, y_label):
    fig = plt.figure(figsize=(5, 3.5))
    ax = fig.add_subplot()
    
    sns.color_palette('pastel')
    sns.lineplot(data=df, x="Rank", y=stat, hue='Position', 
                 style='Position', markers=True, markersize=6, 
                 dashes=False, err_style=None)
        
    plt.xticks(rank_order(), rotation=label_rot, size=label_size)
    plt.ylabel(y_label, size=label_size)
    plt.xlabel('Rank', size=label_size)
    plt.tight_layout()
    
    fig, ax = change_plot_color(fig, ax, 'white', 'black') 
    plt.savefig(f'{plot_path}{stat}_rank_pos_white.png')

    fig, ax = change_plot_color(fig, ax, 'black', 'white')
    plt.savefig(f'{plot_path}{stat}_rank_pos_black.png')
    
    plt.show()