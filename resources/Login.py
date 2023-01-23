from flask_restful import Resource
from flask import request, jsonify
from config import conn , app
import datetime
import jwt
from werkzeug.security import check_password_hash
class Login(Resource):
    def post(self):

        auth = request.get_json()
        email = auth.get('email')
        password = auth.get('password')

        if not email or not password:
            return 'no username or pass',400
        cur = conn.cursor()
        cur.execute("SELECT uid,password from users WHERE email = (%s);",(email,))
        resp = cur.fetchone()
        cur.close()
        # print(resp)
        if resp:
            _uid = resp[0]
            _pass = resp[1]

            if check_password_hash(_pass,password):

                resp = {
                    'tokenType': "Bearer"
                }
                token = jwt.encode({'uid':_uid,'exp':datetime.datetime.now()+datetime.timedelta(1)},app.config['SECRET_KEY'])
                resp['expiresIN'] = 1440
                resp['authState'] = _uid
                resp['token'] = token
                print('success')
                return jsonify(resp)
            pass