"""
Email manager
"""

import base_common.msg
from base_lookup import api_messages as msgs
from base_common.dbacommon import params
from base_common.dbacommon import app_api_method
from base_svc.comm import BaseAPIRequestHandler
from base_config.service import support_mail

import base_api.hash2params.save_hash
import base_api.mail_api.save_mail


name = "Send email"
location = "contact"
request_timeout = 10


def get_email_message(name,email,mailmsg):

    m = """Mail send from {},<br/> with email: {}<br/><br/>Message: <br/>{}""".format(
            email,
            name,
            mailmsg
            )

    return m


@app_api_method(
    method='PUT',
    #api_return=[(200, 'OK'), (404, '')]
)
@params(
    {'arg': 'email', 'type': str, 'required': True, 'description': 'Guest email'},
    {'arg': 'name', 'type': str, 'required': True, 'description': 'Guest name'},
    {'arg': 'mailmsg', 'type': str, 'required': True, 'description': 'Guest message'},
)
def do_put(email, name, mailmsg, *args, **kwargs):
    """
    Save email for sending
    """
    message = get_email_message(email, name, mailmsg)
    support_mail = 'milicevicdj@gmail.com'
    # SAVE EMAIL FOR SENDING
    rh1 = BaseAPIRequestHandler()
    rh1.set_argument('sender', email)
    rh1.set_argument('receiver', support_mail)
    rh1.set_argument('message', message)
    kwargs['request_handler'] = rh1
    res = base_api.mail_api.save_mail.do_put(email, support_mail,message, **kwargs)
    if 'http_status' not in res or res['http_status'] != 204:
        return base_common.msg.error('Error sending message')

    return base_common.msg.post_ok(msgs.OK)
