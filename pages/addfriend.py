from __main__ import app
from flask import render_template
from flask_login import current_user


@app.route("/addfriend")
def addfriend_page():
    """Обработка личного кабинета"""
    return render_template(
        'addfriend.html',
        user=current_user,
        round=round
    )