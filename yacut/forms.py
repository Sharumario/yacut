from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, Regexp, URL

from settings import (
    ERROR_UNCORRECT_URL, MAX_ORIGINAL_SIZE, MAX_SHORT_SIZE,
    PATTERN_FOR_SHORT_ID
)


ERROR_MAX_SIZE = f'Длина поля не должна превышать {MAX_SHORT_SIZE} символов.'
ERROR_REQUIRED_FIELD = 'Обязательное поле.'
ERROR_PATTERN_FOR_SHORT_ID = ('Идентификатор может состоять только '
                              'из латинских букв и цифр.')
FIELD_ORIGINAL_LINK = 'Оригинальная длинная ссылка'
FIELD_CUSTOM_ID = 'Ваш вариант короткой ссылки'
FIELD_SUBMIT = 'Добавить'


class URLMapForm(FlaskForm):
    original_link = StringField(
        FIELD_ORIGINAL_LINK,
        validators=(
            DataRequired(message=ERROR_REQUIRED_FIELD),
            Length(max=MAX_ORIGINAL_SIZE, message=ERROR_UNCORRECT_URL),
            URL(message=ERROR_UNCORRECT_URL),
        ),
    )
    custom_id = StringField(
        FIELD_CUSTOM_ID,
        validators=(
            Length(max=MAX_SHORT_SIZE, message=ERROR_MAX_SIZE,),
            Optional(),
            Regexp(PATTERN_FOR_SHORT_ID, message=(
                ERROR_PATTERN_FOR_SHORT_ID),
            ),
        ),
    )
    submit = SubmitField(FIELD_SUBMIT)
