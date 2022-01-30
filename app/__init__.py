from flask import Flask
from config import config_options
from flask_material import Material

def create_app(config_name):
    app = Flask(__name__)

    # setting config
    from .requests import configure_src_request
    configure_src_request(app)