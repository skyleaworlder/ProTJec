from flask import Blueprint, jsonify
from flask import request, make_response
from ..glovar import *
import traceback
from ..jwt_op import generateJWT

from ..db import read as R

loginBp = Blueprint('login', __name__, url_prefix='/login')

@loginBp.route('', methods=['POST'])
def login():
    try:
        data = request.get_json() # get json
        print("data:", data)
        usr_no = data['no']
        usr_password = data['password']
        pwd_fromDb = R.getPwdByNo(usr_no).records()[0]['password']
        if pwd_fromDb == usr_password:
            info = R.getUsrInfoByNo(usr_no).records()[0]
            role = 'admin' if info['level'] == 0 else 'client'
            print(role)
            response = make_response(jsonify({
                'status': GET_SUCCESS,
                'name': info['name'],
                'level': role,
                'inst': info['inst'],
                'grade': info['grade'],
                'avatar': info['avatar'],
                'document': info['document'],
                'proTJec_token': generateJWT(info)
            }))
            return response
        else:
            return jsonify({
                "status": NAME_PASSWORD_WRONG
            })
    except Exception as e:
        traceback.print_exc()
        return jsonify({
            'status': LOGINOUT_UNKNOWN
        })
