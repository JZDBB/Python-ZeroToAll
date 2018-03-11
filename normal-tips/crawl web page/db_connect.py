# -*- coding: UTF-8 -*-


import MySQLdb
  
# 连接数据库  
conn = MySQLdb.connect(host="192.168.128.55", port=3306, user="root", passwd="", db="skdb", charset="utf8")  
  
cursor = conn.cursor() 
  
# recordCount = 0

def insertOneData(sql):
    # global recordCount
    # recordCount=recordCount+1
    # print recordCount
    cursor.execute(sql)
    conn.commit()
    #if(recordCount % 100 == 0):

def generateSQL(info):
    insertSql = "insert into news_corpus";
    str1 = ""
    str2 = ""
    for key, value in info.items():
        if value == None or value == "unknown" or value == "None":
            value = ""
        str1 = str1 + key + ",";
        str2 = str2 + "'" + MySQLdb.escape_string(value) + "',"
    str1 = str1[:len(str1) - 1]
    str2 = str2[:len(str2) - 1]
    insertSql = insertSql + "(" + str1 + ") values(" + str2 + ")"
    return insertSql

def close():
    cursor.close()
    conn.close()
