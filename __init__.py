
APP_NAME = 'econtact'
PREFIX = 'econtact'
IMPORTS = [
    'contact',
    'subscribe'
]
SHOW_SPECS = True
DB_CONF = '{}.config.echoconfig'.format(APP_NAME)
SVC_PORT = 9885
TESTS = 'tests'
BASE_TEST = True
MSG_LOOKUP = 'lookup.api_messages'
APP_VERSION = '0.0.1'
# APP_HOOKS = 'apphooks'
# LB = False    # True for load balancer application
# BALANCE = ['127.0.0.1:{}'.format(7700+x) for x in range(40)] # balance server address list
