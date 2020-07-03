# 1
'''create a DataFrame fruits'''
fruits = pd.DataFrame({'Apples':[30],'Bananas':[21]})

# 2
'''Create a dataframe fruit_sales'''
fruit_sales = pd.DataFrame({'Apples':[35,41],'Bananas':[21,34]},index=['2017 Sales','2018 Sales'])

# 3
'''Create a variable ingredients with a Series that looks like:

Flour     4 cups
Milk       1 cup
Eggs     2 large
Spam       1 can
Name: Dinner, dtype: object'''

ingredients = pd.Series(['4 cups','1 cup','2 large','1 can'],index=['Flour','Milk','Eggs','Spam'],name='Dinner')

# 4
'''Read the following csv dataset of wine reviews into a DataFrame called reviews:
The filepath to the csv file is ../input/wine-reviews/winemag-data_first150k.csv'''

reviews = pd.read_csv('../input/wine-reviews/winemag-data_first150k.csv',index_col=0)

# 5
'''Run the cell below to create and display a DataFrame called animals:'''
'''write code to save this DataFrame to disk as a csv file with the name cows_and_goats.csv'''
animals.to_csv('cows_and_goats.csv')