from flask import (
    render_template,
    g,
    request,
    redirect,
    url_for
)
from web.forms.search_form import SearchForm
from utils import convert_url


def index():
    form = SearchForm()
    page = render_template('main_page.html', form=form) if g.user else render_template('landing_page.html')

    if request.method == 'POST':
        if form.validate_on_submit():
            object_id = convert_url(form.search.data)

            if object_id:
                return redirect(url_for('web.albums', community_id=object_id))

        return render_template('main_page.html',
                                   error_message='Простите, но ваша ссылка указана не верно, пожалуйста укажите ссылку правильно.')
    return page
