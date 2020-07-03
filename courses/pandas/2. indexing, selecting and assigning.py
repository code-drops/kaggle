# reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

#1
'''Select the description column from reviews and assign the result to the variable desc.'''
desc = reviews['description']
type(desc)

# 2
'''Select the first value from the description column of reviews, assigning it to variable first_description.'''
first_description = desc[0]

# 3
'''Select the first row of data (the first record) from reviews, assigning it to the variable first_row.'''
first_row = reviews.iloc[0]

# 4
'''Select the first 10 values from the description column in reviews, assigning the result to variable first_descriptions.'''
first_descriptions = reviews['description'][0:10]

# 5
'''Select the records with index labels 1, 2, 3, 5, and 8, assigning the result to the variable sample_reviews.'''
sample_reviews = reviews.iloc[[1,2,3,5,8]]

# 6
'''Create a variable df containing the country, province, region_1, and region_2 columns of the records with the index labels 0, 1, 10, and 100. In other words, generate the following DataFrame:'''
df = reviews[["country","province","region_1","region_2"]].iloc[[0,1,10,100]]

# 7
'''Create a variable df containing the country and variety columns of the first 100 records.'''
df = reviews.loc[0:99,['country','variety']]

# 8
'''Create a DataFrame italian_wines containing reviews of wines made in Italy.'''
italian_wines = reviews[reviews['country']=='Italy']

# 9
'''Create a DataFrame top_oceania_wines containing all reviews with at least 95 points (out of 100) for wines from Australia or New Zealand.'''
top_oceania_wines = reviews[(reviews['points']>=95) & ((reviews['country']=='Australia') | (reviews['country']=='New Zealand'))]