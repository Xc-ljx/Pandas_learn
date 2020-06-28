import pandas as pd
import sys,os
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame,read_csv
from numpy import random

"""
print("Python version "+sys.version)
print("Pandas version "+pd.__version__)
print("Matplotlib version "+matplotlib.__version__)
"""

#数据创建
names = ['Bob','Jessica','Mary','John','Mel']
births = [968,155,77,578,973]
BabyDataSet = list(zip(names,births))
df = pd.DataFrame(data = BabyDataSet,columns=['Names','Births'])
df.to_csv('births1880.csv',index=False,header=False)

#获取数据
Location = r'./births1880.csv'
df = pd.read_csv(Location,names=['Names','Births'])
os.remove(Location)

#准备数据,即查看数据类型是否符合要求
#分析数据
Sorted = df.sort_values(['Births'],ascending=False)
Sorted.head(1);
df['Births'].max()

#表现数据
df['Births'].plot.bar()
MaxValue = df['Births'].max()
MaxName = df['Names'][df['Births'] == df['Births'].max()].values
Text = str(MaxValue)+"-"+MaxName
plt.annotate(Text,xy=(1,MaxValue),xytext=(8,0),xycoords=('axes fraction','data'),textcoords='offset points')
print("The most popular name")
df[df['Births'] == df['Births'].max()]
