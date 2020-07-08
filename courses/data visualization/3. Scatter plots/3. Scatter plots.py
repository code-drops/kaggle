import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1
'''Read the candy data file into candy_data. Use the "id" column to label the rows.'''
candy_filepath = "../input/candy.csv"
candy_data = pd.read_csv(candy_filepath,index_col='id')

# 2
'''Print the first five rows of the data'''
print(candy_data.head())

'''Which candy was more popular with survey respondents: '3 Musketeers' or 'Almond Joy'?'''
more_popular = '3 Musketeers' if candy_data['winpercent'][1]>candy_data['winpercent'][3] else 'Almond Joy'

'''Which candy has higher sugar content: 'Air Heads' or 'Baby Ruth'?'''
more_sugar = 'Air Heads' if candy_data['sugarpercent'][2]>candy_data['sugarpercent'][4] else 'Baby Ruth'

# 3
'''Do people tend to prefer candies with higher sugar content?'''
'''Scatter plot showing the relationship between 'sugarpercent' and 'winpercent' '''
sns.scatterplot(x=candy_data['sugarpercent'],y=candy_data['winpercent'])

# 4
''' Scatter plot w/ regression line showing the relationship between 'sugarpercent' and 'winpercent' '''
sns.regplot(x=candy_data['sugarpercent'],y=candy_data['winpercent'])

# 5
''' # Scatter plot showing the relationship between 'pricepercent', 'winpercent', and 'chocolate' '''
sns.scatterplot(x=candy_data['sugarpercent'],y=candy_data['winpercent'],hue=candy_data['chocolate'])

# 6
''' Create the same scatter plot you created in Step 5, but now with two regression lines, corresponding to (1) chocolate candies and (2) candies without chocolate. '''
sns.lmplot(x="sugarpercent", y="winpercent", hue="chocolate", data=candy_data)

# 7
''' Create a categorical scatter plot to highlight the relationship between 'chocolate' and 'winpercent'. Put 'chocolate' on the (horizontal) x-axis, and 'winpercent' on the (vertical) y-axis. '''
sns.swarmplot(x=candy_data['chocolate'],y=candy_data['winpercent'])