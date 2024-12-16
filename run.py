from flask import has_request_context
from app import app
from flask_cors import CORS


# from utils.custom_logger import *
app.config['MAX_CONTENT_LENGTH']= 50*1024*1024
CORS(app)



if __name__ == "__main__":
    app.run(port=5000)