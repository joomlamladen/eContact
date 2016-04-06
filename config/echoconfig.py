
from collections import namedtuple
DbConfig = namedtuple('DbConfig', 'db, host, user, passwd, charset')
db_config = DbConfig('dcube', 'localhost', 'tms', '123', 'utf8')
