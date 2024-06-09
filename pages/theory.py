from __main__ import app
from flask import render_template
from data.themes import Themes
from data.theory import Theory
from data import db_session as db
from flask import request

@app.route('/theory', methods=['GET', 'POST'])
def theory_page():
    'Обработка страницы с теорией'
    db_sess = db.create_session()
    if request.method == 'POST':
        name_of_theme = request.form['btn'] # -  получить названия кнопки
        return render_template(
            'theory.html',
            themes=db_sess.query(Themes).all(),
            theory=db_sess.query(Theory).filter(Theory.name == name_of_theme).first(),
        )
    return render_template(
        'theory.html',
        themes=db_sess.query(Themes).all(),
        theory=db_sess.query(Theory).filter(Theory.name == 'Сложение').first()
    )