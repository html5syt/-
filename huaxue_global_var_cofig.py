#copy from http://t.zoukankan.com/wulixia-p-14942434.html
def var_init():
    """初始化"""
    global GLOBALS_DICT
    GLOBALS_DICT = {}


def set_var(name, value):
    """设置"""
    try:
        GLOBALS_DICT[name] = value
        return True
    except KeyError:
        return False


def get_var(name):
    """取值"""
    try:
        return GLOBALS_DICT[name]
    except KeyError:
        return "Not Found"