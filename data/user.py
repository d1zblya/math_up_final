import sqlalchemy as sa
from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(SqlAlchemyBase, UserMixin):
    '''Форма создания таблицы пользователей'''
    
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)
    surname = sa.Column(sa.String)
    email = sa.Column(sa.String, index=True)
    hashed_password = sa.Column(sa.String)
    rating = sa.Column(sa.Integer, default=0)
    friends = sa.Column(sa.String)
    user_count_tasks = sa.Column(sa.Integer, default=0)
    user_count_correctly= sa.Column(sa.Integer, default=0)
    
    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
     
    