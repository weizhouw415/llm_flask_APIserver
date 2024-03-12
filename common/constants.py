# -*- coding: utf-8 -*-

# logger
LOGGER_NAME = "llmapiserver"
LOGGER_HOME = "/var/log"

# lang
EN = "en"
ZH_CN = "zh-cn"
DEFAULT_LANG = EN
SUPPORTED_LANGS = [EN, ZH_CN]

# config file path
SERVER_CONFIG_PATH = ""

# database config constants
REMOTE_APP_SERVER_DB_PATH = ""

# log config constants
REMOTE_APP_SERVER_LOG_PATH = ""

# 
MAX_CACHE_ROUND = 10

# APIs
API_ROUTE_TEST = "/llm/test"
API_ROUTE_INDEX = "/llm/index"
API_ROUTE_REPLY = "/llm/reply"
API_ROUTE_TOOLS = "/llm/tools"