import os
from flask_login import LoginManager, login_required, logout_user
from data import db_session
from flask import Flask, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'our_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

from pages import (
    registration,
    login,
    theory,
    solve,
    lcab,
    quests,
    stats,
    addfriend,
    passwordreset
)


@app.route('/')
def main_page():
    return render_template('main.html')


@app.route('/logout')
@login_required
def logout():
    """Выход из профиля"""

    logout_user()

    return redirect('/')


if __name__ == '__main__':
    db_session.global_init('db\math.db')  # - указать адрес БД
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
