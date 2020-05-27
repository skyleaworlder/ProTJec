from flask import Blueprint, jsonify
from flask import request, make_response
from ..glovar import *
import traceback
from ..jwt_op import generateJWT

from ..db import create as C
from ..db import update as U
from ..db import read as R

infBp = Blueprint('info', __name__, url_prefix='/info')

@infBp.route('update', methods=['POST'])
def updateInfo(**checkrst):
    try:
        data = request.get_json()
        print("checkrst, data: ", checkrst, data)

        if R.checkExistById(data['id'], 'users').size() != 1:
            return jsonify({"status": USER_UNEXIST})

        DR = U.changeUsrInfo(
            data['id'], data['name'], data['no'], data['inst'],
            data['grade'], data['document'], data['chat'], data['avatar']
        )
        if DR.size() != 1:
            return jsonify({"status": INFO_ERROR})
        newInfo_records = DR.records()[0]
        return jsonify({
            "status": INFO_SUCCESS,
            "data": {
                "no": newInfo_records['no'],
                "name": newInfo_records['name'],
                "inst": newInfo_records['inst'],
                "grade": newInfo_records['grade'],
                "document": newInfo_records['document'],
                "chat": newInfo_records['chat'],
                "avatar": newInfo_records['avatar']
            }
        })
    except Exception as e:
        traceback.print_exc()
        return jsonify({"status": INFO_UNKNOWN})


@infBp.route('token', methods=['GET'])
def refreshToken(**checkrst):
    try:
        no = request.args.get('no')
        print("checkrst, no: ", checkrst, no)

        DR1 = R.checkExistByUsrNo(no)
        if DR1.size() != 1:
            return jsonify({"status": USER_UNEXIST})
        usr_id = DR1.records()[0]['id']

        info = R.getUsrInfoByNo(no).records()[0]
        role = 'admin' if info['level'] == 0 else 'client'
        response = make_response(jsonify({
            'status': GET_SUCCESS,
            'proTJec_token': generateJWT(info)
        }))
        return response

    except Exception as e:
        traceback.print_exc()
        return jsonify({"status": INFO_UNKNOWN})


@infBp.route('get', methods=['GET'])
def getBaseInfo(**checkrst):
    try:
        usr_id = request.args.get('id')
        print("checkrst, no", checkrst, usr_id)

        DR1 = R.checkExistById(usr_id, 'users')
        DR2 = R.getUsrInfoById(usr_id)
        if DR1.size() != 1 or DR2.size() != 1:
            return jsonify({"status": USER_UNEXIST})

        info = DR2.records()[0]
        return jsonify({
            "status": GET_SUCCESS,
            "data": {
                "no": info['no'],
                "name": info['name'],
                "grade": info['grade'],
                "inst": info['inst'],
                "avatar": info['avatar'],
                "document": info['document'],
                "chat": info['chat']
            }
        })

    except Exception as e:
        traceback.print_exc()
        return jsonify({"status": INFO_UNKNOWN})