from __main__ import app
from flask import render_template
from models.generator import (
    MathProblemGenerator, 
    difficult_div,
    difficult_mul,
    difficult_sub,
    difficult_sum
)
from flask import session
from flask import request
from flask_login import current_user, AnonymousUserMixin
from data import db_session
from data.user import User


@app.route("/quests/<type>", methods=['GET', 'POST'])
def quests_page(type):
    """Обработка квестов"""
    answer = 0
    
    gen = MathProblemGenerator()
    gen.add_funcs(difficult_div)
    gen.add_funcs(difficult_mul)
    gen.add_funcs(difficult_sub)
    gen.add_funcs(difficult_sum)
    
    generated_answer = gen.get_problem()
    
    if request.method == 'POST':
        db_sess = db_session.create_session()
        true_answer = session.get('true_answer')
        print(true_answer)
        if str(request.form['ans']) == str(true_answer):  # session.get('tr_answer') - request.form['ans'] == tr_answer
            
            if not isinstance(current_user, AnonymousUserMixin):
                user = db_sess.query(User).filter(User.email == current_user.email).first()
                if user:
                    user.rating += 20
                    user.user_count_correctly += 1
                    user.user_count_tasks += 1
                    db_sess.commit()
            
            answer = ('Правильно', 1, request.form['ans'])
        else:
            
            if not isinstance(current_user, AnonymousUserMixin):
                user = db_sess.query(User).filter(User.email == current_user.email).first()
                if user:
                    user.user_count_tasks += 1
                    db_sess.commit()
            
            answer = (f'Неправильно,\nПравильный ответ: {true_answer}', 0, request.form['ans'])
            
        session['true_answer'] = generated_answer
        
        return render_template(
                'quests.html',
                type=type,
                answer=answer
            )
        
    session['true_answer'] = generated_answer
    
    return render_template(
        'quests.html',
        type=type,
        answer=answer
    )
