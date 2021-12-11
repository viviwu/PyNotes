# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         do_pandas
# Description:
# Author:       Administrator
# Date:         2021/12/9
# desc: Copyright © Administrator All rights reserved.
# -------------------------------------------------------------------------------

import sys
import numpy as np
import pandas as pd

dt = np.arange(5,10)
series = pd.Series(data=dt, index=['a','b','c','d','e'])
print(series)

arr2d = np.random.random((3,4))
df = pd.DataFrame(data=arr2d, columns=['a','b','c','d'], index=['r0','r1','r2'])
print(df)

# key/value
def pd_series():
    method = 1
    if  method == 0:
        values = ['Apple', 'Google', 'Meta', '百度']
        idx = ['A', 'B', 'C', 'D']
        series = pd.Series(data=values, index=idx)
    else:
        dict = {1: 'Apple', 2: 'Google', 3: 'Meta', 4: '百度'}
        series = pd.Series(data=dict)

    print(series)
    print(series.values, series.index)
    print(series.to_json())

def pd_dataframe():
    method = 0
    if method == 0:
        # dt = [[1,2,3],[4,5,6],[7,8,9]]
        dt = np.random.rand(4, 3)  # numpy.ndarray
        df = pd.DataFrame(data=dt, columns=['A', 'B', 'C'], dtype=float)
    elif method == 1:
        dt = {'A':[1,2,3], 'B':[4,5,6], 'C':[7,8,9]}
        df= pd.DataFrame(data=dt)
    elif method == 2:
        dt = [{'A':1,'B':2,'C':3}, {'A':4,'B':5,'C':6}, {'A':7,'B':8,'C':9}]
        df = pd.DataFrame(data=dt)
    elif method == 3:
        df = pd.read_csv('test.csv')
    elif method == 4:
        df = pd.read_excel('test.xlsx')
    else:
        df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
    '''
   A  B  C
0  1  2  3
1  4  5  6
2  7  8  9
    '''
    print(df)
    df.to_csv('test.csv')

    '''
    # render dataframe as excel
    writer = pd.ExcelWriter('test.xlsx')
    df.to_excel(writer)
    writer.save()
    '''

    print(df.to_dict(orient='records'))     #list[dict{k:v},dict{k:v}]
    print(df.to_dict(orient='index'))
    print(df.columns.tolist())
    print(df.index.tolist())

    # slice by row id(index)
    # print(df.loc[1].to_dict())    #Series
    # print(df.loc[[0,1]].to_dict())  #Dataframe
    # print(df.loc[[0, 1][0]])  #Series

    # slice by column name
    # print(type(df['A']), df['A'], df.A)
    print(df[['A','C']])


def clean_data():
    dt = [[0,1,2,3],[4,5,6],[7,8,9,5],[4,0,None,2]]
    df = pd.DataFrame(dt, columns=['a','b','c','d'])
    print(df)
    print(df.isnull())  # False/True
    # print(df.duplicated())

    # 去掉空行
    # print(df.dropna(inplace=False))
    # print(df.dropna(subset=['d'], inplace=False))

    # 修补空缺的值
    x = df["d"].median()    # 取平均值
    x = df["d"].mode()      # 取众数
    x = df["d"].median()    # 取中位数
    print(df.fillna(x))

    # 替换错误数据
    df.loc[0, 'a'] = 99
    print(df)

    for x in df.index :
        if df.loc[x,'b']<10 :
            df.loc[x,'b'] = 123
    print(df)


def df_fromat_date():
    # 第三个日期格式错误
    data = {
        "Date": ['2020/12/01', '2020/12/02', '20201226'],
        "duration": [50, 40, 45]
    }

    df = pd.DataFrame(data, index=["day1", "day2", "day3"])
    print(df)

    df['Date'] = pd.to_datetime(df['Date'])
    print(df)


def do_series_map():
    series1 = series.map(lambda x: '%.3f'%x)
    series2 = series.apply(lambda x: '%.2f' % x)
    print(series1)
    print(series2)


def do_dataframe_apply_map():

    print(df['a'].map(lambda x:x*10))  # series map
    print(df['a'].apply(lambda x:x*10)) # series apply

    # apply()将一个函数作用于DataFrame中的行或列
    fn = lambda x:x.max()-x.min()
    fn = lambda x:x.mean()
    print(df.apply(fn))

    # applymap() 则作用于DataFrame中的每一个元素
    fn = lambda x:x*1000
    print(df.applymap(fn))


def slice_dataframe():
    print(df['a'])
    print(df.d)
    print(df[['b', 'c']])

    print(df.loc['r0'])
    print(df.loc[['r1', 'r2']])

    '''
    orient : str {'dict', 'list', 'series', 'split', 'records', 'index'}
                Determines the type of the values of the dictionary.

                - 'dict' (default) : dict like {column -> {index -> value}}
                - 'list' : dict like {column -> [values]}
                - 'series' : dict like {column -> Series(values)}
                - 'split' : dict like
                  {'index' -> [index], 'columns' -> [columns], 'data' -> [values]}
                - 'records' : list like
                  [{column -> value}, ... , {column -> value}]
                - 'index' : dict like {index -> {column -> value}}
    '''
    print(df.to_dict(orient='records'))        # list[{dict, dict}]
    print(df.to_dict(orient='index'))


def dataframe_append_concat():

    cond = 0
    if  cond == 0:
        df2 = pd.DataFrame(data=np.random.random((2, 5)), columns=['a', 'b', 'c', 'd','e'], index=['r3', 'r4'])
        print(df2)
        # new_df = df.append(df2)
        new_df = pd.concat([df,df2], axis=0, sort=False)      # 横向合并
        print(new_df)
    else:
        df3 = pd.DataFrame(data=np.random.random((3, 2)), columns=['e','f'], index=['r0','r1','r3'])
        print(df3)

        new_df = pd.concat([df, df3], axis=1, sort=False)       # 纵向合并
        print(new_df)


def nested_dataframe():
    df1 = pd.DataFrame(data={'col0': [1, 2], 'col2': [3, 9]})
    df2 = pd.DataFrame(data={'col0': [3, 4], 'col2': [7, 9]})
    df3 = pd.DataFrame(data={'col0': [3, 5], 'col2': [7, 6]})
    # data = {'Site':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12, 13]}
    data = {'Site': [df1, df2, df3], 'Age': [10, 12, 13]}
    df = pd.DataFrame(data)
    print(df)

# pd_series()
# pd_dataframe()
# clean_data()
# df_fromat_date()
# do_series_map()
# do_dataframe_apply_map()
# slice_dataframe()
dataframe_append_concat()
# xdf = xdf.drop('datetime', axis=1, inplace=False)
# nested_dataframe()