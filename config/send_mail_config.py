#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from logging.handlers import TimedRotatingFileHandler

log_filename = "/var/log/base/send_mail.log"
log_handler = TimedRotatingFileHandler(log_filename, when="midnight")
log_formatter = logging.Formatter(
    '%(asctime)-6s %(name)s %(module)s %(funcName)s %(lineno)d - %(levelname)s %(message)s')
log_handler.setFormatter(log_formatter)

log = logging.getLogger('DGTL')
log.propagate = False
log.addHandler(log_handler)
log.setLevel(logging.DEBUG)
_log = "DGTL"

db_host = 'localhost'
db_user = 'eeeecon'
db_passwd = '1212123'
db_name = 'dcubeeee'  # Promenjeno za potrebe TESTA
db_charset = 'utf8'

sg_key = ''

REDIS_SERVER = 'localhost'
REDIS_PORT = 6379
SVC_PORT = 9885

