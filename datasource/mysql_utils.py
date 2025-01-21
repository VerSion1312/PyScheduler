# -*- coding: UTF-8 -*-
"""
@File    ：mysql_utils.py
@Author  ：VerSion
@Date    ：2024/11/26 09:08
"""
import pymysql

from . import get_db_config


def execute_mysql_query(db_name, query, params=None):
    try:
        # 获取数据库配置
        db_config = get_db_config(db_name)

        # 连接到数据库
        conn = pymysql.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database'],
            cursorclass=pymysql.cursors.DictCursor  # 使用字典游标
        )

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
    except pymysql.MySQLError as e:
        raise Exception(f"MySQL 查询失败: {e}")
