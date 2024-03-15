from common.utils import is_integer, is_str, is_str, to_list
from common.log.logger import logger
import common.error.error_code as ErrorCodes
import common.error.error_msg as ErrorMsg
from common.error.error import Error
import common.constants as Const

class RequestChecker(object):
    def __init__(self, sender):
        self.error = Error(ErrorCodes.ERR_CODE_INVALID_REQUEST_PARAM)

    def get_error(self):
        return self.error

    def set_error(self, msg=None, *args):
        _args = []
        for a in args:
            _args += to_list(a)
        self.error = Error(
            ErrorCodes.ERR_CODE_INVALID_REQUEST_PARAM, msg, tuple(_args))

    def _trim_directive(self, directive):
        param_to_trim = []
        for param in directive:
            if directive[param] is not None:
                continue
            param_to_trim.append(param)

        for param in param_to_trim:
            del directive[param]

    def _trim_list(self, list_items):
        new_items = list()
        for item in list_items:
            if item is None:
                continue
            if not is_str(item) and not is_integer(item):
                continue
            if item not in new_items:
                new_items.append(item)
        return new_items

    def _check_str_params(self, directive, params):
        for param in params:
            if param not in directive:
                continue
            if not is_str(directive[param]):
                self.set_error(ErrorMsg.ERR_MSG_INVALID_REQUEST_PARAM, param)
                return False
        return True

    def _check_integer_params(self, directive, params):
        for param in params:
            if param not in directive:
                continue
            val = directive[param]
            if not is_integer(val):
                self.set_error(
                    ErrorMsg.ERR_MSG_INVALID_REQUEST_PARAM, param)
                return False
        return True

    def _check_list_params(self, directive, params, notrim=[]):
        for param in params:
            if param not in directive:
                continue
            if not isinstance(directive[param], list):
                self.set_error(
                    ErrorMsg.ERR_MSG_INVALID_REQUEST_PARAM, param)
                return False
            if notrim and param in notrim:
                continue
            directive[param] = self._trim_list(directive[param])
        return True

    def _check_required_params(self, directive, params):
        for param in params:
            if param not in directive or directive[param] is None:
                self.set_error(ErrorMsg.ERR_MSG_INVALID_REQUEST_PARAM, param)
                return False
        return True

    def _check_params(self, directive, required_params=[], str_params=[],
                      integer_params=[], list_params=[]):
        return self._check_required_params(directive, required_params) and \
            self._check_str_params(directive, str_params) and \
            self._check_integer_params(directive, integer_params) and \
            self._check_list_params(directive, list_params)

    def check_request(self, api, directive):
        handler_map = {
            # host
            Const.API_ROUTE_REPLY: self.llm_reply,
            Const.API_ROUTE_TOOLS: self.llm_tools
        }
        return handler_map[api](directive)

    def llm_reply(self, directive):
        if not self._check_params(directive,
                                  required_params=['model', 'message'],
                                  str_params=['model', 'message', 'temperature', 'taskid'],
                                  integer_params=[],
                                  list_params=[]):
            return False
        return True

    def llm_tools(self, directive):
        if not self._check_params(directive,
                                  required_params=['message'],
                                  str_params=['message', 'temperature'],
                                  integer_params=[],
                                  list_params=[]):
            return False
        return True
