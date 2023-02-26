import os
import re
import string


RANDOM_ITERATION_ID = 10
MAX_ORIGINAL_SIZE = 1000
MAX_SHORT_SIZE = 16
MAX_RANDOM_SYMBOLS_SIZE = 6

RANDOM_SYMBOLS = string.ascii_letters + string.digits

ERROR_GET_SHORT_ID = 'Невозможно сгенерировать short_id'
ERROR_ID_NOT_FOUND = 'Указанный id не найден'
ERROR_MAX_SIZE = 'Длина поля не должна превышать 16 символов.'
ERROR_UNCORRECT_URL = 'Некорректный адрес URL.'
ERROR_REGEXP = ('Идентификатор может состоять только '
                'из латинских букв и цифр.')
ERROR_REPEAT_NAME = 'Имя {custom_id} уже занято!'
ERROR_REQUIRED_FIELD = 'Обязательное поле.'
FIELD_ORIGINAL_LINK = 'Оригинальная длинная ссылка'
FIELD_CUSTOM_ID = 'Ваш вариант короткой ссылки'
FIELD_SUBMIT = 'Добавить'
REQUEST_NO_BODY = 'Отсутствует тело запроса'
REQUEST_NO_URL = '"url" является обязательным полем!'
REQUEST_UNCORRECT_URL = 'Указано недопустимое имя для короткой ссылки'
REQUEST_REPEAT_NAME = 'Имя "{custom_id}" уже занято.'

REGEXP = fr'^[{re.escape(RANDOM_SYMBOLS)}]+$'


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URI",
        default="sqlite:///db.sqlite3",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
