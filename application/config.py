import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """base config"""


class ProductionConfig(Config):
    """prod config"""


class DevelopmentConfig(Config):
    """dev config"""


class TestingConfig(Config):
    TESTING = True
