"""
Email manager
"""

import base_common.msg
from base_lookup import api_messages as msgs
from base_common.dbacommon import params
from base_common.dbacommon import app_api_method
from base_svc.comm import BaseAPIRequestHandler
from base_config.service import support_mail
import json
import base_api.hash2params.save_hash
import base_api.mail_api.save_mail

name = "Send email"
location = "contact"
request_timeout = 10


def get_message(data, email, mailmsg, web):

    data = json.loads(data)

    emessage = ''
    receiver = ''
    sender = email
    if web == "mojlet":
            receiver = ''
            emessage += 'Sender name : ' + data['firstName'] + data['lastName'] + ' </br>'
            emessage += 'Sender phone : ' + data['phone'] + ' </br>'
            emessage += 'Sender email : ' + email + ' </br>'

    if web == "digitalcube":
        import re
        #sender = 'mladen@digitalcube.rs'
        subject = 'Digital Cube d.o.o. web'
        receiver = 'mladen@digitalcube.rs'
        rpl={'#email#':email,'#name#':data['name'],'#des#': mailmsg}
        print(rpl)
        with open('/home/www/work/eContact/tpl-dcube1.html','r') as f:
           s=f.read()
           for key in rpl.keys():
              s = re.sub( key, rpl[key], s )
           
           emessage = s
           print(s)   
    print(emessage)                                                 
    print(sender+' '+receiver+' '+emessage)
    return subject, sender, receiver, emessage

@app_api_method(
    method='PUT',
)
@params(
    {'arg': 'data', 'type': json, 'required': True, 'description': 'Data'},
    {'arg': 'email', 'type': str, 'required': True, 'description': 'Email'},
    {'arg': 'mailmsg', 'type': str, 'required': False, 'description': 'Message'},
    {'arg': 'web', 'type': str, 'required': True, 'description': 'Name of website'},
)
def do_put(data, email, mailmsg, web, *args, **kwargs):

    """
    Save email for sending
    """
    print(data+' '+email+' '+mailmsg)

    subject, sender, receiver, emessage = get_message(data,email,mailmsg,web)
    # print(sender,receiver,message)
    # SAVE EMAIL FOR SENDING
    # subj = 'Email from digitalcube'
    # rh1 = BaseAPIRequestHandler()
    # rh1.set_argument('sender', sender)
    # rh1.set_argument('receiver', receiver)
    # rh1.set_argument('message', emessage)
    # rh1.set_argument('subject',subj)
    # kwargs['request_handler'] = rh1

    # SAVE EMAILS FOR SENDING
    rh1 = BaseAPIRequestHandler()
    rh1.set_argument('sender', 'mladen@digitalcube.rs')
    rh1.set_argument('receiver', 'mladen@digitalcube.rs')
    rh1.set_argument('subject', subject)
    rh1.set_argument('message', email + '   ' +mailmsg)
    rh1.set_argument('data',data)
    kwargs['request_handler'] = rh1
    res = base_api.mail_api.save_mail.do_put(email, **kwargs)
    if 'http_status' not in res or res['http_status'] != 204:
            return base_common.msg.error('Something wrong')

    # res = base_api.mail_api.save_mail.do_put(sender, receiver, emessage, *args, **kwargs)
    # if 'http_status' not in res or res['http_status'] != 204:
    #     return base_common.msg.error('Something wrong')

    return base_common.msg.post_ok(msgs.OK)
