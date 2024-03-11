import requests
import common.constants as Const
from common.log.logger import logger
from common.utils import json_load

def send_post_request(url, req):
    rep = None
    try:
        rep = requests.post(url, json=req, timeout=Const.REQUEST_TIMEOUT)
        if rep.status_code == 200:
            return json_load(rep.text)
    except Exception as e:
        logger.error(e)
        return None

def send_get_request(req):
    pass