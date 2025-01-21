# -*- coding: UTF-8 -*-
"""
@File    ：getTestDataTasks.py
@Author  ：VerSion
@Date    ：2024/11/18 16:52
@Remark  ：此文件为编写数据同步任务的案例
"""
import datetime
import logging

from api import get_api_client
from datasource import execute_mysql_query
from . import record_task_history


def get_test_data(begin_date='', end_date=''):
    # 如果没传入起止日期，则默认取3小时前的
    if begin_date == '':
        begin_date = (datetime.datetime.now() - datetime.timedelta(hours=3)).strftime('%Y-%m-%d %H:%M:%S')

    if end_date == '':
        end_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    msg = ''
    logging.info(f'开始同步 {begin_date} 到 {end_date} 的测试数据...')

    try:
        datas = []

        # 获取测试数据
        sql = f"""  SELECT      *
                    FROM        tbl_test
                    WHERE       create_time >= '{begin_date}'
                                AND create_time < '{end_date}'
                    ORDER BY    create_time DESC"""
        # 查询数据
        datas.extend(execute_mysql_query('test_db', sql))

        if len(datas) > 0:
            # 创建API客户端
            api_client = get_api_client()
            # 通过某种方法插入数据，此处以接口为例
            insert_response = api_client.api_post('url/to/insert', json=datas)
            if len(insert_response.get('success', -1)) != 0:
                raise Exception(insert_response.get('message', '未知异常'))
            logging.info(f'数据同步成功， 本次上传 {len(datas)} 条')

        if msg == '':
            msg = '已完成'
    except Exception as e:
        msg = f'异常: {str(e)}'
    finally:
        record_task_history('get_test_data', msg)
        logging.info(msg)
