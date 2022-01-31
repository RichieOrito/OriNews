from flask import Flask
from config import config_options
from flask_material import Material
# from flask_bootstrap import Bootstrap

material = Material()
# bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    #Create the app configurations.
    app.config.from_object(config_options[config_name])

    #Initializing Material
    material.init_app(app)
    # bootstrap.init_app(app)

    app.static_folder = 'static'

    #Register blueprint.
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .requests import configure_src_request
    configure_src_request(app)

    return app