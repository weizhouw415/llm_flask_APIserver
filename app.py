from flask import Flask, request, render_template, jsonify
import common.constants as Const
from common.error.error import Error
import common.error.error_code as ErrCode
import common.error.error_msg as ErrMsg
from common.log.logger import logger
from request.api_request import api_request
from common.utils import return_error, return_success
# business
from handler import handler
import common.context as context
#from flask_cors import CORS
from dotenv import load_dotenv


app = Flask(__name__)


@app.route(Const.API_ROUTE_TEST, methods=['GET'])
def test():
    req = None
    rep = None
    try:
        req = {"api": Const.API_ROUTE_TEST}
        rep = handler.handle_test(req)
        if isinstance(rep, Error):
            return return_error(req, rep)
        return rep
    except Exception as e:
        logger.error(e)
        rep = Error(req, Error(ErrCode.ERR_CODE_INTERNAL_ERROR, 
                               ErrMsg.ERR_MSG_SERVER_INTERNAL_ERROR))
        return return_error(req, rep)
    
    
@app.route(Const.API_ROUTE_INDEX, methods=['GET'])
def index():
    return render_template("index.html")


@app.route(Const.API_ROUTE_REPLY, methods=['POST'])
def reply():
    req = None
    rep = None
    try:
        req = request.get_json()
        req['api'] = Const.API_ROUTE_REPLY
        ret = api_request(req)
        if isinstance(ret, Error):
            logger.error('%s check parameter error' % req['api'])
            return return_error(req, ret)
        rep = handler.handle_llm_reply(req)
        if isinstance(rep, Error):
            return return_error(req, rep)
        return return_success(req, rep)
    except Exception as e:
        logger.error(e)
        rep = Error(req, Error(ErrCode.ERR_CODE_INTERNAL_ERROR, 
                               ErrMsg.ERR_MSG_SERVER_INTERNAL_ERROR))
        return return_error(req, rep)
    

@app.route(Const.API_ROUTE_TOOLS, methods=['POST'])
def tools():
    req = None
    rep = None
    try:
        req = request.get_json()
        req['api'] = Const.API_ROUTE_TOOLS
        ret = api_request(req)
        if isinstance(ret, Error):
            logger.error('%s check parameter error' % req['api'])
            return return_error(req, ret)
        rep = handler.handel_llm_tools(req)
        if isinstance(rep, Error):
            return return_error(req, rep)
        return return_success(req, rep)
    except Exception as e:
        logger.error(e)
        rep = Error(req, Error(ErrCode.ERR_CODE_INTERNAL_ERROR, 
                               ErrMsg.ERR_MSG_SERVER_INTERNAL_ERROR))
        return return_error(req, rep)
    

if __name__ == '__main__':
    logger.info('=== llm server Start ===')
    # ctx = context.instance()
    # logger.info(ctx.config)
    # logger.info(ctx.host_cache)
    load_dotenv(verbose=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
