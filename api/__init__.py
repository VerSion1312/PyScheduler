# -*- coding: UTF-8 -*-
"""
@File    ：__init__.py
@Author  ：VerSion
@Date    ：2024/11/25 17:28
"""

# 导入APIClient类，用于构建和管理API客户端
from .api_client import APIClient

# 实例化一个默认的API客户端，用于连接和操作API服务
# 该客户端配置了基础URL、app_id和app_secret，以便在调用API时进行身份验证和授权，若没有可不配置
default_api_client = APIClient(
    base_url="https://write.your.api/here",
    app_id="appIdOfAuthentication",
    app_secret="secret-key-of-authentication"
)


# 获取默认的API客户端实例
# 该函数无需参数，返回一个已经配置好基础URL、app_id和app_secret的API客户端实例
def get_api_client():
    return default_api_client
