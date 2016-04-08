
from collections import namedtuple
DbConfig = namedtuple('DbConfig', 'db, host, user, passwd, charset')
db_config = DbConfig('dcube', 'localhost', 'econ', '123', 'utf8')
