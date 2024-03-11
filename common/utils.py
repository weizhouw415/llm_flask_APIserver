from common.error.error import Error
import simplejson
from common.constants import DEFAULT_LANG

def json_dump(obj, indent=None):
    try:
        return simplejson.dumps(obj, separators=(',', ':'), indent=indent)
    except Exception:
        return None

def json_load(json):
    if not json:
        return None

    try:
        return simplejson.loads(json, encoding='utf-8')
    except Exception:
        return None

def return_success(req, rep=None, dump=False, **kwargs):
    rep = {} if rep is None else rep
    rep['api'] = req['api']
    rep["ret_code"] = 0
    for k in kwargs:
        rep[k] = kwargs[k]
    if dump:
        return json_dump(rep)
    else:
        return rep


def return_error(req, error, dump=False, **kwargs):
    rep = {}
    rep['api'] = req['api']     # comment this line in production environment
    for k in kwargs:
        rep[k] = rep[k]
    if isinstance(error, Error):
        rep["ret_code"] = error.get_code()
        if isinstance(error.message, str):
            rep["message"] = error.message
        else:
            rep["message"] = error.get_message(DEFAULT_LANG)
    if dump:
        return json_dump(rep)
    else:
        return rep

def is_str(value):
    if not isinstance(value, str):
        return False
    return True

def is_integer(value):
    try:
        _ = int(value)
    except:
        return False
    return True

def is_float(value):
    try:
        _ = float(value)
    except:
        return False
    return True

def to_list(val):
    return list(val) if isinstance(val, (list, tuple, set)) else [val]
