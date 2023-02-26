import random
import re
import urllib.parse
from datetime import datetime

from yacut import db
from yacut.error_handlers import raise_thrower
from settings import (
    ERROR_GET_SHORT_ID, ERROR_UNCORRECT_URL, ERROR_REPEAT_NAME,
    MAX_ORIGINAL_SIZE, MAX_SHORT_SIZE, MAX_RANDOM_SYMBOLS_SIZE, REGEXP,
    RANDOM_ITERATION_ID, RANDOM_SYMBOLS, REQUEST_UNCORRECT_URL,
    REQUEST_REPEAT_NAME
)


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

    def save_urlmap(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_query_elememt(short_id):
        return URLMap.query.filter_by(short=short_id).first()

    @staticmethod
    def get_unique_short_id():
        for _ in range(RANDOM_ITERATION_ID):
            short_id = "".join(
                random.sample(RANDOM_SYMBOLS, MAX_RANDOM_SYMBOLS_SIZE)
            )
            if URLMap.get_query_elememt(short_id) is None:
                return short_id
        raise ValueError(ERROR_GET_SHORT_ID)

    @staticmethod
    def create_and_validate(url, short_id, api=False):
        if api:
            raise_thrower(
                len(url) > MAX_ORIGINAL_SIZE or
                urllib.parse.urlsplit(url).scheme not in ['http', 'https'],
                ERROR_UNCORRECT_URL
            )
        if not short_id:
            short_id = URLMap.get_unique_short_id()
        elif api and short_id:
            raise_thrower(
                len(short_id) > MAX_SHORT_SIZE or
                not re.fullmatch(REGEXP, short_id), REQUEST_UNCORRECT_URL
            )
            raise_thrower(
                URLMap.get_query_elememt(short_id),
                REQUEST_REPEAT_NAME.format(custom_id=short_id)
            )
        else:
            if URLMap.get_query_elememt(short_id):
                raise ValueError(ERROR_REPEAT_NAME.format(custom_id=short_id))
        urlmap = URLMap(original=url, short=short_id)
        urlmap.save_urlmap()
        return urlmap
