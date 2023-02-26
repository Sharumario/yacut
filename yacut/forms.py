from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, URL

from settings import (
    MAX_SHORT_SIZE, ERROR_MAX_SIZE, ERROR_UNCORRECT_URL, ERROR_REGEXP,
    ERROR_REQUIRED_FIELD, FIELD_ORIGINAL_LINK, FIELD_CUSTOM_ID, FIELD_SUBMIT,
    REGEXP
)


class URLMapForm(FlaskForm):
    original_link = StringField(
        FIELD_ORIGINAL_LINK,
        validators=(
            DataRequired(message=ERROR_REQUIRED_FIELD),
            URL(message=ERROR_UNCORRECT_URL),
        ),
    )
    custom_id = StringField(
        FIELD_CUSTOM_ID,
        validators=(
            Length(max=MAX_SHORT_SIZE, message=ERROR_MAX_SIZE,),
            Regexp(REGEXP, message=(ERROR_REGEXP),),
        ),
    )
    submit = SubmitField(FIELD_SUBMIT)