
tests_included = [
    'echo_put_test',
]

import base_lookup.api_messages as amsgs
from base_config.settings import APP_PREFIX
from base_tests.tests_common import test, WarningLevel, log_info

def echo_put_test(svc_port):
    log_info("Contact Put test", '', None)

    import contact
    loc = '{}/{}'.format(APP_PREFIX, contact.location)



