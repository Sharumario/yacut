import random
import string
from datetime import datetime

from yacut import db
from settings import MAX_SHORT_SIZE, MAX_RANDOM_SYMBOLS_SIZE


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String, nullable=False)
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

    @classmethod
    def check_unique_short_id(cls, short_id):
        return cls.query.filter_by(short=short_id).first()

    @classmethod
    def get_unique_short_id(cls):
        while True:
            short_id = "".join(
                (random.choice(string.ascii_letters + string.digits)
                 for _ in range(MAX_RANDOM_SYMBOLS_SIZE))
            )
            if cls.check_unique_short_id(short_id) is None:
                break
        return short_id
