# -*- coding: UTF-8 -*-
"""
@File    ：main.py
@Author  ：VerSion
@Date    ：2024/11/18 16:52
"""
import logging

from app import app
from config import start_scheduler
from tasks import load_task_history


def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("任务执行器开始运行...")
    start_scheduler()
    # 在程序启动时加载任务历史记录
    load_task_history()
    # 启动flask网页应用
    app.run(host='0.0.0.0', port=8398)


if __name__ == "__main__":
    main()
