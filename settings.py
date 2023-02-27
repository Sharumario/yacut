import os
import re
import string


MAX_ORIGINAL_SIZE = 2048
MAX_SHORT_SIZE = 16
MAX_RANDOM_SYMBOLS_SIZE = 6
RANDOM_ITERATION_ID = 10

RANDOM_SYMBOLS = string.ascii_letters + string.digits

ERROR_UNCORRECT_URL = 'Некорректный адрес URL.'

PATTERN_FOR_SHORT_ID = fr'^[{re.escape(RANDOM_SYMBOLS)}]+$'


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URI",
        default="sqlite:///db.sqlite3",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
