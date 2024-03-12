from common.log.logger import logger
from common.db.data_types import SearchType, SearchWordType
import common.constants as Const

API_PARAMETER = {
    # host
    Const.API_ROUTE_REPLY: ['model', 'message', 'temperature', 'round'],
    Const.API_ROUTE_TOOLS: ['message', 'temperature']
}

class RequestBuilder(object):
    @staticmethod
    def llm_reply(req): 
        new_req = {}
        params = API_PARAMETER[req.get('api')]
        for item in req:
            if item in params:
                new_req[item] = req[item]
        return new_req
    
    @staticmethod
    def llm_tools(req): 
        new_req = {}
        params = API_PARAMETER[req.get('api')]
        for item in req:
            if item in params:
                new_req[item] = req[item]
        return new_req

