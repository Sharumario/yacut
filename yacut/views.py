from flask import flash, render_template, redirect, url_for

from settings import ERROR_REPEAT_NAME
from yacut import app
from yacut.forms import URLMapForm
from yacut.models import URLMap


@app.route('/', methods=('GET', 'POST'))
def main_view():
    form = URLMapForm()
    if form.validate_on_submit():
        if not form.custom_id.data:
            form.custom_id.data = URLMap.get_unique_short_id()
        if URLMap.check_unique_short_id(form.custom_id.data):
            flash(ERROR_REPEAT_NAME.format(
                custom_id=form.custom_id.data)
            )
            return render_template('main_page.html', form=form)
        urlmap = URLMap(
            original=form.original_link.data,
            short=form.custom_id.data,
        )
        urlmap.save_urlmap()
        return render_template(
            'main_page.html',
            form=form,
            short_link=url_for(
                'redirect_short_url',
                short_id=urlmap.short,
                _external=True
            ),
        )
    return render_template('main_page.html', form=form)


@app.route('/<string:short_id>', methods=['GET'])
def redirect_short_url(short_id):
    return redirect(
        URLMap.query.filter_by(short=short_id).first_or_404().original,
    )
