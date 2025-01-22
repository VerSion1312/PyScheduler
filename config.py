# -*- coding: UTF-8 -*-
"""
@File    ：config.py
@Author  ：VerSion
@Date    ：2024/11/18 16:53
"""
from apscheduler.schedulers.background import BackgroundScheduler

from tasks import getTestDataTasks

scheduler = BackgroundScheduler()

# 在此处添加任务
# 添加任务：定时同步测试数据，每2小时执行一次
scheduler.add_job(getTestDataTasks.get_test_data, 'cron', hour='*/2', id='get_test_data',
                  kwargs={'begin_date': '', 'end_date': ''})


def start_scheduler():
    scheduler.start()
