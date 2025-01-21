# -*- coding: UTF-8 -*-
"""
@File    ：__init__.py
@Author  ：VerSion
@Date    ：2024/11/19 09:08
"""
import json
import os
from datetime import datetime
from typing import Any

# 任务运行历史记录
task_history: list[Any] = []
MAX_HISTORY_SIZE: int = 500
HISTORY_FILE: str = "task_history.json"


def load_task_history():
    global task_history
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as file:
            file_content = file.read().strip()
            if len(file_content) == 0:
                task_history = []
            else:
                task_history = json.loads(file_content)
    else:
        task_history = []
    print(task_history)
    return task_history


def save_task_history():
    with open(HISTORY_FILE, 'w') as file:
        json.dump(task_history, file, indent=4)


def record_task_history(job_id, status):
    task_history.append({
        'job_id': job_id,
        'status': status,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })
    # 限制任务历史记录在最大限制内
    if len(task_history) > MAX_HISTORY_SIZE:
        del task_history[0: len(task_history) - MAX_HISTORY_SIZE]
    # 按照时间戳倒序排列
    task_history.sort(key=lambda x: x['timestamp'], reverse=True)
    # 保存到文件
    save_task_history()
