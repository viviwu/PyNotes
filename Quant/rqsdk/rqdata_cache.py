# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         rqdata_sql
# Description:
# Author:       Administrator
# Date:         2021/4/24
# desc: Copyright © Administrator All rights reserved.
# -------------------------------------------------------------------------------

import sys
import rqdatac, pandas, datetime
import sqlite3

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print("https://www.ricequant.com/doc/rqdata/python/")
    rqdatac.init()
    # 获取用户当前登录版本、服务器信息
    rqdatac.info()
    # 获取用户配额信息
    print(rqdatac.user.get_quota())

def cache_index_components_price_data():
    rqdatac.init()
    order_book_id = "000300.XSHG"  # 000016.XSHG 上证50
    list = rqdatac.index_components(order_book_id, date='2021-06-01')
    for symbol in list:
        df = rqdatac.get_price(symbol, start_date=20150101, end_date="2021-06-01")
        #  rqdatac.get_price('000002.XSHE', start_date=pandas.Timestamp("20150101"), end_date=datetime.datetime(2015, 2, 1))

        cond = 0
        if cond == 0:
            conn = sqlite3.connect("cache/components.db")
            # cur = conn.cursor();
            df.to_sql(symbol, con=conn, if_exists='append', index=True)
            conn.close()
        elif cond == 1:
            df.to_csv("cache/" + symbol + ".csv")
        else:
            return


def read_sqlite_db():
    with sqlite3.connect("cache/quot.sqlite") as conn:
        # cur = conn.cursor()
        # 提取整个表packs，存到dataframe中
        # sql_cmd = "select * from tb_000001"
        # sql_cmd = "select * from tb_000001 where low=9.9857"
        sql_cmd = "select * from tb_000001 where date=\"2015-01-06 00:00:00\""
        df = pandas.read_sql(sql_cmd, con=conn)
        print(df.shape, df.dtypes, df.head())


def exec_sqlite_db():
    with sqlite3.connect("cache/quot.sqlite") as conn:
        cur = conn.cursor()
        sql_cmd = "select * from tb_000001"
        dt = cur.execute(sql_cmd)
        df = pandas.DataFrame(data=dt)
        # 表的大小 数据类型  前几行数据
        # print(df.shape, df.dtypes, df.head())
        print(df)
        cur.close()
        conn.close()


def cache_rqdata_daily_data():
    rqdatac.init()
    list = []
    cond = 1
    if 0 == cond :
        df = rqdatac.all_instruments(type='CS', market='cn', date='2021-06-01')
        list = df.order_book_id.to_list()
    else :
        # index
        list = ['000016.XSHG', '000300.XSHG', '000001.XSHG', '000905.XSHG', '399001.XSHE']

    conn = sqlite3.connect("cache/daily.db")
    # cur = conn.cursor();
    for symbol in list:
        print(symbol)
        df = rqdatac.get_price(symbol, start_date=20150101, end_date="2021-06-01")
        df.to_sql(symbol, con=conn, if_exists='append', index=True)
    conn.commit()
    conn.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('MyRqData')
    # rqdata_api_demo()
    # exec_sqlite_db()
    # read_sqlite_db()

    cache_rqdata_daily_data()
