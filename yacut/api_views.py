import re

from flask import jsonify, request, url_for

from settings import (
    ERROR_ID_NOT_FOUND, MAX_SHORT_SIZE, REGEXP, REQUEST_NO_BODY,
    REQUEST_NO_URL, REQUEST_UNCORRECT_URL, REQUEST_REPEAT_NAME
)
from yacut import app
from yacut.error_handlers import raise_thrower
from yacut.models import URLMap


@app.route('/api/id/', methods=['POST'])
def post_short_url():
    data = request.get_json()
    raise_thrower(not data, REQUEST_NO_BODY)
    raise_thrower('url' not in data, REQUEST_NO_URL)
    short_id = data.get('custom_id')
    if not short_id:
        short_id = URLMap.get_unique_short_id()
    raise_thrower(
        not re.fullmatch(REGEXP, short_id) or
        len(short_id) > MAX_SHORT_SIZE, REQUEST_UNCORRECT_URL
    )
    raise_thrower(
        URLMap.check_unique_short_id(short_id),
        REQUEST_REPEAT_NAME.format(custom_id=short_id)
    )
    urlmap = URLMap(original=data.get("url"), short=short_id)
    urlmap.save_urlmap()
    return jsonify({
        "url": urlmap.original,
        "short_link": url_for(
            "redirect_short_url",
            short_id=urlmap.short,
            _external=True,
        )
    }), 201


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original_url(short_id):
    urlmap = URLMap.check_unique_short_id(short_id)
    raise_thrower(not urlmap, ERROR_ID_NOT_FOUND, 404)
    return jsonify({"url": urlmap.original}), 200
