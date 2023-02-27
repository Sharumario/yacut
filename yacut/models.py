import random
import re
import urllib.parse
from datetime import datetime

from yacut import db
from yacut.error_handlers import GenarationShortIdError, raise_thrower
from settings import (
    ERROR_UNCORRECT_URL, MAX_ORIGINAL_SIZE, MAX_SHORT_SIZE,
    MAX_RANDOM_SYMBOLS_SIZE, PATTERN_FOR_SHORT_ID, RANDOM_ITERATION_ID,
    RANDOM_SYMBOLS
)


ERROR_GET_SHORT_ID = 'Невозможно сгенерировать short_id'
ERROR_REPEAT_NAME = 'Имя {custom_id} уже занято!'
REQUEST_UNCORRECT_URL = 'Указано недопустимое имя для короткой ссылки'
REQUEST_REPEAT_NAME = 'Имя "{custom_id}" уже занято.'


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_ORIGINAL_SIZE), nullable=False)
    short = db.Column(
        db.String(MAX_SHORT_SIZE),
        nullable=False,
        unique=True,
        index=True
    )
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    @staticmethod
    def get_url_map(short_id):
        return URLMap.query.filter_by(short=short_id).first()

    @staticmethod
    def get_unique_short_id():
        for _ in range(RANDOM_ITERATION_ID):
            short_id = "".join(
                random.sample(RANDOM_SYMBOLS, MAX_RANDOM_SYMBOLS_SIZE)
            )
            if URLMap.get_url_map(short_id) is None:
                return short_id
        raise GenarationShortIdError(ERROR_GET_SHORT_ID)

    @staticmethod
    def create_and_validate(url, short_id, validate=False):
        if validate:
            raise_thrower(
                len(url) > MAX_ORIGINAL_SIZE or
                urllib.parse.urlsplit(url).scheme not in ['http', 'https'],
                ERROR_UNCORRECT_URL,
                throw='ValueError'
            )
        if not short_id:
            short_id = URLMap.get_unique_short_id()
        elif validate and short_id:
            raise_thrower(
                len(short_id) > MAX_SHORT_SIZE or not re.fullmatch(
                    PATTERN_FOR_SHORT_ID, short_id
                ),
                REQUEST_UNCORRECT_URL,
                throw='ValueError'
            )
            raise_thrower(
                URLMap.get_url_map(short_id),
                REQUEST_REPEAT_NAME.format(custom_id=short_id),
                throw='ValueError'
            )
        raise_thrower(
            URLMap.get_url_map(short_id),
            ERROR_REPEAT_NAME.format(custom_id=short_id),
            throw='ValueError'
        )
        urlmap = URLMap(original=url, short=short_id)
        db.session.add(urlmap)
        db.session.commit()
        return urlmap
