from flask import Blueprint, jsonify
from flask import request, make_response
from ..glovar import *
import traceback
from ..jwt_op import generateJWT

from ..db import create as C

prfBp = Blueprint('profile', __name__, url_prefix='/profile')

prfBp.route('/signup', methods=['POST'])
def signUp(**checkrst):
    try:
        data = request.get_json()
        usr_no = data['no']
        usr_password = data['pwd']
        usr_name = data['name']
        usr_userlevel = data['level']
        usr_inst = data['inst']
        usr_avatar = data['avatar']
        DR_record = C.userInfoInsert(
            usr_no, usr_password, usr_name, usr_userlevel,
            usr_inst, usr_grade, usr_avatar
        ).records()[0]
        if DR_record['id'] and DR_record['no'] == usr_no:
            return jsonify({
                "status": SET_SUCCESS,
                "no": usr_no
            })
        else:
            return jsonify({"status": SET_FAILED})
    except Exception as e:
        traceback.print_exc()
        return jsonify({"status": SET_FAILED})