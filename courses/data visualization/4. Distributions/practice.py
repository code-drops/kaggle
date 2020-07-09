import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('Iris.csv',index_col=0)

# Histogram
sns.distplot(a=iris['PetalLengthCm'], kde=False)
plt.show()

# Density plots
sns.kdeplot(data=iris['PetalLengthCm'],shade=True)
plt.show()

# 2 KDE plots
sns.jointplot(x=iris['PetalLengthCm'],y=iris['SepalWidthCm'],kind='kde')
plt.show()

# Color coded histograms
sns.distplot(a=iris[iris['Species']=='Iris-setosa']['PetalLengthCm'], label="Iris-setosa", kde=False)
sns.distplot(a=iris[iris['Species']=='Iris-versicolor']['PetalLengthCm'], label="Iris-versicolor", kde=False)
sns.distplot(a=iris[iris['Species']=='Iris-virginica']['PetalLengthCm'], label="Iris-virginica", kde=False)
plt.legend()
plt.show()

# Color coded histograms
sns.kdeplot(iris[iris['Species']=='Iris-setosa']['PetalLengthCm'], label="Iris-setosa",shade=True)
sns.kdeplot(iris[iris['Species']=='Iris-versicolor']['PetalLengthCm'], label="Iris-versicolor",shade=True)
sns.kdeplot(iris[iris['Species']=='Iris-virginica']['PetalLengthCm'], label="Iris-virginica",shade=True)
plt.legend()
plt.show()