from flask import Blueprint, jsonify
from flask import request, make_response
import datetime
from ..glovar import *
import traceback

from ..db import read as R
from ..db import update as U

rspBp = Blueprint('response', __name__, url_prefix='/response')

@rspBp.route('/fetch', methods=['GET'])
def getAllResponseInfo(**checkrst):
    usr_id = request.args.get('usr_id')
    limit = request.args.get('limit')
    page = request.args.get('page')


@rspBp.route('/changeState', methods=['POST'])
def changeResState(**checkrst):
    data = request.get_json()
    usr_id = data['usr_id']
    pro_id = data['pro_id']
    state = data['state']

    DR1 = R.checkExistById(usr_id, 'users')
    DR2 = R.checkExistById(pro_id, 'projects')
    if DR1.size() != 1:
        return jsonify({"status": USER_UNEXIST})
    if DR2.size() != 1:
        return jsonify({"status": PROJ_UNEXIST})

    DR3 = U.changeRspState(usr_id, pro_id, state)
    if DR3.size() != 1:
        return jsonify({"status": RSP_ERROR})

    records = DR3.records()[0]

    return jsonify({
        "status": RSP_SUCCESS,
        "data": {
            "state": records['state']
        }
    })