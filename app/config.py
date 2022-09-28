import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


class Config:
    JSON_AS_ASCII = False
    DEBUG = True


config = Config()
