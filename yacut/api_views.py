from flask import jsonify, request, url_for

from settings import (
    ERROR_ID_NOT_FOUND, REQUEST_NO_BODY,
    REQUEST_NO_URL
)
from yacut import app
from yacut.error_handlers import raise_thrower, InvalidAPIUsage
from yacut.models import URLMap


@app.route('/api/id/', methods=['POST'])
def post_short_url():
    data = request.get_json()
    raise_thrower(not data, REQUEST_NO_BODY)
    raise_thrower('url' not in data, REQUEST_NO_URL)
    try:
        urlmap = URLMap.create_and_validate(
            data.get('url'), data.get('custom_id'), True
        )
    except ValueError as error:
        raise InvalidAPIUsage(error)
    return jsonify({
        'url': urlmap.original,
        'short_link': url_for(
            'redirect_short_url',
            short_id=urlmap.short,
            _external=True,
        )
    }), 201


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original_url(short_id):
    urlmap = URLMap.get_query_elememt(short_id)
    raise_thrower(not urlmap, ERROR_ID_NOT_FOUND, 404)
    return jsonify({'url': urlmap.original}), 200
