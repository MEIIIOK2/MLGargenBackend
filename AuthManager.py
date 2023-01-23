from flask import request, jsonify
from functools import wraps
from config import conn,app
import jwt


def require_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token:
            decoded = jwt.decode(token.split(' ')[1], app.config['SECRET_KEY'], "HS256")
            try:
                cur = conn.cursor()
                cur.execute("SELECT count(*) FROM users where uid=(%s);", (decoded['uid'],))
                resp = cur.fetchone()
                cur.close()
                if resp[0] == 0:
                    return jsonify('User not found')
                return f(uid=decoded['uid'], *args, **kwargs)
            except BaseException as e:
                print(e.args)
                conn.rollback()
        else:
            return jsonify('Not Authorized')
    return wrapper
