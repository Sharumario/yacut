from flask import abort, flash, render_template, redirect, url_for

from yacut import app
from yacut.error_handlers import GenarationShortIdError
from yacut.forms import URLMapForm
from yacut.models import URLMap


@app.route('/', methods=('GET', 'POST'))
def main_view():
    form = URLMapForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    try:
        urlmap = URLMap.create_and_validate(
            form.original_link.data, form.custom_id.data
        )
    except (GenarationShortIdError, ValueError) as error:
        flash(error)
        return render_template('index.html', form=form)
    return render_template(
        'index.html',
        form=form,
        short_link=url_for(
            'redirect_short_url',
            short_id=urlmap.short,
            _external=True
        ),
    )


@app.route('/<string:short_id>', methods=['GET'])
def redirect_short_url(short_id):
    urlmap = URLMap.get_url_map(short_id)
    if urlmap is None:
        abort(404)
    return redirect(urlmap.original)
