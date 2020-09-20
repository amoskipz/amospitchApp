from flask import Flask
from flask_bootstrap import Bootstrap

def create_app(config_name):
    app = Flask(__name__)
    
    app.config.from_object(config_options[config_name])