# -*- coding: UTF-8 -*-
"""
@File    ：config_utils.py
@Author  ：VerSion
@Date    ：2024/11/26 16:41
"""
import configparser
import os


def get_db_config(db_name):
    try:
        config = configparser.ConfigParser()
        # 使用相对路径读取 database.ini 文件
        config.read(os.path.join(os.path.dirname(__file__), 'database.ini'), encoding='utf-8')
        return config[db_name]
    except KeyError:
        raise KeyError(f"当前不存在名为'{db_name}' 的数据库配置")
