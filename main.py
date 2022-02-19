import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas_profiling as pp
import matplotlib
matplotlib.use('tkagg')
#Load the dataset
data=pd.read_csv('SampleSuperstore.csv')

#Data exploration
print(data.info)
print(data.describe())
report=pp.ProfileReport(data)
report.to_file('output.html')
#Data Cleaning
print(data.duplicated().sum())
print(data.drop_duplicates(inplace=True))
print(data.duplicated().sum())
print(data.isnull().sum())
data.corr().style.background_gradient(cmap='green')
data.boxplot()
plt.show()