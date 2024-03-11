import json
import common.constants as Const
from models.host_model import HostModel

class ServerContext():

    def __init__(self):
        self.config = None
        self.host_cache = {}
        self.conn = None

    def init(self):
        with open(Const.SERVER_CONFIG_PATH, 'r', encoding='utf-8') as f:
            self.config = json.load(f)

        hosts = HostModel.search()
        for item in hosts:
            self.host_cache[item['host_id']] = item['host_ip']

g_server_context = None
def instance():
    global g_server_context
    if g_server_context is None:
        g_server_context = ServerContext()
        g_server_context.init()
    return g_server_context

