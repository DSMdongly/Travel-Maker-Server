from config import Config


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'postgres://localhost:5432/travel_maker_dev?user=postgres&password=ehdgus0608'


