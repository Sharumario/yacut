from flask import jsonify, request, url_for


from yacut import app
from yacut.error_handlers import (
    raise_thrower, GenarationShortIdError, InvalidAPIUsage
)
from yacut.models import URLMap


ERROR_ID_NOT_FOUND = 'Указанный id не найден'
REQUEST_NO_URL = '"url" является обязательным полем!'
REQUEST_NO_BODY = 'Отсутствует тело запроса'


@app.route('/api/id/', methods=['POST'])
def post_short_url():
    data = request.get_json()
    raise_thrower(not data, REQUEST_NO_BODY)
    raise_thrower('url' not in data, REQUEST_NO_URL)
    try:
        urlmap = URLMap.create_and_validate(
            data.get('url'), data.get('custom_id'), True
        )
    except (GenarationShortIdError, ValueError) as error:
        raise InvalidAPIUsage(str(error))
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
    urlmap = URLMap.get_url_map(short_id)
    raise_thrower(not urlmap, ERROR_ID_NOT_FOUND, error_number=404)
    return jsonify({'url': urlmap.original}), 200
