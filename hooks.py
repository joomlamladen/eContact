
from config import send_mail_config

hooks = [

    "get_params",
]

def get_params():

    res = {}

    res['db_host'] = send_mail_config.db_host
    res['db_user'] = send_mail_config.db_user
    res['db_passwd'] = send_mail_config.db_passwd
    res['db_name'] = send_mail_config.db_name
    res['db_charset'] = send_mail_config.db_charset
    res['sg_key'] = send_mail_config.sg_key
    res['REDIS_SERVER'] = send_mail_config.REDIS_SERVER
    res['REDIS_PORT'] = send_mail_config.REDIS_PORT
    res['send_mail_log'] = send_mail_config.log_filename
    res['_log'] = send_mail_config._log


    return res

