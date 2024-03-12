from common.log.logger import logger
from common.error.error import Error
import common.error.error_code as ErrCode
import common.error.error_msg as ErrMsg
from common.utils import return_success, return_error
from request.request_builder import RequestBuilder
import common.constants as Const
import common.context as context
from llm.llm import LLMmodel
from langchain_core.messages import HumanMessage, AIMessage

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
    ctx = context.instance()
    try:
        req = RequestBuilder.llm_reply(_req)
        if "temperature" in req:
            llm = LLMmodel(req["model"], req["temperature"])
        else:
            llm = LLMmodel(req["model"])
        if "round" in req:
            r = req["round"]
            if (r >= len(ctx.host_cache)):
                history = ctx.host_cache
            else:
                history = ctx.host_cache[-r:]
            reply_msg = llm.multiple_round_reply(req["message"], history)
            ctx.host_cache.append(HumanMessage(req["message"]))
            ctx.host_cache.append(AIMessage(reply_msg))
            if (len(ctx.host_cache) > Const.MAX_CACHE_ROUND):
                ctx.host_cache.pop(0)
            logger.info(ctx.host_cache)
            print(ctx.host_cache)
        else:
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


def handel_llm_tools(_req):
    rep = None
    ctx = context.instance()
    try:
        req = RequestBuilder.llm_tools(_req)
        if "temperature" in req:
            llm = LLMmodel(req["temperature"])
        else:
            llm = LLMmodel()
        return llm.tool(req["message"])
    except Exception as e:
        logger.error(e)
        rep = return_error(req, Error(ErrCode.ERR_CODE_INTERNAL_ERROR,
                                      ErrMsg.ERR_MSG_SERVER_INTERNAL_ERROR))
    logger.info(rep)
    return rep