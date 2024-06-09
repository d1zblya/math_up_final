from __main__ import app
from flask import render_template
from flask_login import current_user


@app.route("/lcab")
def lcab_page():
    """Обработка личного кабинета"""
    return render_template(
        'lcab.html',
        user=current_user,
        round=round
    )
