from os import getenv


class Config:
    SECRET_KEY = getenv('SECRET_KEY') or 'uma string randômica e gigante'
    PORT = int(getenv('PORT'))
    DEBUG = eval(getenv('DEBUG').title())
    #POSTGRES_HOST = getenv('POSTGRES_URI')
    from dao import Session


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True


class ProductionConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
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