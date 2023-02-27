from flask import jsonify, request, url_for


from yacut import app
from yacut.error_handlers import GenarationShortIdError, InvalidAPIUsage
from yacut.models import URLMap


ERROR_ID_NOT_FOUND = 'Указанный id не найден'
REQUEST_NO_URL = '"url" является обязательным полем!'
REQUEST_NO_BODY = 'Отсутствует тело запроса'


@app.route('/api/id/', methods=['POST'])
def post_short_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage(REQUEST_NO_BODY)
    if 'url' not in data:
        raise InvalidAPIUsage(REQUEST_NO_URL)
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
    if not urlmap:
        raise InvalidAPIUsage(ERROR_ID_NOT_FOUND, 404)
    return jsonify({'url': urlmap.original}), 200
