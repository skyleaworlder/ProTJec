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
