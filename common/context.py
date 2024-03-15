import common.constants as Const

class ServerContext():

    def __init__(self):
        self.chat_history_cache = {}
        # cache format：{<task-id>: ["list of chat history"]}

g_server_context = None
def instance():
    global g_server_context
    if g_server_context is None:
        g_server_context = ServerContext()
    return g_server_context

