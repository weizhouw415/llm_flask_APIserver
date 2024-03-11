from common.constants import LOGGER_NAME

g_logger_name = None
def set_logger_name(logger_name):
    global g_logger_name
    g_logger_name = logger_name
    return

def get_logger_name():
    global g_logger_name
    if not g_logger_name:
        return LOGGER_NAME
    return g_logger_name 


