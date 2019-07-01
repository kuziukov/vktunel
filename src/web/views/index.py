from flask import render_template, g


def index():
    page = 'main_page.html' if g.user else 'landing_page.html'
    return render_template(page)
