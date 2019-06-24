from flask import render_template
from decorators.login_required import login_required


@login_required
def community_page():
    return render_template('community_page.html')