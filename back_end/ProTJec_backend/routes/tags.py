from flask import Blueprint, jsonify
from flask import request, make_response
from ..glovar import *
import traceback

from ..db import read as R
from ..db import create as C

tagBp = Blueprint("tags", __name__, url_prefix='/tags')

@tagBp.route('', methods=['GET'])
def getAllTags(**checkrst):
    try:
        DR1 = R.getTags()
        if DR1.size() == 0:
            return jsonify({"status": TAG_FAILED})
        return jsonify({
            "status": GET_SUCCESS,
            "data": {
                "tags": DR1.records()
            }
        })
    except Exception as e:
        traceback.print_exc()
        return jsonify({"status": TAG_UNKNOWN})
