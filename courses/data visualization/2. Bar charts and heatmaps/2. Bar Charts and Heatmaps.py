'''You're interested in using IGN reviews to guide the design of your upcoming game. Thankfully, someone has summarized the rankings in a really useful CSV file that you can use to guide your analysis.'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1
''' load the data '''
ign_filepath = "../input/ign_scores.csv"
ign_data = pd.read_csv(ign_filepath,index_col='Platform')

# 2
'''Print the data'''
print(ign_data)

''' What is the highest average score received by PC games, for any platform?'''
high_score = max(ign_data.loc['PC'])

'''On the Playstation Vita platform, which genre has the lowest average score? Please provide the name of the column, and put your answer in single quotes (e.g., 'Action', 'Adventure', 'Fighting', etc.)'''
worst = 10
for genre in ign_data.columns:
    if ign_data[genre]['PlayStation Vita']<worst:
        worst = ign_data[genre]['PlayStation Vita']
        g = genre
print(g)

# 3
'''Bar chart showing average score for racing games by platform'''
sns.barplot(x=ign_data.index,y=ign_data['Racing'])

# 4
'''# Heatmap showing average game score by platform and genre'''
sns.heatmap(data=ign_data,annot=True)

