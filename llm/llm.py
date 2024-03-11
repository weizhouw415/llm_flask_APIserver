from langchain_community.chat_models import QianfanChatEndpoint
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from common.error.error import Error
import common.error.error_code as ErrCode
import common.error.error_msg as ErrMsg
from common.log.logger import logger


class LLMmodel():
    def __init__(self, model: str = "qianfan", temp: float = 0.9):
        self.model = model
        self.temp = temp
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

    def tool(self, msg: str, input: dict = {}):
        try:
            model = self.get_model()
            if isinstance(model, Error):
                return model
                
            prompt = ChatPromptTemplate.from_template(msg)
            parser = StrOutputParser()
            
            chain = prompt | model | parser
            return chain.invoke(input)
        except Exception as e:
            logger.error(e)
            return Error(ErrCode.ERR_CODE_LLM_REPLY, ErrMsg.ERR_MSG_LLM_REPLY)
