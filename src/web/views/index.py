from flask import (
    render_template,
    g,
    request,
    redirect,
    url_for
)

from cores.vk import API
from web.forms.search_form import SearchForm


def index():
    form = SearchForm()
    page = render_template('main_page.html', form=form) if g.user else render_template('landing_page.html')

    if request.method == 'POST':
        if form.validate_on_submit():
            data = form.search.data.split('/')

            if len(data) >= 4 and data[3]:
                mask = data[3]

                api = API(access_token=g.user.access_token, v=5.100)
                response = api.utils.resolveScreenName(screen_name=mask)

                if 'type' in response and 'object_id' in response:
                    type = response['type']
                    object_id = response['object_id']

                    if type == 'group':
                        return redirect(url_for('web.albums', community_id=object_id))

        return render_template('main_page.html',
                                   error_message='Простите, но ваша ссылка указана не верно, пожалуйста укажите ссылку правильно.')
    return page
