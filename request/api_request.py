from request.request_checker import RequestChecker
import common.error.error_code as ErrorCodes 
import common.error.error_msg as ErrorMsg
from common.error.error import Error
from common.log.logger import logger
import common.constants as Const

class APIRequest():

    def __init__(self, api, params):
        self.api = api
        self.params = params

    def __str__(self):
        return (('api:(%s) params:(%s)') % ( self.api, self.params))

    def _check_core_params(self):
        ''' TODO: check core params '''
        core_params = []
        for param in core_params:
            if param not in self.params:
                return False
        
        return True
    
    def _check_expires(self):
        ''' TODO: check expires '''
        return True

    def _check_signature(self):
        ''' TODO: check signature'''
        return True
    
    def validate(self):
        ''' TODO: validate request '''
        if not self._check_core_params():
            return False
        
        if not self._check_expires():
            return False

        if not self._check_signature():
            return False

        return True

    def check_request(self):
        if not self.validate():
            return Error(ErrorCodes.ERR_CODE_VALIDATE,
                         ErrorMsg.ERR_MSG_AUTH_ERROR)
        checker = RequestChecker(self.params)
        ret = checker.check_request(self.api, self.params)
        if not ret:
            return checker.get_error()
        return ret

def api_request(req):
    return APIRequest(req.get('api', ''), req).check_request()