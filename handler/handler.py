from common.log.logger import logger
from common.error.error import Error
import common.error.error_code as ErrCode
import common.error.error_msg as ErrMsg
from common.utils import return_success, return_error
from request.request_builder import RequestBuilder
import common.constants as Const
import common.context as context
from llm.llm import LLMmodel

INTERNAL_ERROR = Error(ErrCode.ERR_CODE_INTERNAL_ERROR, ErrMsg.ERR_MSG_SERVER_INTERNAL_ERROR)

def handle_test(req):
    try:
        rep = return_success(req)
    except Exception as e:
        logger.error(e)
        rep = return_error(req, INTERNAL_ERROR)
    logger.info(rep)
    return rep


def handle_llm_reply(_req):
    rep = None
   # ctx = context.instance()
    try:
        req = RequestBuilder.llm_reply(_req)
        if "temperature" in req:
            llm = LLMmodel(req["model"], req["temperature"])
        else:
            llm = LLMmodel(req["model"])
        reply_msg = llm.reply(req["message"])
        if isinstance(reply_msg, Error):
            return reply_msg
        logger.info("llm reply msg: %s", reply_msg)
        rep = {"message": reply_msg}
    except Exception as e:
        logger.error(e)
        rep = return_error(req, INTERNAL_ERROR)
    logger.info(rep)
    return rep


def handel_llm_tools(req):
    rep = None
    ctx = context.instance()
    try:
        pass
    except Exception as e:
        logger.error(e)
        rep = return_error(req, Error(ErrCode.ERR_CODE_INTERNAL_ERROR,
                                      ErrMsg.ERR_MSG_SERVER_INTERNAL_ERROR))
    logger.info(rep)
    return rep