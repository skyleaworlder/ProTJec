from flask import Blueprint, jsonify
from flask import request, make_response
from ..glovar import *
import traceback
from ..jwt_op import generateJWT
import datetime

from ..db import read as R
from ..db import create as C

loginBp = Blueprint('login', __name__, url_prefix='/login')

@loginBp.route('', methods=['POST'])
def login():
    try:
        data = request.get_json() # get json
        print("data:", data)
        usr_no = data['no']
        usr_password = data['password']
        DR0 = R.checkExistByUsrNo(usr_no)
        DR1 = R.getPwdByNo(usr_no)
        if DR1.size() != 1 or DR0.size() != 1:
            return jsonify({"status": NAME_PASSWORD_WRONG})

        pwd_fromDb = DR1.records()[0]['password']
        if pwd_fromDb != usr_password:
            return jsonify({"status": NAME_PASSWORD_WRONG})
        else:
            info = R.getUsrInfoByNo(usr_no).records()[0]
            # set role
            role = 'admin' if info['level'] == 0 else 'client'

            # loginLogs insert preparation
            usr_id = info['id']
            lgi_time = datetime.datetime.now().replace(microsecond=0)
            DR2 = C.addLoginLogs(lgi_time, usr_id)

            if DR2.size() != 1:
                return jsonify({"status": LOGIN_UNKNOWN})
            # print(role)
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
    except Exception as e:
        traceback.print_exc()
        return jsonify({
            'status': LOGIN_UNKNOWN
        })
