import common.constants as Const

class ServerContext():

    def __init__(self):
        self.host_cache = []

g_server_context = None
def instance():
    global g_server_context
    if g_server_context is None:
        g_server_context = ServerContext()
    return g_server_context

