import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np
import sys
import matplotlib
import xlrd
import openpyxl
np.seed(111) #在相同数的约束下生成的随机数是一样的
def CreateDataSet(Number=1):
    Output = []
    for i in range(Number):
        #创建一个按周计算的日期范围（周一起始）
        rng = pd.date_range(start='1/1/2009',end='12/31/2012',freq='W-MON')
        #创建一些随机数
        data = np.randint(low=25,high=1000,size=len(rng))
        #状态池
        status = [1,2,3]
        #创建一个随机的状态列表
        random_status = [status[np.randint(low=0,high=len(status))]for i in range(len(rng))]
        #行政州的列表
        states = ['GA','FL','fl','NY','NJ','TX']
        #创建一个行政周的随机列表
        random_states = [states[np.randint(low=0,high=len(states))]for i in range(len(rng))]

        Output.extend(zip(random_states,random_status,data,rng))
    return Output

dataset = CreateDataSet(4)
df = pd.DataFrame(data=dataset,columns=['State','Status','CustomerCount','StatusDate'])
df.to_excel('Lesson3.xlsx',index=False)
print('Done!')
#从excel中获取数据
Location = r'./Lesson3.xlsx'
df = pd.read_excel(Location,sheet_name=0,index_col='StatusDate')
df['State'] = df.State.apply(lambda x:x.upper())
mask = df['Status'] == 1
df = df[mask]
mask = df.State == 'NJ'
df['State'][mask] = 'NY'
df['CustomerCount'].plot(figsize=(15,5));
sortdf = df[df['State']=='NY'].sort_index(axis=0)
Daily = df.reset_index().groupby(['State','StatusDate']).sum()
del Daily['Status']
#Daily.loc['FL'].plot()
#Daily.loc['GA'].plot()
#Daily.loc['NY'].plot()
#Daily.loc['TX'].plot()
#print(Daily.head())
#计算离群值
StateYearMonth = Daily.groupby([Daily.index.get_level_values(0),Daily.index.get_level_values(1).year,
                                Daily.index.get_level_values(1).month])
Daily['Lower'] = StateYearMonth['CustomerCount'].transform(lambda x:x.quantile(q=.25) - (1.5*x.quantile(q=.75)-x.quantile(q=.25)))
Daily['Upper'] = StateYearMonth['CustomerCount'].transform(lambda x:x.quantile(q=.75) + (1.5*x.quantile(q=.75)-x.quantile(q=.25)))
Daily['Outlier'] = (Daily['CustomerCount'] < Daily['Lower']) | (Daily['CustomerCount'] > Daily['Upper'])
Daily = Daily[Daily['Outlier'] == False]

ALL = pd.DataFrame(Daily['CustomerCount'].groupby(Daily.index.get_level_values(1)).sum())
ALL.columns = ['CustomerCount']
YearMonth = ALL.groupby([lambda x:x.year,lambda x:x.month])
ALL['MAX'] = YearMonth['CustomerCount'].transform(lambda x:x.max())

#创建BHAG数据
data = [1000,2000,3000]
idx = pd.date_range(start='12/31/2011',end='12/21/2013',freq='A')
BHAG = pd.DataFrame(data,index=idx,columns=['BHAG'])
combined = pd.concat([ALL,BHAG],axis=0)
combined = combined.sort_index(axis=0)
fig,axes = plt.subplots(figsize=(12,7))
combined['BHAG'].fillna(method='pad').plot(color='green',label='BHAG')
combined['MAX'].plot(color='blue',label='All Markets')
plt.legend(loc='best')
plt.show()

