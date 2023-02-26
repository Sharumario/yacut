import os


MAX_SHORT_SIZE = 16
MAX_RANDOM_SYMBOLS_SIZE = 6

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

REGEXP = r'^[a-zA-Z0-9]*$'


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
