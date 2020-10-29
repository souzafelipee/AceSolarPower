from os import getenv


class Config:
    SECRET_KEY = getenv('SECRET_KEY') or 'uma string randômica e gigante'
    APP_PORT = int(getenv('APP_PORT'))
    DEBUG = eval(getenv('DEBUG').title())
    #POSTGRES_HOST = getenv('POSTGRES_URI')
    from dao import Session


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}


class TestingConfig(Config):
    FLASK_ENV = 'testing'
    TESTING = True
    #MONGODB_HOST = getenv('POSTGRES_URI_TEST')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}