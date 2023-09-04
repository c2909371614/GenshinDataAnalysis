import numpy as np
import pymysql #引入pymssql模块
# from collections.abc import Iterable

def conn():
    # try:
    connect = pymysql.connect(
    host='localhost', 
    port=3306,
    user='root',
    password='9290',
    database="genshin"
    ) #服务器名,账户,密码,数据库名
    if connect:
        print("连接成功!")
    print("conn running")
    cursor_obj = connect.cursor(pymysql.cursors.DictCursor)
    cursor_obj.execute('select * from characters order by weaponType')
    user = cursor_obj.fetchall()
    # print(user[0]["name"])
    for i in user:
        # for j in i.values():
        #     print(j," "*2, end="\t")
        temp = i.values()
        for j in temp:
            out_j = str(j)
            print('%-7s'%(out_j),end="")
        print()
        # outTemp = (temp(0))
        # print('%-2d %-5s %-5s %-5s %-5s '%(outTemp))
    # user[0]
    cursor_obj.execute('select count(*) from characters where rankStar="五星"')
    count = cursor_obj.fetchall()
    print(count)
    # return connect


if __name__ == '__main__':
    conn = conn()
    # conn.close()