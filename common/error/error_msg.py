# -*- coding: utf-8 -*-
from common.constants import EN, ZH_CN

# request
ERR_MSG_INVALID_REQUEST_METHOD = {EN: "Invalid Http Request Method",
                                  ZH_CN: u"无效的Http请求方法"}
ERR_MSG_INVALID_REQUEST_PARAM = {EN: "Invalid Request Parameter: %s",
                                 ZH_CN: u"无效的请求参数：%s"}
ERR_MSG_VALIDATE = {EN: "Valid Parameter Error",
                                 ZH_CN: u"参数校验失败"}

# auth
ERR_MSG_AUTH_ERROR = {EN: "Auth Error",
                           ZH_CN: u"认证失败"}

# remote app agent
ERR_MSG_REMOTE_APP_AGENT_ERROR = {EN: "Remote App Agent Action(%s) Error",
                                ZH_CN: u"虚拟应用请求(%s)错误"}
ERR_MSG_REMOTE_APP_AGENT_RETURN_DATA_FORMAT_ERROR = {EN: "Remote App Agent Return Data Format Error",
                                ZH_CN: u"虚拟应用服务返回数据格式错误"}


#server
ERR_MSG_SERVER_INTERNAL_ERROR = {EN: "Server Internal Error",
                           ZH_CN: u"服务器内部错误"}

# llm
ERR_MSG_LLM_REPLY = {EN: "llm return error",
                     ZH_CN: u"大模型回复错误"}
ERR_MSG_LLM_MODEL_NAME = {EN: "Invalid llm model name",
                          ZH_CN: u"w无效的大模型名称"}