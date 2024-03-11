import common.error.error_code as ErrorCodes
import common.error.error_msg as ErrorMsg
from common.constants import DEFAULT_LANG, SUPPORTED_LANGS

class Error(object):
    def __init__(self, code, message=None, args=None, kwargs=None):
        self.code = code
        self.message = message
        self.args = args
        self.kwargs = kwargs
        pass

    def get_code(self):
        return self.code

    def get_message(self, lang=DEFAULT_LANG):
        lang = DEFAULT_LANG if lang not in SUPPORTED_LANGS else lang
        if self.args is not None:
            msg = self.message.get(lang) % self.args
        else:
            msg = self.message.get(lang)

        if self.kwargs:
            try:
                msg = msg.format(**self.kwargs)
            except:
                pass

        return msg

