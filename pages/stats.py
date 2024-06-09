from __main__ import app
from flask import render_template
from data.user import User
from data import db_session
from sqlalchemy import desc


@app.route("/stats")
def stats_page():
    """Обработка статистики"""
    db_sess = db_session.create_session()
    return render_template(
        'stats.html',
        top_users_by_answers=db_sess.query(User).order_by(desc(User.user_count_correctly)).limit(10).all(),
        top_users_by_rating=db_sess.query(User).order_by(desc(User.rating)).limit(10).all(),
    )