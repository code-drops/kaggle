import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1
''' load the dataset'''
museum_data = pd.read_csv('museum.csv',index_col=0,parse_dates=True)

# 2
'''print last five rows of dataset'''
print(museum_data.tail())

''' Fill in the line below: How many visitors did the Chinese American Museum receive in July 2018?'''
ca_museum_jul18 = museum_data['Chinese American Museum']['2018-07-01']

''' Fill in the line below: In October 2018, how many more visitors did Avila Adobe receive than the Firehouse Museum?'''
avila_oct18 = museum_data['Avila Adobe']['2018-10-01']-museum_data['Firehouse Museum']['2018-10-01']

# 3
'''Line chart showing the number of visitors to each museum over time'''
sns.lineplot(data=museum_data)

# 4
'''Line plot showing the number of visitors to Avila Adobe over time'''
sns.lineplot(data=museum_data['Avila Adobe'])

