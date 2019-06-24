from flask import render_template
from decorators.login_required import login_required


@login_required
def album_page():
    return render_template('album_page.html')