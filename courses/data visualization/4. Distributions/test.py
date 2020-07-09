import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# 1
'''Paths of the files to read'''
cancer_b_filepath = "../input/cancer_b.csv"
cancer_m_filepath = "../input/cancer_m.csv"

'''Fill in the line below to read the (benign) file into a variable cancer_b_data'''
cancer_b_data = pd.read_csv(cancer_b_filepath,index_col='Id')

'''Fill in the line below to read the (malignant) file into a variable cancer_m_data'''
cancer_m_data = pd.read_csv(cancer_m_filepath,index_col='Id')

# 2
'''Use a Python command to print the first 5 rows of the data'''
cancer_b_data.head()
cancer_m_data.head()

'''Fill in the line below: In the first five rows of the data for benign tumors, what is the largest value for 'Perimeter (mean)'?'''
max_perim = max(cancer_b_data.head(5)['Perimeter (mean)'])

'''Fill in the line below: What is the value for 'Radius (mean)' for the tumor with Id 842517?'''
mean_radius = cancer_m_data['Radius (mean)'][842517]

# 3
'''Use the code cell below to create two histograms that show the distribution in values for 'Area (mean)' for both benign and malignant tumors.'''
sns.distplot(a=cancer_b_data['Area (mean)'],kde=False,label='benign') # Your code here (benign tumors)
sns.distplot(a=cancer_m_data['Area (mean)'],kde=False,label='maligant') # Your code here (malignant tumors)
plt.legend()

# 4
'''Use the code cell below to create two KDE plots that show the distribution in values for 'Radius (worst)' for both benign and malignant tumors.'''
sns.kdeplot(data=cancer_b_data['Radius (worst)'],shade=True,label='benign') # Your code here (benign tumors)
sns.kdeplot(data=cancer_m_data['Radius (worst)'],shade=True,label='maligant') # Your code here (malignant tumors)
plt.legend()