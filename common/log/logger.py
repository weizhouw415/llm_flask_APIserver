import os
import logging
from logging.handlers import RotatingFileHandler
from common.log.logger_name import get_logger_name
from common.constants import LOGGER_HOME

class WFLevelFilter(logging.Filter):
    def filter(self, record):
        return (record.levelno > logging.INFO)


class MsgFormatter(logging.Formatter):
    def __init__(self, fmt=None, datefmt=None):
        logging.Formatter.__init__(self, fmt, datefmt)

    def format(self, record):
        # in bot environment, msg_id is spread by thread local variable
        msg_id = ""
        if msg_id == "":
            # in script environment, msg_id is spread by environment variable
            msg_id = os.environ.get("MSG_ID", "")
        record.msg_id = "" if msg_id == "" else "(%s)" % msg_id
        return logging.Formatter.format(self, record)


logger_name = get_logger_name()

# formatter
formatter = MsgFormatter('%(asctime)s %(levelname)s -%(thread)d- %(message)s (%(pathname)s:%(lineno)d)%(msg_id)s')
rootLogger = logging.getLogger()
# loghome = LOGGER_HOME
loghome = "/home/wwz"   # for debug

# handler2: to log file
logfile = loghome + "/%s.log" % logger_name
h2 = RotatingFileHandler(logfile, mode='a', maxBytes=100000000, backupCount=3)
h2.setFormatter(formatter)
rootLogger.addHandler(h2)

# handler3: to log file, but only warning/error/fatal messages
logfile = loghome + "/%s.log.wf" % logger_name
h3 = RotatingFileHandler(logfile, mode='a', maxBytes=100000000, backupCount=3)
f3 = WFLevelFilter()
h3.addFilter(f3)
h3.setFormatter(formatter)
rootLogger.addHandler(h3)

logger = logging.getLogger(logger_name)
logger.setLevel(logging.INFO)

# new root logger with formatter handler
app_developer_logger = logging.RootLogger(logging.INFO)

# add dispatch_handler
app_developer_formatter = MsgFormatter('%(asctime)s %(levelname)s -%(thread)d- (AppCenter) %(message)s (%(pathname)s:%(lineno)d)%(msg_id)s')

logfile = loghome + "/%s.log" % logger_name
app_developer_h2 = RotatingFileHandler(logfile, mode='a', maxBytes=100000000, backupCount=3)
app_developer_h2.setFormatter(app_developer_formatter)
app_developer_logger.addHandler(app_developer_h2)

logfile = loghome + "/%s.log.wf" % logger_name
app_developer_h3 = RotatingFileHandler(logfile, mode='a', maxBytes=100000000, backupCount=3)
app_developer_h3.setFormatter(app_developer_formatter)
app_developer_h3.addFilter(f3)
app_developer_logger.addHandler(app_developer_h3)


__all__ = [logger, app_developer_logger]
