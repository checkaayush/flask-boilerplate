from flask import Blueprint, jsonify


api = Blueprint('api', __name__)


@api.route('/', methods=['GET'])
@api.route('/health', methods=['GET'])
def ping():
    return jsonify(message='OK')
