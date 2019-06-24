from flask import render_template
from decorators.login_required import login_required


@login_required
def task_page():
    return render_template('task_page.html')