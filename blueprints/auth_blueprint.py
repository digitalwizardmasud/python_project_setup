from flask import Flask, Blueprint, request
from utils.resp import error, success
app = Flask(__name__)

auth_bp = Blueprint("auth", __name__, url_prefix='/auth')




@auth_bp.route('/signin', methods=['POST'])
def signin_route():
    pass
  