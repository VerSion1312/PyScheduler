# PyScheduler



[中文文档](./README.md)

ScreenShots

![1737515604907.png](https://version-pic-bed.oss-cn-hangzhou.aliyuncs.com/images/1737515604907.png)

![1737515634146.png](https://version-pic-bed.oss-cn-hangzhou.aliyuncs.com/images/1737515634146.png)


## 1. Project Purpose

This project is a Python and Flask-based task scheduler designed to manage and execute scheduled tasks. Through this project, users can easily view the task list, manually trigger tasks, check task history, and more.

## 2. Directory Structure
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

## 3. File Descriptions

- **`main.py`**: The main entry file of the project, which starts the scheduler and Flask application.

- **`requirements.txt`**: The project dependency list. You can quickly install dependencies using `pip install -r requirements.txt`.

- **`unit_test.py`**: The entry point for unit testing. When developing new tasks, you can call them in this file.

- **`tasks/`**: Directory for storing task scripts.

  - **`__init__.py`**: Initializes the task module, including the function for recording task history.
  - **`getTestDataTasks.py`**: Example task script.

- **`config.py`**: Configuration file for the scheduler, containing initialization and startup functions.

- **`app.py`**: Entry file for the Flask application, defining routes and view functions.

- **`templates/`**: Directory for storing HTML templates.
  - **`index.html`**: Template for the task list page.
  - **`history.html`**: Template for the task history page.

- **`static/`**: Directory for storing static resources.

  - **`css/`**: Directory for CSS files.

    - **`bootstrap.min.css`**: Bootstrap CSS file.
    - **`style.css`**: Custom CSS stylesheet.
  - **`js/`**: Directory for JavaScript files.
    - **`bootstrap.bundle.min.js`**: Bootstrap JavaScript file.

- **`api/`**: Directory for storing API call methods.

  - **`api_client.py`**: General method for API calls, which validates/refreshes tokens and handles exceptions in the returned results.

- **`datasource/`**: Directory for storing data source configurations and database operation methods.

  - **`database.ini`**: File for storing database connection configurations.
  - **`config_utils.py`**: Method for reading database configurations.
  - **`mysql_utils.py`**: Method for querying data in MySQL databases.
  - **`oracle_utils.py`**: Method for querying data in Oracle databases.
  - **`pgsql_utils.py`**: Method for querying data in PostgreSQL databases.
  - **`sqlserver_utils.py`**: Method for querying data in SQLServer databases.

## 4. Code Writing Standards

1. **Naming Conventions**:
   
   - Variable and function names should use lowercase letters and underscores, e.g., `get_test_data`.
   - Class names should use CamelCase, e.g., `TaskScheduler`.
   - Constant names should use uppercase letters and underscores, e.g., `MAX_HISTORY_SIZE`.
   
2. **Code Comments**:
   - Add comments before key code segments and functions to explain their purpose and parameters.
   - Use `TODO` to mark tasks that need to be completed.

3. **Code Formatting**:
   - Use 4 spaces for indentation.
   - Each line of code should not exceed 80 characters.

## 5. Steps for Developing New Tasks

1. **Create Task Script**:
   - Create a new task script in the `tasks/` directory, e.g., `task3.py`.
   - Define the task function in the script and call `record_task_history` to log task execution history.

2. **Configure Scheduler**:
   - Import the new task script in `config.py`.
   - Use `scheduler.add_job` to register the new task, specifying the trigger and parameters.

3. **Update Frontend Page**:
   - If the new task needs to be displayed on the frontend page, add a new task row in `templates/index.html`. (Not recommended)

## 6. Task Registration Time Settings

This section details the settings for the `scheduler.add_job` method when registering tasks, including `interval` and `cron` type triggers.

### 1. `interval` Type Trigger

The `interval` type trigger is used to repeat tasks at fixed intervals. You can specify the interval, such as every 5 seconds, every 10 minutes, etc.

#### Syntax

```python
scheduler.add_job(func, 'interval', **kwargs)
```

#### Parameters

- `func`: The task function to execute.
- `'interval'`: Specifies the trigger type as `interval`.
- `**kwargs`: Other optional parameters for specifying the interval.

#### Optional Parameters

- `seconds`: Interval in seconds.
- `minutes`: Interval in minutes.
- `hours`: Interval in hours.
- `days`: Interval in days.
- `weeks`: Interval in weeks.
- `start_date`: Start date and time for the task.
- `end_date`: End date and time for the task.
- `timezone`: Timezone for the task.

#### Examples

```python
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

def task():
    print("Task executed!")

# Execute task every 5 seconds
scheduler.add_job(task, 'interval', seconds=5)

# Execute task every 10 minutes
scheduler.add_job(task, 'interval', minutes=10)

# Execute task every 2 hours
scheduler.add_job(task, 'interval', hours=2)

# Execute task every 3 days
scheduler.add_job(task, 'interval', days=3)

# Execute task every 2 weeks
scheduler.add_job(task, 'interval', weeks=2)

# Specify start date and time
scheduler.add_job(task, 'interval', seconds=5, start_date='2023-10-01 00:00:00')

# Specify end date and time
scheduler.add_job(task, 'interval', seconds=5, end_date='2023-10-31 23:59:59')

# Specify timezone
scheduler.add_job(task, 'interval', seconds=5, timezone='Asia/Shanghai')
```

### 2. `cron` Type Trigger

The `cron` type trigger is used to execute tasks at specific times, similar to cron jobs in Unix/Linux. You can specify the execution time, such as daily at a certain time, weekly at a certain time, etc.

#### Syntax

```python
scheduler.add_job(func, 'cron', **kwargs)
```

#### Parameters

- `func`: The task function to execute.
- `'cron'`: Specifies the trigger type as `cron`.
- `**kwargs`: Other optional parameters for specifying the execution time.

#### Optional Parameters

- `year`: Year (4 digits).
- `month`: Month (1-12).
- `day`: Day (1-31).
- `week`: Week number (1-53).
- `day_of_week`: Day of the week (0-6 or mon,tue,wed,thu,fri,sat,sun).
- `hour`: Hour (0-23).
- `minute`: Minute (0-59).
- `second`: Second (0-59).
- `start_date`: Start date and time for the task.
- `end_date`: End date and time for the task.
- `timezone`: Timezone for the task.

#### Examples

```python
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

def task():
    print("Task executed!")

# Execute task every minute
scheduler.add_job(task, 'cron', minute='*')

# Execute task at the 15th minute of every hour
scheduler.add_job(task, 'cron', minute=15)

# Execute task daily at 10:30
scheduler.add_job(task, 'cron', hour=10, minute=30)

# Execute task every Monday at 10:30
scheduler.add_job(task, 'cron', day_of_week='mon', hour=10, minute=30)

# Execute task on the 1st and 15th of every month at 10:30
scheduler.add_job(task, 'cron', day='1,15', hour=10, minute=30)

# Execute task on January 1st at 00:00 every year
scheduler.add_job(task, 'cron', month='1', day='1', hour=0, minute=0)

# Specify start date and time
scheduler.add_job(task, 'cron', minute='*', start_date='2023-10-01 00:00:00')

# Specify end date and time
scheduler.add_job(task, 'cron', minute='*', end_date='2023-10-31 23:59:59')

# Specify timezone
scheduler.add_job(task, 'cron', minute='*', timezone='Asia/Shanghai')
```

### 3. Mixing `interval` and `cron`

You can mix `interval` and `cron` type triggers in the same scheduler to meet different task scheduling needs.

#### Example

```python
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

def task1():
    print("Task 1 executed!")

def task2():
    print("Task 2 executed!")

# Execute task1 every 5 seconds
scheduler.add_job(task1, 'interval', seconds=5)

# Execute task2 daily at 10:30
scheduler.add_job(task2, 'cron', hour=10, minute=30)

scheduler.start()
```

## 7. Development Notes

1. **Task Execution Time**:
   - Ensure that task execution times do not conflict with other tasks to avoid resource competition.

2. **Exception Handling**:
   - Add exception handling logic in task functions to log detailed information about task execution failures.

3. **History Record Limit**:
   - Limit task history records to 100 entries. Delete the oldest records when the limit is exceeded.

## 8. Q&A

### Q1: How to manually trigger a task?
A1: On the task list page, click the "Trigger" button in the task row. A confirmation box will pop up. Click confirm to execute the task immediately.

### Q2: How to view task history?
A2: On the task list page, click the task name to navigate to the task history page, which displays the execution history of the task.

### Q3: How to add a new task?
A3: Create a new task script in the `tasks/` directory and register the new task in `config.py`.

### Q4: How to modify task trigger time?
A4: Modify the trigger parameters in `config.py`, such as the `cron` expression or `interval` time.

### Q5: How to limit the number of task history records?
A5: In `tasks/__init__.py`, use `del task_history[0: len(task_history) - MAX_HISTORY_SIZE]` to delete the oldest records, ensuring the task history is limited to the specified number.

## 9. Deployment Method

### 1. Install Python and Dependencies

Taking CentOS as an example. (Other systems can be deployed similarly)

First, ensure that Python and pip are installed on your CentOS system. If not, use the following commands to install them:

```bash
sudo yum install python3
sudo yum install python3-pip
```

Then, use pip to install the project dependencies:

```bash
sudo pip3 install Flask apscheduler
```

### 2. Create Project Directory

Create a directory on the CentOS system to store your project files. For example:

```bash
sudo mkdir /opt/PyScheduler
cd /opt/PyScheduler
```

Upload your project files (including `main.py`, `config.py`, `app.py`, `tasks/`, `templates/`, `static/`, etc.) to this directory.

### 3. Install Project Dependencies

To ensure the project runs smoothly, install all required dependencies. The project includes a dependency list `requirements.txt`, which can be used to quickly install dependencies:

```bash
sudo pip3 install -r requirements.txt
```

> When installing the `psycopg2` package from the dependencies, you may encounter exceptions. This is because the psycopg2 package requires the PostgreSQL development package. You can resolve this issue using the following two methods:
>
> 1. Install the PostgreSQL development package using the following command:
>
>    ```bash
>    sudo yum install postgresql-devel
>    ```
>
> 2. If PostgreSQL is not required in your actual business scenario, you can remove psycopg2 and pgsql_utils from the project dependencies. The specific steps are as follows:
>
>    - Delete `psycopg2~=2.9.10` from `requirements.txt`.
>    - Delete the `/datasource/pgsql_utils.py` file.

### 4. Create systemd Service

To keep the project running in the background and start automatically on system boot, create a systemd service.

#### Create Service File

Create a new service file in the `/etc/systemd/system/` directory, e.g., `PyScheduler.service`:

```bash
sudo nano /etc/systemd/system/PyScheduler.service
```

Add the following content to the file:

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

Replace `your_username` with your system username.

#### Start and Enable the Service

After saving and closing the file, use the following commands to start the service and enable it to start on boot:

```bash
sudo systemctl daemon-reload
sudo systemctl start PyScheduler
sudo systemctl enable PyScheduler
```

### 5. Configure Firewall

If your CentOS system has a firewall enabled (e.g., Firewalld), allow HTTP/HTTPS traffic through the firewall.

```bash
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --reload
```

### 6. Access the Project

Now, you can access your project via a browser. Assuming your CentOS server's IP address is `192.168.1.100`, you can visit `http://192.168.1.100:8398/` to view the task scheduler panel.

### 7. Log Management

To easily view project logs, configure a log file. Add logging in `main.py`:

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

### 8. Monitoring and Management

You can use the following commands to monitor and manage your service:

- Check service status:

  ```bash
  sudo systemctl status PyScheduler
  ```

- View logs:

  ```bash
  sudo journalctl -u PyScheduler
  ```

- Restart the service:

  ```bash
  sudo systemctl restart PyScheduler
  ```