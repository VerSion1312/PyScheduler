# -*- coding: UTF-8 -*-
"""
@File    ：app.py
@Author  ：VerSion
@Date    ：2024/11/18 17:13
"""
from datetime import datetime

from flask import Flask, render_template, jsonify, request

from config import scheduler
from tasks import load_task_history

app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    jobs = scheduler.get_jobs()
    return render_template('index.html', jobs=jobs)


@app.route('/jobs')
def get_jobs():
    jobs = scheduler.get_jobs()
    job_list = []
    for job in jobs:
        job_list.append({
            'id': job.id,
            'name': job.name,
            'next_run_time': job.next_run_time,
            'trigger': str(job.trigger)
        })
    return jsonify(job_list)


@app.route('/trigger/<job_id>', methods=['POST'])
def trigger_job(job_id):
    # 获取URL中的查询参数
    params = request.args.to_dict()

    job = scheduler.get_job(job_id)
    if job:
        # 将参数传递给job的kwargs
        job.kwargs.update(params)
        job.modify(next_run_time=datetime.now())
        return jsonify({'status': 'success', 'message': f'任务 {job_id} 已成功注册，正在执行...'})
    else:
        return jsonify({'status': 'error', 'message': f'无法找到任务 {job_id}'})


@app.route('/history/<job_id>')
def history(job_id):
    # 在程序启动时加载任务历史记录
    history_list = load_task_history()
    job_history = [entry for entry in history_list if entry['job_id'] == job_id]
    return render_template('history.html', job_id=job_id, history=job_history)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8398)
