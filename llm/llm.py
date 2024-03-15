from langchain_community.chat_models import QianfanChatEndpoint
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
import json
from math import pow
from common.error.error import Error
import common.error.error_code as ErrCode
import common.error.error_msg as ErrMsg
from common.log.logger import logger
from llm.tools import *
import common.constants as Const

class LLMmodel():
    def __init__(self, model: str = "openai", temp: float = 0.9, r: int = 1):
        self.model = model
        self.temp = temp
        self.round = r  # 多轮对话缓存的轮次数
        logger.info("llm model: %s, temperature: %f", model, temp)

    def get_model(self):
        if (self.model == "openai"):
            model = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=self.temp)
        elif (self.model == "qianfan"):
            model = QianfanChatEndpoint(temperature=self.temp)
        else:
            return Error(ErrCode.ERR_CODE_LLM_MODEL_NAME, ErrMsg.ERR_MSG_LLM_MODEL_NAME)
        return model

    def reply(self, msg: str):
        try:
            model = self.get_model()
            if isinstance(model, Error):
                return model
            return model.invoke(msg).content
        except Exception as e:
            logger.error(e)
            return Error(ErrCode.ERR_CODE_LLM_REPLY, ErrMsg.ERR_MSG_LLM_REPLY)
        
    def multiple_round_reply(self, cache: list):
        try:
            if (self.round > Const.MAX_CACHE_ROUND or self.round < 1):
                return Error(ErrCode.ERR_CODE_LLM_EXCEED_ROUND, ErrMsg.ERR_MSG_LLM_EXCEED_ROUND)
            model = self.get_model()
            print(model)
            if isinstance(model, Error):
                return model
            template = ChatPromptTemplate.from_messages(cache)
            print(template)
            messages = template.format_messages()
            print(messages)
            return model.invoke(messages).content
        except Exception as e:
            logger.error(e)
            return Error(ErrCode.ERR_CODE_LLM_REPLY, ErrMsg.ERR_MSG_LLM_REPLY)

    def tool(self, msg: str):
        try:
            model = self.get_model()
            if isinstance(model, Error):
                return model
            model_with_tools = model.bind_tools([Multiply, Minus, Add, Power])      # 4 tools added
            kargs = model_with_tools.invoke(msg).additional_kwargs    
            logger.info(kargs)    
            if not kargs:
                return Error(ErrCode.ERR_CODE_LLM_FUNCTION, ErrMsg.ERR_MSG_LLM_FUNCTION)
            func = kargs["tool_calls"][0]["function"]["name"]
            args = json.loads(kargs["tool_calls"][0]["function"]["arguments"])
            result = self.handle_tools(func, args)
            if isinstance(result, Error):
                return result
            resp = {"function": func, "message": result}
            return resp
        except Exception as e:
            logger.error(e)
            return Error(ErrCode.ERR_CODE_LLM_REPLY, ErrMsg.ERR_MSG_LLM_REPLY)
        
    def handle_tools(self, function: str, args: dict):
        if (function == "Multiply"):
            return args['a'] * args['b']
        elif (function == "Add"):
            return args['a'] + args['b']
        elif (function == "Minus"):
            return args['a'] - args['b']
        elif (function == "Power"):
            return pow(args['a'], args['b'])
        else:
            return Error(ErrCode.ERR_CODE_LLM_FUNCTION_PARAM, ErrMsg.ERR_MSG_LLM_FUNCTION_PARAM)
