from flask import Blueprint, jsonify
from flask import request, make_response
import datetime
from ..glovar import *
import traceback
from ..jwt_op import generateJWT

from ..db import read as R
from ..db import create as C
from ..db import delete as D

proBp = Blueprint("projects", __name__, url_prefix="/projects")

@proBp.route('/fetch', methods=['GET'])
def proFecth(**checkrst):
    try:
        print("checkrst:", checkrst)
        # args gain from response are string type
        limit = int(request.args.get('limit'))
        page = int(request.args.get('page'))
        initiatorId = None
        if request.args.get('initiatorId') is not None:
            initiatorId = int(request.args.get('initiatorId'))

        DR1 = R.getAllProInfo(limit, page, state=0, initiatorId=initiatorId)
        DR2 = R.getAllProInfo(state=0, initiatorId=initiatorId)

        if DR1.size() == 0 or DR2.size() == 0:
            return jsonify({"status": PROJ_UNEXIST})
        pro = DR1.records()
        cnt = DR2.size()
        print(pro, limit, page, cnt)

        return jsonify({
            "status": GET_SUCCESS,
            "data": {
                "projects": pro,
                "total": cnt
            }
        })
    except Exception as e:
        traceback.print_exc()
        return jsonify({
            "status": PROJ_UNKNOWN
        })


@proBp.route('/add', methods=['POST'])
def proAdd(**checkrst):
    try:
        print("checkrst:", checkrst)
        data = request.get_json()
        print(data)
        usr_id = data['usr_id']
        name = data['name']
        sort = data['sort']
        endTime = data['endTime']
        need = data['need']
        intro = data['intro']
        releaseTime = datetime.datetime.now().replace(microsecond=0)
        endTime = datetime.datetime.now().strptime(endTime, '%Y-%m-%d %H:%M:%S')
        tags = data['tags']
        print(releaseTime, endTime, tags)

        # first: process base info of project
        DR1 = C.proAdd(usr_id, name, sort, releaseTime,endTime, need, intro)
        if DR1.size() != 1:
            return jsonify({"status": PROJ_UNKNOWN})

        # second: append tags upon process, using pro_tag table
        pro_id = DR1.records()[0]['id']
        for tag in tags:
            DR2 = C.addTagsOfPro(pro_id, tag['id'])
            if DR2.size() != 1:
                return jsonify({"status": PROJ_UNKNOWN})

        return jsonify({"status": PROJ_SUCCESS})
    except Exception as e:
        traceback.print_exc()
        return jsonify({"status": PROJ_UNKNOWN})


@proBp.route('/info', methods=['GET'])
def proGetInfo(**checkrst):
    try:
        print("checkrst:", checkrst)
        id = int(request.args.get('id'))
        # 获得项目的所有信息
        pro = R.getProInfoById(id)
        if pro.size() != 1:
            return jsonify({"status": PROJ_UNEXIST})
        pro_records = pro.records()[0]

        # 获得首倡者的所有信息
        initiator = R.getInitiatorInfoByProId(id)
        if initiator.size() != 1:
            return jsonify({"status": PROJ_UNEXIST})
        initiator_records = initiator.records()

        # 获得响应者的所有信息
        responders = R.getRespondersInfoByProId(id)
        responders_records = responders.records()

        # 获得项目的所有tag
        tags = R.getProTagsByProId(id)
        tags_records = []
        if tags.size() != 0:
            tags_records = tags.records()

        return jsonify({
            "status": PROJ_SUCCESS,
            "data": {
                "name": pro_records['name'],
                "initiator": initiator_records,
                "responder": responders_records,
                "sort": pro_records['sort'],
                "releaseTime": pro_records['releaseTime'],
                "endTime": pro_records['endTime'],
                "need": pro_records['need'],
                "intro": pro_records['intro'],
                "tags": tags_records
            }
        })
    except Exception as e:
        traceback.print_exc()
        return jsonify({"status": PROJ_UNKNOWN})



@proBp.route('/requestUsers', methods=['GET'])
def proRequestUsrShowById(**checkrst):
    try:
        pro_id = request.args.get('pro_id')
        DR1 = R.checkExistById(pro_id, 'projects')
        if DR1.size() == 0:
            return jsonify({"status": PROJ_UNEXIST})

        DR2 = R.getReqUsrInfoByProId(pro_id)
        request_records = DR2.records()
        return jsonify({
            "status": GET_SUCCESS,
            "data": request_records
        })
    except Exception as e:
        traceback.print_exc()
        return jsonify({"status": REQ_UNKNOWN})