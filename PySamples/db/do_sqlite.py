#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db

def show_tables():
    try:
        sql_db = sqlite3.connect('test.db')
        # 创建一个Cursor:
        cursor = sql_db.cursor()
        cursor.execute("select name from sqlite_master where type='table' order by name")
        cursor.fetchall()
        # 关闭Cursor:
        cursor.close()
        # 提交事务:
        sql_db.commit()
        # 关闭Connection:
        sql_db.close()
    except sqlite3.Error as err:
        print(err)


def update_user_table():
    # 如果文件不存在，会自动在当前目录创建:
    sql_db = sqlite3.connect('test.db')
    # 创建一个Cursor:
    cursor = sql_db.cursor()
    # 执行一条SQL语句，创建user表:
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    # 继续执行一条SQL语句，插入一条记录:
    cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
    # 通过rowcount获得插入的行数:
    print('rowcount =', cursor.rowcount)
    # 关闭Cursor:
    cursor.close()
    # 提交事务:
    sql_db.commit()
    # 关闭Connection:
    sql_db.close()


show_tables()
# update_user_table()



# 查询记录：
sql_db = sqlite3.connect('test.db')
cursor = sql_db.cursor()
# 执行查询语句:
cursor.execute('select * from user where id=?', '1')
# 获得查询结果集:
values = cursor.fetchall()
print(values)
cursor.close()
sql_db.close()
