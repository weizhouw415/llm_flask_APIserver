from common.log.logger import logger
from common.error.error import Error
import common.error.error_code as ErrCode
import common.error.error_msg as ErrMsg
from common.utils import return_success, return_error
from request.request_builder import RequestBuilder
import common.constants as Const
import common.context as context
from llm.llm import LLMmodel
from langchain.prompts import HumanMessagePromptTemplate, AIMessagePromptTemplate

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
    try:
        req = RequestBuilder.llm_reply(_req)
        if "temperature" in req:
            llm = LLMmodel(req["model"], req["temperature"])
        else:
            llm = LLMmodel(req["model"])
        if "taskid" in req:
            ctx = context.instance()
            task_id = req["taskid"]
            if task_id in ctx.chat_history_cache:
                history = ctx.chat_history_cache[task_id]
            else:
                history = []
            history.append(HumanMessagePromptTemplate.from_template(req["message"]))
            reply_msg = llm.multiple_round_reply(history)
            if isinstance(reply_msg, Error):
                return reply_msg
            history.append(AIMessagePromptTemplate.from_template(reply_msg))
            logger.info(history)
            ctx.chat_history_cache[task_id] = history
            print("666: ", ctx.chat_history_cache)
        else:
            reply_msg = llm.reply(req["message"])
        if isinstance(reply_msg, Error):
            return reply_msg
        logger.info("llm reply msg: %s", reply_msg)
        rep = {"message": reply_msg}
    except Exception as e:
        logger.error(e)
        rep = return_error(_req, INTERNAL_ERROR)
    logger.info(rep)
    return rep


def handel_llm_tools(_req):
    rep = None
#    ctx = context.instance()
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