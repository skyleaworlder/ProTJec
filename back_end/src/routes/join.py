from flask import Blueprint, jsonify
from flask import request, make_response
import datetime
from ..glovar import *
import traceback
from ..jwt_op import generateJWT

from ..db import create as C
from ..db import update as U
from ..db import read as R

joinBp = Blueprint('join', __name__, url_prefix='/join')


@joinBp.route('agree', methods=['POST'])
def agreeJoin(**checkrst):
    try:
        data = request.get_json()
        usr_id = data['usr_id']
        pro_id = data['pro_id']
        state = data['state']
        print("checkrst:", checkrst, data)

        # check user and project exist
        if R.checkExistById(usr_id, 'users').size() != 1:
            return jsonify({"status": USER_UNEXIST})
        if R.checkExistById(pro_id, 'projects').size() != 1:
            return jsonify({"status": PROJ_UNEXIST})
        if R.checkResExistByIds(usr_id, pro_id).size() != 1:
            return jsonify({"status": REQ_UNEXIST})

        DR1 = C.capAgreeJoin(usr_id, pro_id)
        DR2 = U.proNeedDecrease(pro_id)
        DR3 = U.changeRspState(usr_id, pro_id, state)

        if DR1.size() != 1 and DR2.size() != 1 and DR3.size() != 1:
            return jsonify({"status": JOIN_ERROR})
        if DR2.records()[0]['need'] == 0:
            U.changeProState(pro_id, '3')

        return jsonify({
            "status": JOIN_SUCCESS
        })
    except Exception as e:
        traceback.print_exc()
        return jsonify({"status": JOIN_UNKNOWN})


@joinBp.route('pro', methods=['POST'])
def joinPro(**checkrst):
    try:
        data = request.get_json()
        usr_id = data['usr_id']
        pro_id = data['pro_id']
        time = datetime.datetime.now().replace(microsecond=0)
        state = 'W' # means waiting for agreeing
        print("checkrst:", checkrst, data, time)

        # check user and project exist
        if R.checkExistById(usr_id, 'users').size() != 1:
            return jsonify({"status": USER_UNEXIST})
        if R.checkExistById(pro_id, 'projects').size() != 1:
            return jsonify({"status": PROJ_UNEXIST})
        if R.checkResExistByIds(usr_id, pro_id).size() != 0:
            return jsonify({"status": REQ_EXIST})

        DR1 = C.attemptJoin(time, state, usr_id, pro_id)
        if DR1.size() != 1:
            return jsonify({"status": REQ_ERROR})

        return jsonify({
            "status": REQ_SUCCESS
        })
    except Exception as e:
        traceback.print_exc()
        return jsonify({"status": REQ_UNKNOWN})
