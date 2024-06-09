from __main__ import app
from flask import render_template, redirect
from random import randint
from flask import request, session
from data import db_session
from data.solve import Solve
from data.user import User
import time
from flask_login import current_user, AnonymousUserMixin


@app.route("/solve/<dif>", methods=['GET', 'POST'])
def solves_page(dif):
    """Обработка страницы с решением примеров"""
    db_sess = db_session.create_session()
    # обработчик ответов пользователя
    answer = 0
    if request.method == 'POST':
        tr_answer = session.get('tr_answer')
        text = session.get('task_text')
        if str(request.form['ans']) == str(tr_answer):  # session.get('tr_answer') - request.form['ans'] == tr_answer
            if not isinstance(current_user, AnonymousUserMixin):
                user = db_sess.query(User).filter(User.email == current_user.email).first()
                if user:
                    user.rating += 10
                    user.user_count_correctly += 1
                    user.user_count_tasks += 1
                    db_sess.commit()
            answer = ('Правильно', 1, request.form['ans'])
            return render_template(
                'solve.html',
                dif=dif,
                answer=answer,
                example=text
            )
        else:
            if not isinstance(current_user, AnonymousUserMixin):
                user = db_sess.query(User).filter(User.email == current_user.email).first()
                if user:
                    user.user_count_tasks += 1
                    db_sess.commit()
            answer = (f'Неправильно,\nПравильный ответ: {tr_answer}', 0, request.form['ans'])
            return render_template(
                'solve.html',
                dif=dif,
                answer=answer,
                example=text
            )

    if dif == 'easy':
        task = db_sess.query(Solve).filter(Solve.id == randint(1, 30)).first()
        example = task.easy
        session['tr_answer'] = task.easy_sol
        session['task_text'] = task.easy
        return render_template(
            'solve.html',
            dif=dif,
            example=example
        )
    elif dif == 'medium':
        task = db_sess.query(Solve).filter(Solve.id == randint(1, 30)).first()
        example = task.medium
        session['tr_answer'] = task.medium_sol
        session['task_text'] = task.medium
        return render_template(
            'solve.html',
            dif=dif,
            example=example
        )
    elif dif == 'hard':
        task = db_sess.query(Solve).filter(Solve.id == randint(1, 30)).first()
        example = task.hard
        session['tr_answer'] = task.hard_sol
        session['task_text'] = task.hard
        return render_template(
            'solve.html',
            dif=dif,
            example=example
        )
    return render_template(
        'solve.html',
        dif=dif,
        answer=answer
    )

