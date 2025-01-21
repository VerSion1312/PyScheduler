# -*- coding: UTF-8 -*-
"""
@File    ：api_client.py
@Author  ：VerSion
@Date    ：2024/11/25 17:28 
"""
import base64
import logging
import time

import requests


class APIClient:
    _err_dic = {
        401: "User is not authenticated, or authentication has expired",
        403: "Interface Need Authentication",
        404: "Interface not Found"
    }
    """
    API客户端类，用于与特定的API服务进行交互。

    该类负责管理访问令牌的获取和刷新，并提供方法来发起API请求。
    """

    def __init__(self, base_url, app_id, app_secret):
        """
        初始化API客户端。

        参数:
        - base_url: API服务的基础URL。
        - app_id: 应用的标识符。
        - app_secret: 应用的秘密。
        """
        self.base_url = base_url
        self.app_id = app_id
        self.app_secret = app_secret
        self.access_token = None
        self.token_expires_at = 0

    def _get_basic_auth(self):
        """
        获取基础认证token。

        返回:
        - 认证字符串，用于发起认证请求。
        """
        auth_str = f"{self.app_id}:{self.app_secret}"
        auth_bytes = auth_str.encode('utf-8')
        auth_base64 = base64.b64encode(auth_bytes).decode('utf-8')
        return f"Basic {auth_base64}"

    def _get_access_token(self):
        """
        获取访问令牌。
        在这里实现接口认证的逻辑（如果有的话）。
        该方法通过应用的ID和秘钥来请求访问令牌，并解析响应以更新访问令牌和过期时间。
        """
        url = f"{self.base_url}/url/to/getToken"
        headers = {
            "Authorization": self._get_basic_auth()
        }
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        token_data = response.json()
        self.access_token = token_data['access_token']
        self.token_expires_at = time.time() + token_data['expires_in']

    def _ensure_access_token(self):
        """
        确保访问令牌是有效的。

        如果访问令牌不存在或者已经过期，则请求新的访问令牌。
        """
        if not self.access_token or time.time() >= self.token_expires_at:
            self._get_access_token()

    def _make_request(self, method, endpoint, **kwargs):
        """
        发起API请求。

        参数:
        - method: HTTP方法，例如GET、POST等。
        - endpoint: API的端点。
        - **kwargs: 其他传递给请求的参数。

        返回:
        - 响应的JSON数据。
        """
        retry_count = 0
        max_retries = 5  # 最大重试次数

        while True:
            self._ensure_access_token()
            url = f"{self.base_url}/{endpoint}"
            headers = {
                "Authorization": f"Bearer {self.access_token}",
                "Content-Type": "application/json;charset=UTF-8;"
            }
            response = requests.request(method, url, headers=headers, **kwargs)
            if response.status_code != 401:
                response.raise_for_status()  # 如果不是401，检查其他HTTP错误
                return response.json()  # 返回响应的JSON数据

            retry_count += 1
            if retry_count >= max_retries:
                raise Exception(f"达到最大重试次数 ({max_retries})，接口状态仍为 401，请检查系统接口。")
            else:
                logging.info(f"第 {retry_count} 次重试...")
            # 等待一段时间后重试
            time.sleep(1)

    def _check_err(self, response):
        code = response.get('code')
        if code in self._err_dic:
            raise Exception(self._err_dic[code] + '异常信息：' + response.get('message'))
        if str(code)[0] == '5':
            raise Exception('服务端异常。异常信息：' + response.get('message'))
        if response.get('errorResult', True):
            raise Exception('接口返回了一个异常。异常信息：' + response.get('message'))
        return response

    def api_get(self, endpoint, **kwargs):
        """
        发起GET请求。

        参数:
        - endpoint: API的端点。
        - **kwargs: 其他传递给请求的参数。

        返回:
        - 响应的JSON数据。
        """
        return self._check_err(self._make_request('GET', endpoint, **kwargs))

    def api_post(self, endpoint, **kwargs):
        """
        发起POST请求。

        参数:
        - endpoint: API的端点。
        - **kwargs: 其他传递给请求的参数。

        返回:
        - 响应的JSON数据。
        """
        return self._check_err(self._make_request('POST', endpoint, **kwargs))

    def api_put(self, endpoint, **kwargs):
        """
        发起PUT请求。

        参数:
        - endpoint: API的端点。
        - **kwargs: 其他传递给请求的参数。

        返回:
        - 响应的JSON数据。
        """
        return self._check_err(self._make_request('PUT', endpoint, **kwargs))

    def api_delete(self, endpoint, **kwargs):
        """
        发起DELETE请求。

        参数:
        - endpoint: API的端点。
        - **kwargs: 其他传递给请求的参数。

        返回:
        - 响应的JSON数据。
        """
        return self._check_err(self._make_request('DELETE', endpoint, **kwargs))
