# -*- coding: UTF-8 -*-
"""
@File    ：oracle_utils.py
@Author  ：VerSion
@Date    ：2024/11/26 09:09
"""
import cx_Oracle

from . import get_db_config


def execute_oracle_query(db_name, query, params=None):
    try:
        # 获取数据库配置
        db_config = get_db_config(db_name)

        # 连接到数据库
        dsn = cx_Oracle.makedsn(db_config['host'], db_config['port'], service_name=db_config['service_name'])
        conn = cx_Oracle.connect(
            user=db_config['user'],
            password=db_config['password'],
            dsn=dsn
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
    except cx_Oracle.Error as e:
        raise Exception(f"Oracle 查询失败: {e}")
