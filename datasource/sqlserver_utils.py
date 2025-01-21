# -*- coding: UTF-8 -*-
"""
@File    ：sqlserver_utils.py
@Author  ：VerSion
@Date    ：2024/11/26 09:09
"""
import pyodbc

from . import get_db_config


def execute_sqlserver_query(db_name, query, params=None):
    try:
        # 获取数据库配置
        db_config = get_db_config(db_name)

        # 连接到数据库
        conn_str = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={db_config['host']};"
            f"DATABASE={db_config['database']};"
            f"UID={db_config['user']};"
            f"PWD={db_config['password']}"
        )
        conn = pyodbc.connect(conn_str)

        # 创建游标
        cursor = conn.cursor()

        # 执行查询
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        # 获取查询结果
        result = cursor.fetchall()

        # 关闭游标和连接
        cursor.close()
        conn.close()

        return result
    except pyodbc.Error as e:
        raise Exception(f"SQL Server 查询失败: {e}")
