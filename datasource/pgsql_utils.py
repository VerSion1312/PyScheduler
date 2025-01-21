# -*- coding: UTF-8 -*-
"""
@File    ：pgsql_utils.py
@Author  ：VerSion
@Date    ：2024/11/25 17:53
"""
import psycopg2
from psycopg2.extras import RealDictCursor

from . import get_db_config


def execute_pgsql_query(db_name, query, params=None):
    try:
        # 获取数据库配置
        db_config = get_db_config(db_name)

        # 连接到数据库
        conn = psycopg2.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database']
        )

        # 创建游标，使用 RealDictCursor 返回字典类型的结果
        cursor = conn.cursor(cursor_factory=RealDictCursor)

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
    except Exception as e:
        raise Exception(f"PostgreSQL 查询失败: {e}")
