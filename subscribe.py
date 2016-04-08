"""
Email manager
"""

import base_common.msg
from base_lookup import api_messages as msgs
from base_common.dbacommon import params
from base_common.dbacommon import app_api_method
from base_common.dbcommon import get_db
from MySQLdb import IntegrityError
from base_common.seq import sequencer

name = "Send email"
location = "subscribe"
request_timeout = 10

@app_api_method(
    method='PUT',
    api_return=[(200, 'OK'), (404, '')]
)
@params(
    {'arg': 'email', 'type': str, 'required': True, 'description': 'Guest email'},
)
def do_put(email, *args, **kwargs):
    """
    Save email for subscriber
    """

    _db = get_db()
    dbc = _db.cursor()
    query = "SELECT email FROM subscribers WHERE email={}".format(email)
    try:
        row = dbc.execute(query)
    except IntegrityError as e:
        return base_common.msg.error(msgs.EXECUTE_QUERY_ERROR)

    if row.count != 0:
        return base_common.msg.error(msgs.ALREADY_EXIST)

    id = sequencer().new('b')
    query = "INSERT INTO subscribers id, email VALUES('{}','{}')".format(id, email)
    try:
        row = dbc.execute(query)
    except IntegrityError as e:
        return  base_common.msg.error(msgs.EXECUTE_QUERY_ERROR)

    dbc.commit()

    return base_common.msg.put_ok(msgs.OK)