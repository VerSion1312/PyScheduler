# -*- coding: UTF-8 -*-
"""
@File    ：__init__.py
@Author  ：VerSion
@Date    ：2024/11/19 17:31
"""
from .config_utils import get_db_config
from .mysql_utils import execute_mysql_query
from .oracle_utils import execute_oracle_query
from .pgsql_utils import execute_pgsql_query
from .sqlserver_utils import execute_sqlserver_query
