"""
Subscribe manager
"""

import base_common.msg
from base_lookup import api_messages as msgs
from lookup import api_messages as amsgs
from base_common.dbacommon import params
from base_common.dbacommon import app_api_method
from base_common.dbacommon import get_db
from MySQLdb import IntegrityError
from base_common.seq import sequencer

name = "Subscribers"
location = "subscribe"
request_timeout = 10

@app_api_method(
    method='PUT',
    api_return=[(200, 'OK'), (404, '')]
)
@params(
    {'arg': 'project', 'type': str, 'required': True, 'description': 'Project'},
    {'arg': 'email', 'type': str, 'required': True, 'description': 'Email'},
)
def do_put(email,project, **kwargs):
    """
    Save email from subscriber
    """

    _db = get_db()
    dbc = _db.cursor()
    query = "SELECT id FROM subscribers WHERE email='{}'".format(email)
    try:
        dbc.execute(query)
    except IntegrityError as e:
        return base_common.msg.error(msgs.EXECUTE_QUERY_ERROR)

    if dbc.rowcount != 0:
        return base_common.msg.error(amsgs.ALREADY_EXIST)

    id = sequencer().new('b')
    query = "INSERT INTO subscribers (id, email, project) VALUES('{}','{}')".format(id, email, project)
    try:
        dbc.execute(query)
    except IntegrityError as e:
        return base_common.msg.error(msgs.EXECUTE_QUERY_ERROR)

    _db.commit()

    return base_common.msg.put_ok()