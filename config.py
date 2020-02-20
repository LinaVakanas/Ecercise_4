"""Flask config class"""
from os.path import dirname, abspath, join


class Config(object):
    """Set Flask base configuration"""
    CSRF_ENABLED = True
    SECRET_KEY = '93b35eaab44cb731d5ea79c9032f4d71f3d4510b9e72'

    #General Config
    DEBUG = False
    TESTING = False

    #Forms config
    WTF_CSRF_SECRET_KEY = 'AD_oTq4fD5vANxK27Gblj_cSXmbOS4vMUXb2P_YhzbU'

    # Database config
    CWD = dirname(abspath(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+join(CWD, 'rain_sqlite.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductConfig(Config):
    """Set configuration for the production/live environment"""
    DEBUG = False
    TESTING = False


class TestConfig(Config):
    """Set configuration for the test environment"""
    TESTING = True
    SQLALCHEMY_DATABSE_URI = 'sqlite:///:memory:'


class DevConfig(Config):
    DEBUG = True
