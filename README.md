# PyScheduler



[English Document](./README-en.md)

运行截图

![1737515604907.png](https://version-pic-bed.oss-cn-hangzhou.aliyuncs.com/images/1737515604907.png)

![1737515634146.png](https://version-pic-bed.oss-cn-hangzhou.aliyuncs.com/images/1737515634146.png)

## 一、项目用途

本项目是一个基于Python和Flask的任务调度器，用于管理和执行定时任务。通过本项目，用户可以方便地查看任务列表、手动触发任务、查看任务的历史记录等。



## 二、目录结构
```txt
PyScheduler/ 
│  app.py
│  config.py
│  main.py
│  README.md
│  unit_test.py
│  requirements.txt
│
├─api
│  │  api_client.py
│  │  __init__.py
│
├─datasource
│  │  config_utils.py
│  │  database.ini
│  │  mysql_utils.py
│  │  oracle_utils.py
│  │  pgsql_utils.py
│  │  sqlserver_utils.py
│  │  __init__.py
│
├─static
│  ├─css
│  │      bootstrap.min.css
│  │      style.css
│  │
│  └─js
│         bootstrap.bundle.min.js
│
├─tasks
│  │  getTestDataTasks.py
│  │  __init__.py
│
├─templates
│      history.html
│      index.html
```



## 三、各文件的作用

- **`main.py`**: 项目的主入口文件，启动调度器和Flask应用。

- **`requirements.txt`**: 项目依赖清单，可以直接通过`pip install -r requirements.txt`来快速安装依赖。

- **`unit_test.py`**: 项目的单元测试入口，开发新任务时，可以在该文件中进行调用。

- **`tasks/`**: 存放任务脚本的目录。

  - **`__init__.py`**: 初始化任务模块，包含任务历史记录的记录函数。
  - **`getTestDataTasks.py`**: 示例任务程序。

- **`config.py`**: 配置调度器的文件，包含调度器的初始化和启动函数。

- **`app.py`**: Flask应用的入口文件，定义路由和视图函数。

- **`templates/`**: 存放HTML模板的目录。
  - **`index.html`**: 任务列表页面的模板。
  - **`history.html`**: 任务历史记录页面的模板。

- **`static/`**: 存放静态资源的目录。

  - **`css/`**: 存放CSS文件的目录。

    - **`bootstrap.min.css`**: Bootstrap的CSS文件。
    - **`style.css`**: 自定义的CSS样式文件。
  - **`js/`**: 存放JavaScript文件的目录。
    - **`bootstrap.bundle.min.js`**: Bootstrap的JavaScript文件。

- **`api/`**: 存放接口调用方法的目录。

  - **`api_client.py`**: 接口调用的通用方法，会在调用时校验/刷新token，并且对返回结果进行异常处理。

- **`datasource/`**: 存放数据源配置及数据库操作方法的目录。

  - **`database.ini`**: 存放数据库连接配置的文件。
  - **`config_utils.py`**: 用于读取数据库配置的方法。
  - **`mysql_utils.py`**: 用于在MySQL数据库中查询数据的方法。
  - **`oracle_utils.py`**: 用于在Oracle数据库中查询数据的方法。
  - **`pgsql_utils.py`**: 用于在PostgreSQL数据库中查询数据的方法。
  - **`sqlserver_utils.py`**: 用于在SQLServer数据库中查询数据的方法。

  

## 四、代码编写规范

1. **命名规范**:
   
   - 变量和函数名使用小写字母和下划线组合，例如`get_test_data`。
   - 类名使用驼峰命名法，例如`TaskScheduler`。
   - 常量名使用大写字母和下划线组合，例如`MAX_HISTORY_SIZE`。
   
2. **代码注释**:
   - 在关键代码段和函数前添加注释，说明其功能和参数。
   - 使用`TODO`标记待完成的任务。

3. **代码格式**:
   - 使用4个空格缩进。
   - 每行代码不超过80个字符。
   
   

## 五、新的任务的开发步骤

1. **创建任务脚本**:
   - 在`tasks/`目录下创建新的任务脚本，例如`task3.py`。
   - 在任务脚本中定义任务函数，并调用`record_task_history`记录任务执行历史。

2. **配置调度器**:
   - 在`config.py`中导入新的任务脚本。
   - 使用`scheduler.add_job`方法注册新的任务，指定任务的触发器和参数。

3. **更新前端页面**:
   - 如果需要在前端页面显示新的任务，可以在`templates/index.html`中添加新的任务行。（不建议）
   
    
   
## 六、任务注册时间设定说明

本章节将详细说明`scheduler.add_job`在注册任务时，触发时间的设定细则，包括`interval`和`cron`类型的触发器。

### 1. `interval` 类型的触发器

`interval`类型的触发器用于在固定的时间间隔内重复执行任务。你可以指定任务的执行间隔时间，例如每5秒、每10分钟等。

#### 语法

```python
scheduler.add_job(func, 'interval', **kwargs)
```

#### 参数

- `func`: 要执行的任务函数。
- `'interval'`: 指定触发器类型为`interval`。
- `**kwargs`: 其他可选参数，用于指定时间间隔。

#### 可选参数

- `seconds`: 间隔的秒数。
- `minutes`: 间隔的分钟数。
- `hours`: 间隔的小时数。
- `days`: 间隔的天数。
- `weeks`: 间隔的周数。
- `start_date`: 任务的开始日期和时间。
- `end_date`: 任务的结束日期和时间。
- `timezone`: 任务的时区。

#### 示例

```python
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

def task():
    print("Task executed!")

# 每5秒执行一次任务
scheduler.add_job(task, 'interval', seconds=5)

# 每10分钟执行一次任务
scheduler.add_job(task, 'interval', minutes=10)

# 每2小时执行一次任务
scheduler.add_job(task, 'interval', hours=2)

# 每3天执行一次任务
scheduler.add_job(task, 'interval', days=3)

# 每2周执行一次任务
scheduler.add_job(task, 'interval', weeks=2)

# 指定任务的开始日期和时间
scheduler.add_job(task, 'interval', seconds=5, start_date='2023-10-01 00:00:00')

# 指定任务的结束日期和时间
scheduler.add_job(task, 'interval', seconds=5, end_date='2023-10-31 23:59:59')

# 指定任务的时区
scheduler.add_job(task, 'interval', seconds=5, timezone='Asia/Shanghai')
```



### 2. `cron` 类型的触发器

`cron`类型的触发器用于在特定的时间点执行任务，类似于Unix/Linux中的cron作业。你可以指定任务的执行时间，例如每天的某个时间、每周的某个时间等。

#### 语法

```python
scheduler.add_job(func, 'cron', **kwargs)
```

#### 参数

- `func`: 要执行的任务函数。
- `'cron'`: 指定触发器类型为`cron`。
- `**kwargs`: 其他可选参数，用于指定时间点。

#### 可选参数

- `year`: 年份（4位数字）。
- `month`: 月份（1-12）。
- `day`: 日期（1-31）。
- `week`: 周数（1-53）。
- `day_of_week`: 星期几（0-6或mon,tue,wed,thu,fri,sat,sun）。
- `hour`: 小时（0-23）。
- `minute`: 分钟（0-59）。
- `second`: 秒（0-59）。
- `start_date`: 任务的开始日期和时间。
- `end_date`: 任务的结束日期和时间。
- `timezone`: 任务的时区。

#### 示例

```python
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

def task():
    print("Task executed!")

# 每分钟执行一次任务
scheduler.add_job(task, 'cron', minute='*')

# 每小时的第15分钟执行一次任务
scheduler.add_job(task, 'cron', minute=15)

# 每天的10:30执行一次任务
scheduler.add_job(task, 'cron', hour=10, minute=30)

# 每周一的10:30执行一次任务
scheduler.add_job(task, 'cron', day_of_week='mon', hour=10, minute=30)

# 每月的1号和15号的10:30执行一次任务
scheduler.add_job(task, 'cron', day='1,15', hour=10, minute=30)

# 每年的1月1号的00:00执行一次任务
scheduler.add_job(task, 'cron', month='1', day='1', hour=0, minute=0)

# 指定任务的开始日期和时间
scheduler.add_job(task, 'cron', minute='*', start_date='2023-10-01 00:00:00')

# 指定任务的结束日期和时间
scheduler.add_job(task, 'cron', minute='*', end_date='2023-10-31 23:59:59')

# 指定任务的时区
scheduler.add_job(task, 'cron', minute='*', timezone='Asia/Shanghai')
```

### 3. 混合使用 `interval` 和 `cron`

你可以在同一个调度器中混合使用`interval`和`cron`类型的触发器，以满足不同的任务调度需求。

#### 示例

```python
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

def task1():
    print("Task 1 executed!")

def task2():
    print("Task 2 executed!")

# 每5秒执行一次任务1
scheduler.add_job(task1, 'interval', seconds=5)

# 每天的10:30执行一次任务2
scheduler.add_job(task2, 'cron', hour=10, minute=30)

scheduler.start()
```



## 七、开发中的注意事项

1. **任务执行时间**:
   - 确保任务的执行时间不会与其他任务冲突，避免资源竞争。

2. **异常处理**:
   - 在任务函数中添加异常处理逻辑，记录任务执行失败的详细信息。

3. **历史记录限制**:
   - 任务历史记录限制在100条内，超过100条后删除最早的记录。
   
   

## 八、Q&A

### Q1: 如何手动触发任务？
A1: 在任务列表页面，点击任务行中的“触发”按钮，会弹出确认框，点击确认后任务会立即执行。

### Q2: 如何查看任务的历史记录？
A2: 在任务列表页面，点击任务名称，会跳转到该任务的历史记录页面，显示任务的执行历史。

### Q3: 如何添加新的任务？
A3: 在`tasks/`目录下创建新的任务脚本，并在`config.py`中注册新的任务。

### Q4: 如何修改任务的触发时间？
A4: 在`config.py`中修改任务的触发器参数，例如`cron`表达式或`interval`时间。

### Q5: 如何限制任务历史记录的数量？
A5: 在`tasks/__init__.py`中，使用`del task_history[0: len(task_history) - MAX_HISTORY_SIZE]`方法删除最早的记录，确保任务历史记录限制在限制条数内。



## 九、发布方法

### 1. 安装Python和依赖

以CentOS系统为例。（其余系统可类比发布）

首先，确保你的CentOS系统上已经安装了Python和pip。如果没有安装，可以使用以下命令进行安装：

```bash
sudo yum install python3
sudo yum install python3-pip
```

然后，使用pip安装项目所需的依赖：

```bash
sudo pip3 install Flask apscheduler
```

### 2. 创建项目目录

在CentOS系统上创建一个目录来存放你的项目文件。例如：

```bash
sudo mkdir /opt/PyScheduler
cd /opt/PyScheduler
```

将你的项目文件（包括`main.py`、`config.py`、`app.py`、`tasks/`、`templates/`、`static/`等）上传到这个目录中。

### 3. 安装项目依赖

为了项目能够正常运行，需要安装所有需要的项目依赖。项目中内置了依赖清单`requirements.txt`，可通过以下指令来快速安装依赖。

```bash
sudo pip3 install -r requirements.txt
```

> 在安装依赖中的`psycopg2`包时可能会出现异常，这是因为psycopg2包需要有PostgreSQL 的开发包，可以通过以下两个方法来解决该问题：
>
> 1. 使用以下命令安装PostgreSQL 的开发包。
>
>    ```bash
>    sudo yum install postgresql-devel
>    ```
>
> 2. 如果实际业务场景用不到PostgreSQL，那么可以移除项目依赖中的psycopg2和pgsql_utils。具体操作为：
>
>    - 删除`requirements.txt`中的`psycopg2~=2.9.10`
>    - 删除`/datasource/pgsql_utils.py`文件

### 4. 创建systemd服务

为了使项目在后台持续运行，并能够在系统启动时自动启动，我们可以创建一个systemd服务。

#### 创建服务文件

在`/etc/systemd/system/`目录下创建一个新的服务文件，例如`PyScheduler.service`：

```bash
sudo nano /etc/systemd/system/PyScheduler.service
```

在文件中添加以下内容：

```ini
[Unit]
Description=python task scheduler
After=network.target

[Service]
User=your_username
WorkingDirectory=/opt/PyScheduler
ExecStart=/usr/bin/python3 /opt/PyScheduler/main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

请将`your_username`替换为你的系统用户名。

#### 启动并启用服务

保存并关闭文件后，使用以下命令启动服务并设置为开机自启：

```bash
sudo systemctl daemon-reload
sudo systemctl start PyScheduler
sudo systemctl enable PyScheduler
```

### 5. 配置防火墙

如果你的CentOS系统启用了防火墙（如Firewalld），需要允许HTTP/HTTPS流量通过防火墙。

```bash
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --reload
```

### 6. 访问项目

现在，你可以通过浏览器访问你的项目。假设你的CentOS服务器的IP地址是`192.168.1.100`，你可以访问`http://192.168.1.100:8398/`来查看任务调度面板。

### 7. 日志管理

为了方便查看项目的运行日志，你可以配置日志文件。在`main.py`中添加日志记录：

#### `main.py`

```python
import logging
from config import start_scheduler
from app import app

if __name__ == '__main__':
    logging.basicConfig(filename='/var/log/PyScheduler.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    start_scheduler()
    app.run(debug=False, port=8398)
```

### 8. 监控和管理

你可以使用以下命令来监控和管理你的服务：

- 查看服务状态：

  ```bash
  sudo systemctl status PyScheduler
  ```

- 查看日志：

  ```bash
  sudo journalctl -u PyScheduler
  ```

- 重启服务：

  ```bash
  sudo systemctl restart PyScheduler
  ```

