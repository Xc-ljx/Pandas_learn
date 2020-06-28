import pandas as pd
import sys,os
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame,read_csv
from numpy import random
"""
#准备数据
names = ['Bob','Jessica','Mary','John','Mel']
random.seed(500)
random_names = [names[random.randint(low=0,high=len(names))] for i in range(1000)] #生成1000个随机重复名字
births = [random.randint(low=0,high=1000)for i in range(1000)]
BabyDataSet = list(zip(random_names,births))
df = pd.DataFrame(data = BabyDataSet,columns=['Names','Births'])
df.to_csv('births1880.txt',index=False,header=False)
"""
#获取数据
Location = r'./births1880.txt'
df = pd.read_csv(Location,names=['Names','Births'])
#os.remove(Location)
#准备数据
name = df.groupby('Names')
df = name.sum()
#表现数据
df['Births'].plot.bar()
print("The most popular name")
print(df.sort_values(by='Births',ascending=False))
plt.show()

#print(df['Births'].max())
