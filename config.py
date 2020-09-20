import os

class Config:
     @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    DEBUG = False


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitch_test'

class DevConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig

}
